from django.urls import path
from. import views
urlpatterns = [
    path('projects/', views.project_list_view, name='projects'),
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
]

urlpatterns += [
    path('projects/new/', views.project_create_view, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_update_view, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete_view, name='project_delete'),
]

