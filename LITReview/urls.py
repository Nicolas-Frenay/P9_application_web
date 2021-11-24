"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import review.views
from django.contrib.auth.views import (LoginView, LogoutView)
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='review/login.html',
                               redirect_authenticated_user=True),
         name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('home/', review.views.home, name='home'),
    path('signup/', review.views.signup, name='signup'),
    path('posts/', review.views.posts, name='posts'),
    path('subs/', review.views.subs, name='subs'),
    path('create_ticket/', review.views.create_ticket, name='create_ticket'),
    path('create_review/', review.views.create_review, name='create_review'),
    path('ticket_response/<int:ticket_id>/', review.views.ticket_response,
         name='ticket_response'),
    path('delete_sub/<int:sub_id>/', review.views.delete_sub,
         name='delete_sub'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
