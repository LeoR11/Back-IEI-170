from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from biblioteca import views as biblioteca_views

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación API Biblioteca",
      default_version='v1',
      description="Documentación de la API del proyecto de biblioteca",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contacto@biblioteca.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('', biblioteca_views.pagina_inicio, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', biblioteca_views.logout_view, name='logout'),
    path('registro/', biblioteca_views.registro, name='registro'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]