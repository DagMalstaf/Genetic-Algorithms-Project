from Individual import Individual
from typing import List

class Population():

    _population: List[Individual] = list()

    def __init__(self) -> None:
        pass

    @staticmethod
    def recombination(inididual1: Individual, indvidual2: Individual) -> List[Individual]:
        pass

    def get(self) -> List[Individual]:
        return self._population

    def add_individual(self, individual: Individual) -> None:
        pass
