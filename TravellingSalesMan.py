import numpy as np
from typing import Double, Tuple
from Parameters import Parameters
from Population import Population

class TravellingSalesMan():

    def __init__(self, matrix: np.ndarray, parameters: Parameters) -> None:
        self.matrix = matrix
        self.parameters = parameters


    def run(self, population: Population) -> Tuple[Double, Double, np.ndarray]:
        pass