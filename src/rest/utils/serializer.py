import json

from abc import ABC, abstractmethod


class Serializer(ABC):

    @abstractmethod
    def serialize(self, object, encoder=None):
        pass


class MongoDocumentSerializer(Serializer):
    def __init__(self, encoder=None):
        self.encoder = encoder

    def serialize(self, object):

        return json.dumps(object, cls=self.encoder)
