import random
from tkinter import NO
from typing import List
from copy import deepcopy
import numpy as np
from Exceptions import CyclicNotationException
from Debug import Debug

class Individual():
    _representation : np.ndarray 
    _distance: float = -1

    _current_index = 0

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
    
    def __getitem__(self, index: int) -> int:
        return self._representation[index]
    
    def __hash__(self):

        return hash(str(self._representation))
    
    @property
    def size(self) -> int:
        return self._representation.size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        tmp = self._representation[self._current_index]
        self._current_index = tmp
        return tmp

    def use_cyclic_notation(self, cyclic_notation: np.ndarray, distanceMatrix: np.ndarray) -> None:
        self._representation = deepcopy(cyclic_notation)

    def use_path_notation(self, path_notation: np.ndarray) -> None:
        self._build_cyclic_notation_from_path(path_notation)

    def _build_cyclic_notation_from_path(self, path_notation: np.ndarray) -> np.ndarray:

        cyclic_notation: np.ndarray = np.full(len(path_notation), -1)

        for city_posittion_in_path, city in enumerate(path_notation):
            cyclic_notation[path_notation[city_posittion_in_path-1]] = city

        if Debug:
            if -1 in cyclic_notation: raise CyclicNotationException("Error in building cyclic notation")

        self._representation = cyclic_notation
       
        return cyclic_notation
            

    def _calculate_distance(self, distanceMatrix: np.ndarray) -> float:
        total_distance = 0.0
        penalty = 1e6  # High penalty for unreachable paths

        for city in range(len(self._representation)):
            city_distance_matrix_index = self._representation[city]
            total_distance += distanceMatrix[city, city_distance_matrix_index] if distanceMatrix[city, city_distance_matrix_index] != float('inf') else penalty

        self._distance = total_distance
        return self._distance


    def get_cyclic_representation(self) -> np.ndarray:
        return deepcopy(self._representation)
    
    def get_distance(self, distance_matrix: np.ndarray) -> float:
        return self._distance if self._distance != -1 else self._calculate_distance(distance_matrix)
    

    def mutate(self) -> None:
        max_idx = self.size -1
        idx1 = random.randint(0, max_idx)
        idx2 = random.randint(0, max_idx)
        self._representation[idx2], self._representation[idx1] = self._representation[idx1], self._representation[idx2]