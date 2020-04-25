from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('recipes/', views.recipes),
    path('recipes/<int:id>/', views.RecipeDeleteView.as_view()),
    path('recipes/<int:id>/update/', views.RecipeUpdateView.as_view()),
    path('recipes/comment/', views.comments),
    path('login/', obtain_jwt_token)
]