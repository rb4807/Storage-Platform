from storage.viewsets import StorageViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('storage',StorageViewsets)