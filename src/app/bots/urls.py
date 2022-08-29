from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import webhook

app_name = "bots"

router = SimpleRouter(False)

urlpatterns = [path("", include(router.urls)), path("webhooks/", webhook)]
