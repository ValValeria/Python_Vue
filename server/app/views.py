import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from .forms import CommentForm, LetterForm, UserForm
from .models import Post, Comment, Carousel, Letter
from django.core.paginator import Paginator
from .classes import ResponseObject
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest
from django.db.models import Q


class LoginView(UserPassesTestMixin, ListView):
    responseObj = ResponseObject()

    def test_func(self):
        return not self.request.user.is_authenticated

    def post(self, request, *args, **kw):
        form = UserForm(True)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is None:
                self.responseObj.add_errors(["You are not in our database"])
            else:
                login(request, user)
                self.responseObj.status = "ok"
        else:
            self.responseObj.add_info(form.errors)

        return JsonResponse(self.responseObj.data_list, safe=False)


class SignUpView(UserPassesTestMixin, ListView):
    responseObj = ResponseObject()

    def test_func(self):
        return not self.request.user.is_authenticated

    def post(self, request, *args, **kw):
        form = UserForm(False)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"],
                                            form.cleaned_data["password"])
            self.responseObj.add_info({id: user.id})
            self.responseObj.status = "ok"
        else:
            self.responseObj.add_errors(form.errors)

        return JsonResponse(self.responseObj.data_list, safe=False)


class LogoutView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_authenticated

    def get(self, request, *args, **kw):
        logout(request)

        return redirect('/')


class LettersView(ListView):
    responseObj = ResponseObject()

    def post(self, request, *args, **kwargs):
        form = LetterForm(request.POST)

        if form.is_valid():
            letter = Letter()
            letter.message = form.cleaned_data['message']
            letter.email = form.cleaned_data['email']
            letter.username = form.cleaned_data['username']
            letter.save()

            self.responseObj.status = "ok"

        return JsonResponse(self.responseObj.data_list, safe=False)


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
        category = request.GET.get('category', '')

        if category != "all":
            category = list(filter(lambda v: v[1] == category, self.categories))[0]

        page = request.GET.get('page', '')
        per_page = request.GET.get('per_page', '')

        self.responseObj.setup_data()

        if page.isdigit() and per_page.isdigit() and category and category[0]:
            if category == "all":
                posts = Post.objects.all().order_by('id').values()
            else:
                posts = Post.objects.filter(category__iexact=category[0]).order_by('id').values()

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

        if page.isdigit() and per_page.isdigit() and 0 <= len(word) < 20:
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
