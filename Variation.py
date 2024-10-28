import numpy as np
from typing import Set
from Individual import Individual

class Variation():
    
    def __init__(self, offspring_size: int, distanceMatrix: np.ndarray) -> None:
        self.offspring_size = offspring_size
        self.distanceMatrix = distanceMatrix

    def produce_offspring(self, parent1: Individual, parent2: Individual) -> Set[Individual]:
        offspring_list = set()
        for _ in range(self.offspring_size):
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
        # TODO
        return individual
