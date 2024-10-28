from Individual import Individual
from typing import List, Iterable
import numpy as np

class Population():

    _population: List[Individual] = list()
    _population_size: int = 0

    def __init__(self, population_size: int) -> None:
        self._population_size = population_size # fixed value

    def get(self) -> List[Individual]:
        return self._population
    
    def get_original_population_size(self) -> int:
        return self._population_size
    
    def get_current_population_size(self) -> int:
        return len(self._population)

    def add_individual(self, individual: Individual) -> None:
        if individual.get_distance() == 0.0:
            individual.get_distance()
        self._population.append(individual)
    
    def add_individuals(self, individuals: Iterable[Individual], distance_matrix: np.ndarray) -> None:
        self._population.extend(individuals)
    
    def remove_individual(self, individual: Individual) -> None:
        self._population.remove(individual)
    
    def get_objective_values(self) -> List[float]:
        return [individual.get_distance() for individual in self._population]
    
    def __getitem__(self, index: int|np.intp) -> Individual:
        return self._population[index]

