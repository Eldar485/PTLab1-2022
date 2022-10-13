# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json
from abc import ABC, abstractmethod


class JsonDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as json_file:
            self.students = json.load(json_file)
            print(self.students)
        return self.students
