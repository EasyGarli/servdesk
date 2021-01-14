from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from users import views

urlpatterns = [
    path('signup', views.CreateUserAPIView.as_view(), name='signup'),
    path('api-token-auth/', obtain_jwt_token),
    path('test', views.TestAPI.as_view(), name='test'),
    path('user/<email>/', views.UserDetail.as_view(), name='user')
]