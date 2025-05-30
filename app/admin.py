from django.contrib import admin
from .models import Autor, Livro, Editora, Genero, Leitor, Cidade

# Inline de Livro em Autor
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]

# Inline de Livro em Editora
class LivroInlineEditora(admin.TabularInline):
    model = Livro
    extra = 1

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInlineEditora]

# Inline de Livro em Genero
class LivroInlineGenero(admin.TabularInline):
    model = Livro
    extra = 1

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInlineGenero]



# Registro dos modelos no admin
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Cidade)
admin.site.register(Livro)
admin.site.register(Leitor)
