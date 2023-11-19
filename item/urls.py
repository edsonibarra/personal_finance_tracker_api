from rest_framework.routers import DefaultRouter
from item.views import ItemModelViewSet


router = DefaultRouter()
router.register("item", ItemModelViewSet)

urlpatterns = router.urls
