from rest_framework.response import Response
from rest_framework.views import APIView

from drfPolls.models import QuestionDRF,ChoiceDRF
from drfPolls.serializers import QuestionSerializer

class QuestionAPIView(APIView):
    def get(self, request):
        lst = QuestionDRF.objects.all().values()
        return Response({'name':'poll','questions': list(lst)})

