from dataclasses import field
from rest_framework import serializers
from main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','title', 'content','creatd_at','updated_at')
        # field = '__all__'