from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contractor
from .producers import send_event


class ContractorCreateView(APIView):
    def post(self, request):
        name = request.data.get('name')
        contractor = Contractor.objects.create(name=name)
        send_event('contractor.created', {
                   'id': contractor.id, 'name': contractor.name})
        return Response({'status': 'created', 'id': contractor.id})
