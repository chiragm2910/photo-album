from rest_framework import serializers
from .models import Photo, Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'photos')


class PhotoSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'user', 'description', 'image', 'created_at', 'updated_at', 'albums')
