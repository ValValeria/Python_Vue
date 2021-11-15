import numpy as np


class ResponseObject:
    def __init__(self):
        self.__data = {"result": [], "info": {}}
        self.__errors = []
        self.status = ''
        self.setup_data()

    @property
    def errors(self):
        return self.__errors

    @property
    def data(self):
        return self.__data

    def add_results(self, data):
        self.__data["result"].extend(data)

    def add_info(self, data):
        self.__data["info"].update(data)

    @property
    def data_list(self):
        data = {
            'data': dict(self.__data),
            'errors': list(self.__errors)
        }

        return data

    def setup_data(self):
        self.__errors.clear()
        self.__data["info"].clear()
        self.__data["result"].clear()
