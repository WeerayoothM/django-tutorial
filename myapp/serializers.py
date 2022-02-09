# file ที่บอกว่าเราจะจัดเก็บ หรือ show ข้อมูลใน field ไหนบ้าง

from rest_framework import serializers
from .models import Todolist


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id', 'title', 'detail')
