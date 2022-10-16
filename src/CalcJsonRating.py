# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CalcJsonRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        students = []
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
        list1 = list(self.rating.values())
        list1.sort()
        if len(self.data) % 2 == 0:
            mediana = (list1[int((len(list1) - 1) / 2)] +
                       (list1[int(len(list1) / 2)])) / 2
        else:
            mediana = (list1[len(list1)]) / 2
        for rate in self.rating:
            if self.rating[rate] >= mediana:
                students.append(rate)
        return students
