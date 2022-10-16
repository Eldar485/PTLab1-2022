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
            for line in json_file:
                if line.strip().endswith(": {"):
                    self.key = line.strip()[1:line.find(':') - 3]
                    self.students[self.key] = []
                if not line.strip().startswith("{") \
                        and not line.strip().startswith("}") \
                        and not line.strip().endswith(": {") \
                        and not line.startswith("}"):
                    subj, score = line[0:len(line) - 1].split(':', maxsplit=1)
                    if score[len(score) - 1] == ',':
                        score = score[0:len(score) - 1]
                    self.students[self.key].append(
                        (subj.strip()[1:len(subj) - 5], int(score.strip())))

        return self.students
