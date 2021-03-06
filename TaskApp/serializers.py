from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'user', 'description', 'image', 'created_at', 'updated_at', 'albums')
        read_only_fields = ('id', 'created_at', 'updated_at')


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'photos')
        read_only_fields = ('id', 'created_at', 'updated_at')
