from django.contrib import admin
from .models import Song
from .models import Artiste
from .models import Lyric

admin.site.register(Song)
admin.site.register(Artiste)
admin.site.register(Lyric)