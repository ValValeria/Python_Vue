from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .classes import ResponseObject
from django.http import JsonResponse, HttpResponseForbidden


# Create your views here.
class PostsView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        if page.isdigit() and per_page.isdigit():
            posts = Paginator(Post.objects.all().order_by('id').values(), int(per_page))
            page_obj = posts.page(int(page))
            num_pages = posts.num_pages if posts.num_pages else 0

            self.responseObj.add_results(list(page_obj.object_list))
            self.responseObj.add_info({"all_pages": num_pages, "results": posts.count})

            return JsonResponse(self.responseObj.data_list, safe=False)
        else:
            return
        pass


class SearchView(ListView):
    responseObj = ResponseObject()

    def get(self, request, *args, **kw):
        word = request.GET.get('search')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        if page.isdigit() and per_page.isdigit() and 3 < len(word) < 20:
            posts = Post.objects.filter(title__icontains=word).order_by('id')
            posts = Paginator(posts.values(), per_page)
            page_obj = posts.page(int(page))
            posts_for_page = list(page_obj.object_list)
            info = {"all_pages": posts.num_pages}

            self.responseObj.add_results(posts_for_page)
            self.responseObj.add_info(info)

            return JsonResponse(self.responseObj.data_list, safe=False)

        return HttpResponseForbidden()



