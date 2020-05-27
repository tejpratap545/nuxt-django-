from django.urls import path, re_path
from rest_framework import routers
from .views import videosviewset, tagviewset
router = routers.DefaultRouter()
router.register('video', videosviewset)
router.register('tag', tagviewset)
urlpatterns = router.urls
