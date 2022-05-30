from django.urls import path, include, re_path
from Media import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name = 'search_results'),
    # re_path(r'^display/<int:image_id>/', views.index, name = 'show_images'),
    # path('<int:image_id>/show_single_image', views.show_single_image, name='show_single_image'),
    path('post_location/location/', views.post_location, name='post_location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  