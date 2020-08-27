from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from .views import ModsView

router = SimpleRouter()

router.register('token', TokenObtainPairView.as_view(), basename='token_obtain_pair')
router.register('token/refresh', TokenRefreshView.as_view(), basename='token_refresh')
router.register('mods', ModsView.as_view(), basename='mods_view')

urlpatterns = router.urls