from Individual import Individual
from typing import List, Iterable, Set
import numpy as np

class Population():

    _population: List[Individual] = list()
    _population_size: int = 0

    def __init__(self, population_size: int) -> None:
        self._population_size = population_size # fixed value

    def get(self) -> List[Individual]:
        return self._population
    
    def __iter__(self):
        return self
    def __next__(self):
        pass

    def get_original_population_size(self) -> int:
        return self._population_size
    
    def get_current_population_size(self) -> int:
        return len(self._population)

    def add_individual(self, individual: Individual) -> None:
        self._population.append(individual)
    
    def add_individuals(self, individuals: Iterable[Individual]) -> None:
        self._population.extend(individuals)
    
    def remove_individual(self, individual: Individual) -> None:
        self._population.remove(individual)
    
    def get_objective_values(self, distance_matrix: np.ndarray) -> List[float]:
        return [individual.get_distance(distance_matrix) for individual in self._population]
    
    def __getitem__(self, index: int|np.intp) -> Individual:
        return self._population[index]

