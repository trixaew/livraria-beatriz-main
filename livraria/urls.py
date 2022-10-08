from django.contrib import admin
from django.urls import include, path
from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'livros', LivroViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
