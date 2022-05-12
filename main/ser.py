from rest_framework import serializers
from main.models import *

ser = serializers.ModelSerializer

class GroupSerializer(ser):
    class Meta:
        model = Group
        fields = "__all__"

class PupilSerializer(ser):
    class Meta:
        depth = 1
        model = Pupil
        fields = "__all__"

class DavomatSerializer(ser):
    class Meta:
        model = Davomat
        fields = "__all__"