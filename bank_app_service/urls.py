"""
URL configuration for bank_app_service project.
-> Develop by 'Heiner Acosta'
"""
from django.contrib import admin
from django.urls import path
from app.controllers.bank_controller import BankController
from app.controllers.link_controller import LinkController
from app.controllers.account_controller import AccountController
from app.controllers.user_controller import RegisterController, LoginConstroller, UserProfileController, LogoutController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banks', BankController.as_view(), name="bank-detail"),
    path('banks/link', LinkController.as_view(), name="link-banks-detail"),
    path('banks/link/<str:link_id>', LinkController.as_view(), name="links"),
    path('account/<str:link_id>', AccountController.as_view(), name="accounts-detail"),
    path('account/<str:link_id>/<str:account_id>/', AccountController.as_view(), name="account-id-detail"),
    path('api/auth/register/', RegisterController.as_view(), name='register'),
    path('api/auth/login/', LoginConstroller.as_view(), name='login'),
    path('api/auth/logout/', LogoutController.as_view(), name='logout'),
    path("user/profile/", UserProfileController.as_view(), name="user-profile"),
]
