import numpy as np

from Exceptions import PopulationSizeException, TravellingSalesMatrixException
from Individual import Individual
from Population import Population

class Initilisation():

    _matrix: np.ndarray = np.ndarray()
    _population_size: int = -1
    _number_of_cities: int = -1

    def __init__(self, matrix: np.ndarray, population_size: int ) -> None:
        if len(matrix.size) != 2 or matrix.size[0] != matrix.size[1] : raise TravellingSalesMatrixException(f"The matrix is invalid is invalid, input size:{matrix.size}")
        self._matrix = matrix #exposure since only read object
        
        self._number_of_cities = matrix.size[0]
        if population_size <= 0 : raise PopulationSizeException(f"The population size is invalid, input:{population_size}")
        self._population_size = population_size

    #TODO: use random greedy connect
    # for now = random
    def get_initial_population(self) -> Population:
        population = Population()
        for _ in range(self._population_size):
            candidate_solution = np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False) # np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False, p=None)
            
            population.add_individual(Individual(candidate_solution))

        return population