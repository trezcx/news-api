from rest_framework import routers
from main.views import ApplicationViewSet, NewsViewSet

router = routers.DefaultRouter()

router.register(r'application', ApplicationViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    *router.urls
]
