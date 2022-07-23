from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('review', ReviewViewSet)

urlpatterns = router.urls
