from django.urls import include, path
from rest_framework.routers import SimpleRouter

app_name = "bots"

router = SimpleRouter(False)

urlpatterns = [
    path("", include(router.urls)),
]
