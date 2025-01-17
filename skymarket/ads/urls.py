from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet
from rest_framework_nested.routers import NestedSimpleRouter

router = SimpleRouter()

router.register('ads', AdViewSet, basename='ads')

comments_router = NestedSimpleRouter(
    router,
    'ads',
    lookup='ad'
)

comments_router.register('comments', CommentViewSet, basename='ad_comments')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(comments_router.urls)),
]
