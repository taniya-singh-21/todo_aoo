from django.urls import path
from. import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('done/<int:id>',views.mark_as_done,name='done'),
    path('new/',views.new_todo,name='new'),
    path('delcomplete/',views.deleteCompleted,name='delcomplete'),
    path('deleteall/',views.deleteall,name='deleteall'),

]
