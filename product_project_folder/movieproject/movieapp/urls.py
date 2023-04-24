from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [

    path('',views.index,name="index"),
    path('movie/<int:mov_id>/',views.detail,name="detail"),
    path('add/',views.add_movie,name='add_name'),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/', views.delete, name="delete")

]
