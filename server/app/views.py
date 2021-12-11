from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView

from .forms import CommentForm
from .models import Post, Comment, Carousel
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .classes import ResponseObject
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest
from django.db.models import Q
from django.db import models
import django.utils.timezone

class PostsSortByCategory(ListView):
   responseObj = ResponseObject()
   categories = (
           ("js", "javascript"),
           ("python", "python"),
           ("ml", "machine learning"),
           ("android", "android development"),
           ("other", "other"),
       )

   def get(self, request, *args, **kwargs):
       category = list(filter(lambda v: v[1] == kwargs['category'], self.categories))[0]
       page = request.GET.get('page', '')
       per_page = request.GET.get('per_page', '')

       if page.isdigit() and per_page.isdigit() and category and category[0]:
          posts = Post.objects.filter(category=category[0]).order_by('id').values()

          if category == "all":
             posts = Post.objects.all().order_by('id').values()

          posts = Paginator(posts, int(per_page))
          page_obj = posts.page(int(page))
          num_pages = posts.num_pages if posts.num_pages else 0

          self.responseObj.add_results(list(page_obj.object_list))
          self.responseObj.add_info({"all_pages": num_pages, "results": posts.count})

          return JsonResponse(self.responseObj.data_list, safe=False)

       return HttpResponseBadRequest()



# Create your views here.
class PostsView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        self.responseObj.setup_data()

        if page.isdigit() and per_page.isdigit():
            posts = Post.objects.all().order_by('id').values()
            posts = Paginator(posts, int(per_page))
            page_obj = posts.page(int(page))
            num_pages = posts.num_pages if posts.num_pages else 0

            self.responseObj.add_results(list(page_obj.object_list))
            self.responseObj.add_info({"all_pages": num_pages, "results": posts.count})

            return JsonResponse(self.responseObj.data_list, safe=False)

        return HttpResponseBadRequest()


class PostView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kwargs):
        post_id = kwargs['id']
        post = Post.objects.filter(id=int(post_id)).values()[0]

        self.responseObj.setup_data()

        if post is not None:
            self.responseObj.data['result'].append(post)

        return JsonResponse(self.responseObj.data_list, safe=False)


class AddLikesView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kwargs):
        self.responseObj.setup_data()

        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        post_id = request.GET.get('post_id')

        if not post_id.isdigit():
            return HttpResponseBadRequest()

        post = Post.objects.filter(id=int(post_id))[0]

        if post is None:
            return HttpResponseNotFound()

        post.users_likes.add(request.user)
        self.responseObj.add_info("ok")

        return JsonResponse(self.responseObj.data_list, safe=False)


class GetLikesView(ListView, LoginRequiredMixin):
    responseObject = ResponseObject()

    def get(self, request, *args, **kw):
        user = request.user
        posts = user.post_set.all()
        self.responseObject.add_results(posts)
        return JsonResponse(self.responseObject.data_list, safe=False)


class CommentsView(ListView):
    responseObject = ResponseObject()

    def get(self, request, *args, **kw):
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')
        post_id = request.GET.get('post_id')
        queries = [page, per_page, post_id]

        self.responseObject.setup_data()

        if filter(lambda x: x.isdigit(), queries):
            comments = Paginator(Comment.objects.all().order_by('id').values(), int(per_page))
            page_obj = comments.page(int(page))
            num_pages = comments.num_pages if comments.num_pages else 0
            results = list(page_obj.object_list)
            info = {"all_pages": num_pages, "results": comments.count}

            self.responseObject.add_results(results)
            self.responseObject.add_info(info)

            return JsonResponse(self.responseObject.data_list, safe=False)

        return HttpResponseBadRequest()


class AddCommentView(ListView, LoginRequiredMixin):
    resObj = ResponseObject()
    login_url = '/login'

    def post(self, request, *args, **kw):
        user = request.user
        form = CommentForm(request.POST)

        self.resObj.setup_data()

        if form.is_valid():
            cleaned_data = form.cleaned_data
            comment = Comment(content=cleaned_data['content'], time=timezone.now())
            comment.user = user
            comment.post = Post.objects.get(int(cleaned_data['post_id']))
            comment.save()

            self.resObj.status = 'ok'

        else:
            self.resObj.errors.append("Check the validity of fields")

        return JsonResponse(self.resObj.data_list, safe=False)


class SearchView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kw):
        word = request.GET.get('search')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        self.responseObj.setup_data()

        if page.isdigit() and per_page.isdigit() and 3 < len(word) < 20:
            posts = Post.objects.filter(Q(title__icontains=word) | Q(category__icontains=word))
            posts = Paginator(posts.order_by('id').values(), per_page)
            page_obj = posts.page(int(page))
            posts_for_page = list(page_obj.object_list)
            info = {"all_pages": posts.num_pages}

            self.responseObj.add_results(posts_for_page)
            self.responseObj.add_info(info)

            return JsonResponse(self.responseObj.data_list, safe=False)

        return HttpResponseForbidden()


class CarouselView(ListView):
    responseObj = ResponseObject()
    allowed_pages = ("posts", "post", "categories")

    def get(self, request, *args, **kw):
        page = request.GET.get('page_type')
        self.responseObj.setup_data()

        if page not in self.allowed_pages:
            return HttpResponseNotFound()

        images = list(Carousel.objects.filter(page=page).values())
        self.responseObj.add_results(images)

        return JsonResponse(self.responseObj.data_list, safe=False)

