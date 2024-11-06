import numpy as np
from typing import Callable, List, Set
from Individual import Individual
from Debug import DEBUG
from itertools import zip_longest


class Variation():
    _offspring_size: int = 0
    _mutation_rate: float = 0.0
    
    def __init__(self, offspring_size: int, mutation_rate: float) -> None:
        if DEBUG:
            assert 0 <= mutation_rate <= 1

        self._offspring_size = offspring_size
        self._mutation_rate = mutation_rate

    def produce_offspring(self, parent1: Individual, parent2: Individual, distanceMatrix: np.ndarray) -> List[Individual]:
        offspring_list = list()
        if parent1 == parent2:
            return list()
        for _ in range(self._offspring_size):
            child = self._recombination(parent1, parent2, distanceMatrix)
            mutated_child = self._mutation(child)
            offspring_list.append(mutated_child)
        return offspring_list
    
    def _find_first_non_zero(self,array: np.ndarray, comparison_operator: Callable[[int], bool]) -> int:

        for index, value in np.ndenumerate(array):
            if comparison_operator(value): return index[0]
        return -1

    def _recombination(self, parent1: Individual, parent2: Individual, distanceMatrix: np.ndarray,
                        p_inherent_common_path: float = 1, 
                        p_inherent_common_city_in_common_location: float = 0.6,
                        p_inherent_difference_city_in_common_location: float = 0.6                       
                        ) -> Individual:
        parent1_cyclic_representation = parent1.get_cyclic_representation()
        parent2_cyclic_representation = parent2.get_cyclic_representation()
        number_of_cities = parent1.get_number_of_cities()

        base_case_no_city = np.full(number_of_cities,-1)
        child_cyclic_representation = np.where(parent1_cyclic_representation == parent2_cyclic_representation, parent1_cyclic_representation, base_case_no_city)
        child = Individual(number_of_cities)
        child.use_cyclic_notation(child_cyclic_representation)
        #start from 1 as the the beginning city should only be allocated last (additional constrain on beginning city)
        all_cities = np.arange(number_of_cities)
        cities_left_to_allocate = np.where(~np.isin(all_cities,child_cyclic_representation), all_cities, base_case_no_city )

        #check for -1 when parents are identical match
        start_city = self._find_first_non_zero(cities_left_to_allocate, lambda x: x != -1)
        if start_city == -1:
            debug = True
            if parent1 == parent2:
                debug2 = True
        cities_left_to_allocate[start_city] = -1 

        self._build_hamiltonian_cycle_exposed(start_city, child, parent1, parent2, cities_left_to_allocate,
                                                p_inherent_common_path,
                                                p_inherent_common_city_in_common_location,
                                                p_inherent_difference_city_in_common_location)
        if DEBUG:
            assert((cities_left_to_allocate == -1).all())
        return child

    def _mutation(self, individual: Individual) -> Individual:
        if np.random.random_sample() > self._mutation_rate:
            individual.mutate()      
        return individual


    def _get_city(self, start_city: int, child: Individual, city_parent1: int, city_parent2: int, cities_left_to_allocate: np.ndarray, 
                  p_inherent_common_city_in_common_location: float,
                  p_inherent_difference_city_in_common_location: float
                  ):
        # last city goes back to the start
        if (cities_left_to_allocate == -1).all():
            # if (np.count_nonzero(child.get_cyclic_representation() == -1) != 1):
            #     debug = True
            return start_city
        
        p_choice = np.random.random_sample()
        #same city on same place in both parents
        if p_choice <= p_inherent_common_city_in_common_location \
            and city_parent1 == city_parent2:
            can_allocate_city_parent = city_parent1 in cities_left_to_allocate
            if can_allocate_city_parent : 
                return self._select_choosen_city(city_parent1, cities_left_to_allocate)
            else:
                return self._get_random_city(cities_left_to_allocate)
        #different city in both parents, but still select from parents
        elif p_choice <= p_inherent_difference_city_in_common_location \
            and city_parent1 != city_parent2:
            can_allocate_city_parent1 = city_parent1 in cities_left_to_allocate
            can_allocate_city_parent2 = city_parent2 in cities_left_to_allocate
            if can_allocate_city_parent1 and can_allocate_city_parent2:
                p_choice_between_parents = np.random.random_sample()
                if p_choice_between_parents <= 0.5:
                    return self._select_choosen_city(city_parent1, cities_left_to_allocate)
                else:
                    return self._select_choosen_city(city_parent2, cities_left_to_allocate)
            elif can_allocate_city_parent1:
                return self._select_choosen_city(city_parent1, cities_left_to_allocate)
            elif can_allocate_city_parent2:
                return self._select_choosen_city(city_parent2, cities_left_to_allocate)
            else:
                return self._get_random_city(cities_left_to_allocate)
        #just random sample
        else:
            return self._get_random_city(cities_left_to_allocate)
    
    def _get_random_city(self, cities_left_to_allocate: np.ndarray) -> int:
        debug = cities_left_to_allocate[cities_left_to_allocate != -1]
        city = np.random.choice(cities_left_to_allocate[cities_left_to_allocate != -1])
        return self._select_choosen_city(city,cities_left_to_allocate)
    
    def _select_choosen_city(self, city: int, cities_left_to_allocate: np.ndarray) -> int:
        cities_left_to_allocate[city] = -1
        if city == 0:
            debug = True
        return city
    
    def _build_hamiltonian_cycle_exposed(self,start_city: int, child: Individual, parent1: Individual, parent2: Individual, cities_left_to_allocate: np.ndarray,
                                         p_inherent_common_path: float,
                                         p_inherent_common_city_in_common_location: float,
                                         p_inherent_difference_city_in_common_location: float
                                         ) -> None:
        
        p_choice = np.random.random_sample()

        for city_parent1, city_parent2, city_child in zip_longest(parent1(start_city), parent2(start_city), child(start_city)):
            if city_child != -1:
                if p_choice > p_inherent_common_path:
                    cities_left_to_allocate[city_child] = city_child
                    child.iterator_set(self._get_city(start_city, child, city_parent1, city_parent2, cities_left_to_allocate,
                                 p_inherent_common_city_in_common_location,
                                 p_inherent_difference_city_in_common_location))
                else: 
                    continue
            p_choice = np.random.random_sample()
            child.iterator_set(self._get_city(start_city, child, city_parent1, city_parent2, cities_left_to_allocate,
                                 p_inherent_common_city_in_common_location,
                                 p_inherent_difference_city_in_common_location))




