from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserDestroyAPIView, UserListAPIView, \
    UserRetrieveAPIView, UserUpdateAPIView, UserCreateAPIView, PaymentCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
