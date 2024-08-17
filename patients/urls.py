from rest_framework.routers import DefaultRouter
from .views import PacienteViews

router = DefaultRouter()
router.register(r'patients', PacienteViews, basename='patients')

urlpatterns = router.urls

