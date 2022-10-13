from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from IDZapk.views import UserViewSet
# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('IDZapk.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

admin.site.site_header = "Api Admin"
admin.site.site_title = "Api Admin Portal"
admin.site.index_title = "Welcome to Api"
admin.site.app_index = "Api"