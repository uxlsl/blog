# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import MovieRes


class MovieResSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRes
        fields = ('name', 'url', 'source', 'down_urls')

    def create(self, validated_data):
        print(validated_data)
        return MovieRes.create(validated_data)
