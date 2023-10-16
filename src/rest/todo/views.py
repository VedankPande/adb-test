from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

            print("latest todo", todo_objects)
            return Response(todo_objects, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):

        print(request.body.decode('utf-8'))
        #self.todo.insert_one()
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        return Response({}, status=status.HTTP_200_OK)