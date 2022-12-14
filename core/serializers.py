from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Autor, Categoria

class AutorSerializer(ModelSerializer):
    class Meta: 
        model = Autor
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Livro 

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
        
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1