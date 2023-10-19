import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.json_encoder import MongoDocumentJSONEncoder
from utils.database import MongoDBDatabase
from utils.serializer import MongoDocumentSerializer
from utils.validators import TodoCreateValidator, ValidationException
from utils.decorators import validate
from .services import MongoTodoService


class TodoListView(APIView):
    """
    description:
    Restful API view to handle requests to the todo resource

    get:
    Return a list of all existing todos

    post:
    Create a new todo document
    """

    # TODO: Does this need to be a class variable or instance variable?
    mongo_uri = 'mongodb://' + \
        os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]

    todo = MongoDBDatabase(mongo_uri, os.environ["DATABASE"]).get_collection(
        os.environ["TODO_COLLECTION"])

    mongoSerializer = MongoDocumentSerializer(encoder=MongoDocumentJSONEncoder)
    mongoService = MongoTodoService(todo, serializer=mongoSerializer)

    def get(self, request):

        try:
            todo_documents = self.mongoService.get_all_todos()
            return Response(data=todo_documents, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @validate(validator_class=TodoCreateValidator)
    def post(self, request, *args, **kwargs):

        try:
            document = self.mongoService.create_todo(
                kwargs.get("validated_data", ""))

            return Response(data=document, status=status.HTTP_201_CREATED)

        except ValidationException as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
