from rest_framework import serializers
from issueTrackerApp.models import Issue

#issues serializer
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
