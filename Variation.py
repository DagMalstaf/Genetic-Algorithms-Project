import numpy as np
from typing import Set
from Individual import Individual
from Debug import DEBUG


class Variation():
    _offspring_size: int = 0
    _mutation_rate: float = 0.0
    
    def __init__(self, offspring_size: int, mutation_rate: float) -> None:
        if DEBUG:
            assert 0 <= mutation_rate <= 1

        self._offspring_size = offspring_size
        self._mutation_rate = mutation_rate

    def produce_offspring(self, parent1: Individual, parent2: Individual, distanceMatrix: np.ndarray) -> Set[Individual]:
        offspring_list = set()
        for _ in range(self._offspring_size):
            child = self._recombination(parent1, parent2, distanceMatrix)
            mutated_child = self._mutation(child)
            offspring_list.add(mutated_child)
        return offspring_list
    

    def _recombination(self, parent1: Individual, parent2: Individual, distanceMatrix: np.ndarray,
                        p_inherent_common_path: float = 1, 
                        p_inherent_common_city_in_common_location: float = 0.6,
                        p_inherent_difference_city_in_common_location: float = 0.6                       
                        ) -> Individual:
        parent1_cyclic_representation = parent1.get_cyclic_representation()
        parent2_cyclic_representation = parent2.get_cyclic_representation()
        number_of_cities = len(parent1_cyclic_representation) #change to call to parent1

        base_case_no_city = np.full(number_of_cities,-1)
        child_cyclic_representation = np.where(parent1_cyclic_representation == parent2_cyclic_representation, parent1_cyclic_representation, base_case_no_city)
        child = Individual(parent1.get_number_of_cities())
        child.use_cyclic_notation(child_cyclic_representation)
        all_cities = np.arange(number_of_cities)
        cities_left_to_allocate = np.where(~np.isin(all_cities,child_cyclic_representation), all_cities, base_case_no_city )
            

        p_choice = np.random.random_sample()
        in_common_subpath = False
        for city_parent1, city_parent2, city_child in zip(parent1, parent2, child):
            if city_child != -1:
                if p_choice > p_inherent_common_path:
                    child.iterator_set(self._get_city( city_parent1, city_parent2, cities_left_to_allocate,
                                 p_inherent_common_city_in_common_location,
                                 p_inherent_difference_city_in_common_location))
                else: 
                    in_common_subpath = True
                    continue
            if in_common_subpath:
                in_common_subpath = False
                p_choice = np.random.random_sample()
            child.iterator_set(self._get_city( city_parent1, city_parent2, cities_left_to_allocate,
                                 p_inherent_common_city_in_common_location,
                                 p_inherent_difference_city_in_common_location))
        if DEBUG:
            assert((cities_left_to_allocate == -1).all())
        return child

    def _mutation(self, individual: Individual) -> Individual:
        if np.random.random_sample() > self._mutation_rate:
            individual.mutate()      
        return individual


    def _get_city(self, city_parent1: int, city_parent2: int, cities_left_to_allocate: np.ndarray, 
                  p_inherent_common_city_in_common_location: float,
                  p_inherent_difference_city_in_common_location: float
                  ):
        p_choice = np.random.random_sample()
        if DEBUG:
            assert((cities_left_to_allocate == -1).any())
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
                return self._select_choosen_city(self._get_random_city(cities_left_to_allocate), cities_left_to_allocate)
        #just random sample
        else:
            return self._select_choosen_city(self._get_random_city(cities_left_to_allocate), cities_left_to_allocate)
    def _get_random_city(self, cities_left_to_allocate: np.ndarray) -> int:
        return np.random.choice(cities_left_to_allocate[cities_left_to_allocate != -1])
    
    def _select_choosen_city(self, city: int, cities_left_to_allocate: np.ndarray) -> int:
        cities_left_to_allocate[city] = -1
        return city