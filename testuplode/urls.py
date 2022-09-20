
from django.urls import path

from rest_framework import routers
from .views import UplodList

router = routers.SimpleRouter()
router.register(r'data', UplodList)

urlpatterns = router.urls    