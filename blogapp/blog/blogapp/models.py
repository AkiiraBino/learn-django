from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #Заголовок поста
    title = models.CharField(max_length=250)
    #URL для записи блога
    slug = models.SlugField(max_length=250, unique_for_date='time_publish')
    #Автор записи в блоге
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    #Основное текстовое поле поста
    body = models.TextField()
    #Время публикации
    time_publish = models.DateTimeField(default=timezone.now)
    #Время создания
    time_created = models.DateTimeField(auto_now_add=True)
    #Время обновления
    time_updated = models.DateTimeField(auto_now=True)
    #Опубликована/Неопубликована
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        #создание url адреса по именам
        #strftime позволяет построить из даты строку с ведущими нулями, а именно тут месяц и день
        return reverse('blogapp:post_detail',
                        args=[self.time_publish.year,
                                self.time_publish.strftime('%m'),
                                self.time_publish.strftime('%d'),
                                self.slug])

#Сортировка по времени публикации в убывающем порядке
class Meta:
    ordering = ('-time_publish',)


#Стандартное представление объекта для джанги
def __str__(self):
    return self.title