from rest_framework import serializers

from drfPolls.models import QuestionDRF
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDRF
        fields = ("description","pub_date")