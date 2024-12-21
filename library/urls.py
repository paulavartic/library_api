from rest_framework.routers import SimpleRouter

from library.apps import LibraryConfig
from library.views import BookViewSet

app_name = LibraryConfig.name

router = SimpleRouter()
router.register('', BookViewSet)


urlpatterns = []

urlpatterns += router.urls
