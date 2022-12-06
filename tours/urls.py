from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.main_page, name = 'main_page'),
    path('advantages/', views.advantages, name = 'advantages'),
    path('tours/', views.tours, name = 'tours'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('category_tour/<str:arg>', views.category_tour, name = 'category_tour'),
    path('commentaries/', views.commentaries, name = 'comment_block'),
    path('commentaries/add_comment', views.left_comment, name = 'left_comment'),
    path('add_message', views.left_message, name = 'left_message'),
    path('proposal/<int:arg>', views.proposal, name = 'proposal'),
    path('add_response/<int:arg>', views.add_response, name = 'add_response'),
    path('create_comment/<int:arg>', views.create_comment, name = 'create_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
