
from django.urls import path

from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movieid>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:movieid>/',views.update,name='update'),
    path('delete/<int:movieid>/',views.delete,name='delete')
]