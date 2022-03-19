from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view()),
    path("category/", views.CategoryListView.as_view()),
    path("category/create/", views.CategoryCreateView.as_view()),
    path("category/<int:pk>", views.CategoryEditView.as_view()),
]