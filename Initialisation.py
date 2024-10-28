import numpy as np

from Exceptions import PopulationSizeException, TravellingSalesMatrixException
from Individual import Individual
from Population import Population

class Initialisation():

    _matrix: np.ndarray
    _population_size: int = -1
    _number_of_cities: int = -1

    def __init__(self, matrix: np.ndarray, population_size: int) -> None:
        shape = matrix.shape
        if len(shape) != 2 or shape[0] != shape[1] : raise TravellingSalesMatrixException(f"The matrix is invalid is invalid, input shape: {shape}")
        self._matrix = matrix #exposure since only read object
        
        self._number_of_cities = matrix.shape[0]
        if population_size <= 0 : raise PopulationSizeException(f"The population size is invalid, input:{population_size}")
        self._population_size = population_size

    #TODO: use random greedy connect
    # for now = random
    def get_initial_population(self) -> Population:
        population = Population(self._population_size)
        for _ in range(self._population_size):
            candidate_solution = np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False) # np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False, p=None)
            individual = Individual()
            individual.use_path_notation(candidate_solution, self._matrix)
            population.add_individual(individual)
        return population