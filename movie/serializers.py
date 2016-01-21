# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import MovieRes, MovieNotify


class MovieResSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRes
        fields = ('name', 'url', 'source', 'down_urls')

    def create(self, validated_data):
        return MovieRes.create(validated_data)


class MovieNotifySerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieNotify
        fields = ('key', 'email')
