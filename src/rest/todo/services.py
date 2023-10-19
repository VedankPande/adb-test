from abc import ABC, abstractmethod


class TodoService(ABC):

    @abstractmethod
    def get_all_todos(self):
        pass

    @abstractmethod
    def create_todo(self):
        pass


class MongoTodoService(TodoService):
    """
    Database service to execute queries for mongo db
    """

    def __init__(self, collection, serializer) -> None:
        self.collection = collection
        self.serializer = serializer

    def get_all_todos(self):
        return [self.serializer.serialize(item)
                for item in self.collection.find()]

    def create_todo(self, task):

        document = {"task": task}

        # insert_one adds an ObjectID to document
        self.collection.insert_one(document)
        return self.serializer.serialize(document)
