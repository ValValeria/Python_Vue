import numpy as np


class ResponseObject:
    def __init__(self):
        self.__errors = []
        self.__data = {"result": [], "info": []}

    @property
    def errors(self):
        return self.__errors

    @property
    def data(self):
        return self.__data

    def add_results(self, data):
        self.__data["result"].extend(data)

    def add_info(self, data):
        self.__data["info"].extend(data)
