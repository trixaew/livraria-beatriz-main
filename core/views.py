from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Autor, Categoria, Editora, Livro
from core.serializers import AutorSerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [IsAuthenticated]
    
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer
