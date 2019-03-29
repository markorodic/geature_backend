from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from users import views as user_views
from projects import views as project_views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'projects', project_views.ProjectsViewSet, basename="project")


urlpatterns = [
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('admin/', admin.site.urls),
     path('api-token-auth/', views.obtain_auth_token),
]