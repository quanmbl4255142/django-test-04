from rest_framework import generics
from django.http import JsonResponse
from .models import cook
from .serializers import cookSerializer


class cookListCreateView(generics.ListCreateAPIView):
    queryset = cook.objects.all()
    serializer_class = cookSerializer


class cookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = cook.objects.all()
    serializer_class = cookSerializer


# API endpoint để lấy thông tin health check
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'message': 'django-test-04 API is running!'
    })
