from django.urls import path

from blogapp.views import *



app_name = 'blogapp'
urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path(
        #Регулярное выражение, последовательность из 4, 2, 2 цифр и последовательность из всяких символов   
        '<int:year>/<int:month>/<int:day>/<str:post>/',
        post_detail,
        name='post_detail'
    )
]
