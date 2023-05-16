from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from actresses import models
from .forms import AddPostForm
from .utils import *


class ActressesHome(DataMixin, ListView):
    model = models.Actresses
    template_name = 'actresses/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return models.Actresses.objects.filter(is_published=True)


class ActressesCategory(DataMixin , ListView):
    model = models.Actresses
    template_name = 'actresses/index.html'
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self) -> QuerySet[Any]:
        return models.Actresses.objects.filter( cat_id__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
                title=' '.join(['Категория', str(context['posts'][0].cat_id)]), 
                cat_selected=context['posts'][0].cat_id
            )
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'actresses/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'actresses/addpage.html'
    login_url = reverse_lazy('home')
    raise_exception = True
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
                title='Добавление'
            )
        return dict(list(context.items()) + list(c_def.items()))
    

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = models.Actresses
    template_name = 'actresses/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
                title=context['post']
            )
        return dict(list(context.items()) + list(c_def.items()))
    

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'actresses/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
                title='Регистрация'
            )
        return dict(list(context.items()) + list(c_def.items()))