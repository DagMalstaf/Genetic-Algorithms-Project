from Individual import Individual
from typing import List, Iterable
import numpy as np

class Population():

    _population: List[Individual] = list()

    def __init__(self, population_size: int) -> None:
        self._population_size = population_size

    @staticmethod
    def recombination(inididual1: Individual, indvidual2: Individual) -> List[Individual]:
        pass

    def get(self) -> List[Individual]:
        return self._population
    
    def get_population_size(self) -> int:
        return self._population_size

    def add_individual(self, individual: Individual, distance_matrix: np.ndarray) -> None:
        if individual.get_distance() == 0.0:
            individual.calculate_distance(distance_matrix)
        self._population.append(individual)
    
    def add_individuals(self, individuals: Iterable[Individual], distance_matrix: np.ndarray) -> None:
        self._population.extend(individuals)
    
    def remove_individual(self, individual: Individual) -> None:
        self._population.remove(individual)
    
    def get_objective_values(self) -> List[float]:
        return [individual.get_distance() for individual in self._population]
    
    def __getitem__(self, index: int) -> Individual:
        return self._population[index]

