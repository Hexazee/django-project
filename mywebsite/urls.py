from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
    #     name="password-reset"),

    # path('password-reset-confirm/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    #     name="password_reset_confirm"),

    # path('password-reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
    #     name="password_reset_done"),

    # path('signup/', user_view.signup, name='user-signup'),
    # path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='user-signin'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    # path('profile/', user_view.profile, name='user-profile'),
    path('accounts/', include('allauth.urls')),
    path('', include('shop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
