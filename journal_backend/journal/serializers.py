from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ('id', 'user', 'content', 'created_at')
        read_only_fields = ('id', 'created_at','user')
