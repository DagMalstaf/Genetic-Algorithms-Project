import numpy as np

from Population import Population

class Initilisation():

    _matrix: np.ndarray = np.ndarray()
    _population_size: int = -1

    def __init__(self, matrix: np.ndarray, population_size: int ) -> None:
        self._matrix = matrix #exposure since only read object
        self._population_size = population_size

    #TODO: use random greedy connect
    # for now = random
    def get_initial_population() -> Population:
        pass
        