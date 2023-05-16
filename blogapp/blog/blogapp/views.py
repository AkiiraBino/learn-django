from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post

# Create your views here.

# def posts_list(request) -> render:
#     posts = {}
#     #Достаем из базы все опубликованные
#     posts['posts'] = Post.objects.filter(status = 'published').all()
#     #Создаю пагинатор из постов по 2 на страницу
#     paginator = Paginator(posts['posts'], 2)
#     #Делаем получаем номер текущей страницы
#     page = request.GET.get('page')
#     try:
#         #Пробуем отобразить взять посты этой страницы
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         #Если параметр не целое число то берем первую страницу
#         posts = paginator.page(1)
        
#     except EmptyPage:
#         #Если страница больше чем количество страниц то возвращаем последнюю
#         posts = paginator.page(paginator.num_pages)

#     dict_html = {}
#     dict_html['page'], dict_html['posts'] = page, posts
#     #Рендерим их на index.html
#     return render(
#             request, 'blogapp/post/list.html', dict_html
#         )


class PostListView(ListView):
    queryset = Post.objects.filter(status = 'published').all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blogapp/post/list.html'

def post_detail(request, year, month, day, post) -> render:
    #Выдает объект по заданным параметрам или ошибку 404
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   time_publish__year=year,
                                   time_publish__month=month,
                                   time_publish__day=day)
    return render(request,'blogapp/post/detail.html', {'post': post})