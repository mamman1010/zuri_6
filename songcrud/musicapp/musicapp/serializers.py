from rest_framework import serializers
from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.ModelSerializer):
    class Meat:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']