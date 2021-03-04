from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register( r'users', views.UserViewSet)
router.register( r'groups', views.GroupViewSet)

