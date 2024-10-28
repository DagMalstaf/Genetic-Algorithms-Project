from typing import List
from copy import deepcopy
import numpy as np

class Individual():

    _representation : np.ndarray 
    _distance: float = 0.0

    def __init__(self) -> None:
        self._representation = np.empty(0)
        self._distance = 0.0

    def __repr__(self) -> str:
        return f"Individual(route={self._representation}, distance={self._distance})"

    def __eq__(self, other: object) -> bool:
            if not isinstance(other, Individual):
                return NotImplemented
            return self._distance == other._distance

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            return NotImplemented
        return self._distance > other._distance

    def use_cyclic_notation(self, cyclic_notation: np.ndarray) -> None:
        self._representation = cyclic_notation

    def use_path_notation(self, path_notation: np.ndarray, distance_matrix: np.ndarray) -> 'Individual':
        self._representation = path_notation
        self.calculate_distance(distance_matrix)
        return self

    def calculate_distance(self, distance_matrix: np.ndarray) -> float:
        total_distance = 0.0
        penalty = 1e6  # High penalty for unreachable paths
        n_cities = distance_matrix.shape[0]

        for i in range(len(self._representation) - 1):
            from_city = self._representation[i]
            to_city = self._representation[i + 1]

            if from_city >= n_cities or to_city >= n_cities:
                raise ValueError(f"City index out of bounds: {from_city} or {to_city}")

            distance = distance_matrix[from_city, to_city]
            if distance == float('inf'):
                total_distance += penalty  
            else:
                total_distance += distance

        from_city = self._representation[-1]
        to_city = self._representation[0]
        if distance_matrix[from_city, to_city] == float('inf'):
            total_distance += penalty
        else:
            total_distance += distance_matrix[from_city, to_city]

        self._distance = total_distance
        return self._distance


    def get_cyclic_representation(self) -> List[int]:
        return deepcopy(self._representation)
    
    def get_distance(self) -> float:
        return self._distance
    
    @property
    def size(self) -> int:
        return len(self._representation)
    
    def __getitem__(self, index: int) -> int:
        return self._representation[index]


    #Iterator along route

    #'Iterator' builder 

    

