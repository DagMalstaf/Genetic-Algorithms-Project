import numpy as np
from typing import Set
from Individual import Individual
from Debug import Debug
import random

class Variation():
    _offspring_size: int = 0
    _mutation_rate: float = 0.0
    
    def __init__(self, offspring_size: int, mutation_rate: float) -> None:
        if Debug:
            assert 0 <= mutation_rate <= 1

        self._offspring_size = offspring_size
        self._mutation_rate = mutation_rate

    def produce_offspring(self, parent1: Individual, parent2: Individual) -> Set[Individual]:
        offspring_list = set()
        for _ in range(self._offspring_size):
            child = self.recombination(parent1, parent2)
            mutated_child = self.mutation(child)
            offspring_list.add(mutated_child)
        return offspring_list
    

    def recombination(self, parent1: Individual, parent2: Individual) -> Individual:
        parent1_cyclic_representation = parent1.get_cyclic_representation()
        parent2_cyclic_representation = parent2.get_cyclic_representation()
        length = len(parent1_cyclic_representation) #change to call to parent1

        child_cyclic_representation = np.where(parent1_cyclic_representation == parent2_cyclic_representation, parent1_cyclic_representation, np.full(length,-1))
        child = Individual()
        child.use_cyclic_notation(child_cyclic_representation)

        for city_parent1, city_parent2, city_child in zip(parent1, parent2, child):
            if city_child != -1: continue
        return Individual()
        #TODO: recombination

    def mutation(self, individual: Individual) -> Individual:
        if random.random() > self._mutation_rate:
            individual.mutate()      
        return individual
