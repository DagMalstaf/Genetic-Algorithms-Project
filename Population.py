from Individual import Individual
from typing import List

class Population():

    _population: List[Individual] = list()

    def __init__(self, population: List[Individual]) -> None:
        self._population = population

    @staticmethod
    def recombination(inididual1: Individual, indvidual2: Individual) -> List[Individual]:
        pass

    def get(self) -> List[Individual]:
        return self._population

    def add_individual(self, individual: Individual) -> None:
        self._population.append(individual)
    
    def add_individuals(self, individuals: List[Individual]) -> None:
        self._population.extend(individuals)
    
    def remove_individual(self, individual: Individual) -> None:
        self._population.remove(individual)
