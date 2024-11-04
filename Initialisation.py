import numpy as np

from Exceptions import PopulationSizeException, TravellingSalesMatrixException
from Individual import Individual
from Population import Population

class Initialisation():

    _population_size: int = -1
    _number_of_cities: int = -1

    def __init__(self, population_size: int, distanceMatrix: np.ndarray) -> None:
        shape = distanceMatrix.shape
        if len(shape) != 2 or shape[0] != shape[1] : raise TravellingSalesMatrixException(f"The matrix is invalid is invalid, input shape: {shape}")

        
        self._number_of_cities = distanceMatrix.shape[0]
        if population_size <= 0 : raise PopulationSizeException(f"The population size is invalid, input:{population_size}")
        self._population_size = population_size

    #TODO: use random greedy connect
    # for now = random
    def get_initial_population(self, distanceMatrix: np.ndarray) -> Population:
        population = Population(self._population_size)
        for _ in range(self._population_size):
            candidate_solution = np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False) # np.random.choice(self._number_of_cities, size=self._number_of_cities, replace=False, p=None)
            individual = Individual(self._number_of_cities)
            individual.use_path_notation(candidate_solution)
            population.add_individual(individual)
        return population