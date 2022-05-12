from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, APIView, authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from main.models import *
from main.ser import *


class GroupView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        group = Group.objects.all()
        ser = GroupSerializer(group, many=True)
        return Response(ser.data)

    def post(self, request):
        user = request.user
        if user.type == 1:
            name = request.data['name']
            force = Group.objects.create(name=name)
            addmission = GroupSerializer(force)
            return Response(addmission.data)

class PupilView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.type == 1:
            group = Pupil.objects.all()
            ser = PupilSerializer(group, many=True)
            return Response(ser.data)
    
    def post(self, request):
        group = request.data['group']
        full_name = request.data['full_name']
        phone = request.data['phone']
        parents_id = request.POST.get('parents_id')
        force = Pupil.objects.create(
            group_id=group,
            full_name=full_name,
            phone=phone,
            parents_id=parents_id
        )
        addmission = PupilSerializer(force)
        return Response(addmission.data)

class DavomatView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.type == 1:
            davomat = Davomat.objects.all()
            dava = DavomatSerializer(davomat, many=True)
            return Response(dava.data)

    def post(self, request):
        user = request.user
        if user.type == 1:
            day = request.data['day']
            time = request.data['time']
            pupil = request.data['pupil']
            davomat = request.data['davomat']
            force = Davomat.objects.create(
                day=day,
                time=time,
                pupil_id=pupil,
                davomat=davomat
            )
            addmission = DavomatSerializer(force)
            return Response(addmission.data)

@api_view(['GET'])
def DavomatTrue(request):
    day = request.GET.get("day")
    davomat = Davomat.objects.filter(day=day, davomat=True)
    dav = DavomatSerializer(davomat, many=True)
    return Response(dav.data)

@api_view(['GET'])
def DavomatFalse(request):
    day = request.GET.get("day")
    davomat = Davomat.objects.filter(day=day, davomat=False)
    dav = DavomatSerializer(davomat, many=True)
    return Response(dav.data)