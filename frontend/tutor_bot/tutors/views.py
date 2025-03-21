from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tutor
from .serializers import TutorSerializer

@api_view(['POST'])
def register_tutor(request):
    if request.method == 'POST':
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_tutors(request):
    specialization = request.GET.get('specialization', '')
    location = request.GET.get('location', '')
    tutors = Tutor.objects.filter(specialization__icontains=specialization, location__icontains=location)
    serializer = TutorSerializer(tutors, many=True)
    return Response(serializer.data)
