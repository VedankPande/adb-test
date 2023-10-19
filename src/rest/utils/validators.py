from abc import ABC, abstractmethod


class ValidationException(Exception):
    pass


class Validator(ABC):

    @abstractmethod
    def is_valid(self):
        pass

    @property
    @abstractmethod
    def validated_data(self):
        pass

    @property
    @abstractmethod
    def validated_data(self):
        pass


class TodoCreateValidator(Validator):
    def __init__(self, data):
        self.data = data
        self._validated_data = None
        self._error = None

    def is_valid(self):

        task = self.data.get("task", "")

        if len(task)==0:
            self.error = "Task is not present"
            return False
        self.validated_data = {"task": task}
        return True

    @property
    def validated_data(self):
        if not self._validated_data:
            raise ValidationException(
                "Data hasn't been validated yet, call 'is_valid' before accessing validated_data")
        return self._validated_data

    @validated_data.setter
    def validated_data(self, data):
        self._validated_data = data

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, err):
        self._error = err