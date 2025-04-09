from django.contrib import admin
from .models import Movie, Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title', 'description')
    list_filter = ('genres', 'release_date')
    fields = ('title', 'description', 'thumbnail', 'video_file', 'release_date', 'genres', 'trailer_file', 'trailer_link')  # thêm dòng này


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


