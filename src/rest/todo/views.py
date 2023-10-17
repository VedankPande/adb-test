from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer
from utils.database import get_db_connection
from utils.json_encoder import JSONEncoder
import json
import logging
import os


class TodoListView(APIView):
    todo = get_db_connection()['todos']

    def get(self, request):

        try:
            todo_items = self.todo.find()
            todo_objects = [json.dumps(item, cls=JSONEncoder)
                            for item in todo_items]

            return Response(data=todo_objects, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):

        serializer = TaskSerializer(data=request.data)
        try:

            if serializer.is_valid():

                validated_data = serializer.validated_data
                document = {"task": validated_data["task"]}
                self.todo.insert_one(document)

                return Response(data= json.dumps(document, cls=JSONEncoder), status=status.HTTP_201_CREATED)

            else:

                return Response(data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(data={"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
