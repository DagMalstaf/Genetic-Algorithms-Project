import random
from tkinter import NO
from typing import List
from copy import deepcopy
import numpy as np
from Exceptions import CyclicNotationException, RepresentationException, InvalidCityInput, SubPathError
from Debug import DEBUG

class Individual():
    _representation : np.ndarray 
    _distance: float
    _NUMBER_OF_CITIES: int 

    _current_index: int
    _start_city: int
    def __init__(self, number_of_cities:int) -> None:
        self._representation :np.ndarray
        self._distance = -1.0
        self._NUMBER_OF_CITIES = number_of_cities
        self._current_index = 0
        self._start_city = 0

    def __repr__(self) -> str:
        return f"Individual(route={self._representation}, distance={self._distance})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            return NotImplemented
        #TODO: risky business!!! -> distance is not unique
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
    
    def __call__(self, start_city: int = 0):
        self._current_index = start_city
        self._start_city = start_city
        return self
    
    def __iter__(self):

        if self._start_city == -1:
            debug = True

        for counter in range(self._NUMBER_OF_CITIES):
            if DEBUG and counter != 0 and self._current_index == self._start_city:
                # if np.count_nonzero(self._representation == -1) != 1:
                #     debug = np.count_nonzero(self._representation == -1) != 1
                raise CyclicNotationException("This individual is not one cycle, we are back at the starting city before visiting all cities.")
            tmp = self._representation[self._current_index]
            yield tmp #city value can change during the iteration
            tmp = self._representation[self._current_index] # tmp is not guaranteed equal to self._representation[self._current_index] anymore
            # if tmp == 0 and np.count_nonzero(self._representation == -1) > 0:
            #     debug = True
            # if np.count_nonzero(self._representation == -1) == 1:
            #     debug = 0

            self._current_index = tmp

        if DEBUG and self._current_index != self._start_city:
                raise CyclicNotationException("This individual is not one cycle, after passing through the cycle we are not at the first city.")

        self._current_index = 0
        self._start_city = 0


    def iterator_set(self, city:int) -> None:
        if DEBUG and city < 0:
            raise InvalidCityInput(f"Cities cannot be represented by a negative number. \n\t input: {city}")
        # if city == 0 and np.count_nonzero(self._representation == -1) != 1:
        #     debug = True
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

        cyclic_notation: np.ndarray = np.full(self._NUMBER_OF_CITIES, -1, dtype=  np.int16)

        for index_path in np.arange(1, self._NUMBER_OF_CITIES + 1, dtype= np.int16):
            cyclic_notation[path_notation[index_path-1]] = path_notation[index_path % self._NUMBER_OF_CITIES]

        if DEBUG and -1 in cyclic_notation: raise CyclicNotationException("Error in building cyclic notation")

        self._representation = cyclic_notation
       
        return cyclic_notation
            

    def _calculate_distance(self, distanceMatrix: np.ndarray) -> float:
        total_distance = 0.0
        penalty = 1e6  # High penalty for unreachable paths

        for city in range(self._NUMBER_OF_CITIES):
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

    def mutate(self, positions_to_swap: int = 1) -> None:

        start_mutate_point, first_swap, second_swap = self._swap_two_elements()
        for _ in range(positions_to_swap - 1):
            start_mutate_point, first_swap, second_swap = self._swap_two_elements(start_mutate_point, first_swap, second_swap)
        


    def _swap_two_elements(self, 
                           start_mutate_point: np.int16 = np.int16(-1), 
                           first_swap: np.int16 = np.int16(-1),
                           second_swap: np.int16 = np.int16(-1) ) -> tuple[np.int16, np.int16, np.int16]:

        if start_mutate_point == -1:
            start_mutate_point = np.random.choice(self._representation)
            first_swap = self._representation[start_mutate_point]
            second_swap = self._representation[first_swap]

        final_mutate_point = self._representation[second_swap]

        self._representation[start_mutate_point] = second_swap
        self._representation[first_swap] = final_mutate_point
        self._representation[second_swap] = first_swap
        return second_swap, first_swap, final_mutate_point