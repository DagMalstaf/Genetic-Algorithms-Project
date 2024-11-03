import random
from tkinter import NO
from typing import List
from copy import deepcopy
import numpy as np
from Exceptions import CyclicNotationException, RepresentationException, InvalidCityInput
from Debug import DEBUG

class Individual():
    _representation : np.ndarray 
    _distance: float = -1
    _NUMBER_OF_CITIES: int = -1

    _current_index = 0
    _counter: int = 0
    def __init__(self, number_of_cities:int) -> None:
        self._representation = np.empty(0)
        self._distance = 0.0
        self._NUMBER_OF_CITIES = number_of_cities

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
        for counter in range(self._NUMBER_OF_CITIES):
            if DEBUG and counter != 0 and self._current_index == 0:
                raise CyclicNotationException("This individual is not one cycle, we are back at the starting city before visiting all cities.")
            tmp = self._representation[self._current_index]
            yield tmp #city value can change during the iteration
            self._current_index = self._representation[self._current_index] # tmp is not guaranteed equal to self._representation[self._current_index] anymore
        if DEBUG and self._current_index !=0:
                raise CyclicNotationException("This individual is not one cycle, after passing through the cycle we are not at the first city.")

    def iterator_set(self, city:int) -> None:
        if DEBUG and city < 0:
            raise InvalidCityInput(f"Cities cannot be represented by a negative number. \n\t input: {city}")
        self._representation[self._current_index] = city

    def use_cyclic_notation(self, cyclic_notation: np.ndarray) -> None:
        if (cyclic_notation.size != self._NUMBER_OF_CITIES): 
            raise RepresentationException(f"The representaion has the wrong size.\n\t NUMBER_OF_CITIES: {self._NUMBER_OF_CITIES}\n\t length representation: {len(cyclic_notation)}")
        self._representation = deepcopy(cyclic_notation)

    def use_path_notation(self, path_notation: np.ndarray) -> None:
        if (path_notation.size != self._NUMBER_OF_CITIES): 
            raise RepresentationException(f"The representaion has the wrong size.\n\t NUMBER_OF_CITIES: {self._NUMBER_OF_CITIES}\n\t length representation: {len(path_notation)}")
        self._build_cyclic_notation_from_path(path_notation)

    def _build_cyclic_notation_from_path(self, path_notation: np.ndarray) -> np.ndarray:

        cyclic_notation: np.ndarray = np.full(len(path_notation), -1)

        for city_posittion_in_path, city in enumerate(path_notation):
            cyclic_notation[path_notation[city_posittion_in_path-1]] = city

        if DEBUG:
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
    
    def get_number_of_cities(self)-> int:
        return self._NUMBER_OF_CITIES

    def mutate(self) -> None:
        max_idx = self.size -1
        idx1 = random.randint(0, max_idx)
        idx2 = random.randint(0, max_idx)
        self._representation[idx2], self._representation[idx1] = self._representation[idx1], self._representation[idx2]