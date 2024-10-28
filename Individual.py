from typing import List
from copy import deepcopy
import numpy as np

class Individual():

    _distance_matrix: np.ndarray = np.ndarray()
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

        self._distance_matrix = distance_matrix if self._distance_matrix is None else print("Distance matrix already defined")
    def use_cyclic_notation(self, cyclic_notation: List[int], distance_matrix: np.ndarray) -> None:
        self._representation = cyclic_notation
        self._calculate_distance(distance_matrix)

    def use_path_notation(self, path_notation: List[int], distance_matrix: np.ndarray) -> None:
        self._distance_matrix = distance_matrix if self._distance_matrix is None else print("Distance matrix already defined")
        self._representation = self._build_cyclic_notation_from_path(path_notation)
        self._calculate_distance(distance_matrix)

    def _build_cyclic_notation_from_path(self, path_notation: List[int]):

        cyclic_notation: List[int] = [-1]*len(path_notation)

        for city_posittion_in_path, city in enumerate(path_notation):
            cyclic_notation[path_notation[city_posittion_in_path-1]] = city

        if Debug:
            

    def _calculate_distance(self) -> float:
        total_distance = 0.0
        penalty = 1e6  # High penalty for unreachable paths

        for city in range(len(self._representation)):
            city_distance_matrix_index = self._representation[city]
            total_distance += self._distance_matrix[city, city_distance_matrix_index] if self._distance_matrix[city, city_distance_matrix_index] != float('inf') else penalty

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

    

