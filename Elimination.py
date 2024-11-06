import numpy as np
from Population import Population
from EvolutionaryFunctions import EvolutionaryFunctions


class Elimination():

    _k: int
    _distance_matrix: np.ndarray
    
    def __init__(self, k: int, distance_matrix: np.ndarray) -> None:
        self._k = k
        self._distance_matrix = distance_matrix

        
    def eliminate(self, population: Population) -> Population:

        while (population.get_current_population_size() != population.get_original_population_size()):
            individual = EvolutionaryFunctions.k_tournament(population, self._k, self._distance_matrix, max)
            population.remove_individual(individual)

        return population
    
    def set_k(self, k) -> None:
        self._k = k

    def get_k(self) -> int:
        return self._k

        