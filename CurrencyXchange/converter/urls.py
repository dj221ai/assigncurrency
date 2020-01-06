from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.CreateUserView)
router.register('api', views.UserBalanceView)


urlpatterns = [
    path('', include(router.urls)),
]
