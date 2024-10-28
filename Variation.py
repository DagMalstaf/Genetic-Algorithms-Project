import numpy as np
from typing import Set
from Individual import Individual

class Variation():
    
    def __init__(self, offspring_size: int) -> None:
        self.offspring_size = offspring_size

    def produce_offspring(self, parent1: Individual, parent2: Individual) -> Set[Individual]:
        offspring_list = set()
        for _ in range(self.offspring_size):
            child = self.recombination(parent1, parent2)
            mutated_child = self.mutation(child)
            offspring_list.add(mutated_child)
        return offspring_list
    

    def recombination(self, parent1: Individual, parent2: Individual) -> Individual:
        parent1_repr = np.array(parent1.get_cyclic_representation())
        parent2_repr = np.array(parent2.get_cyclic_representation())
        length = len(parent1_repr)

        child_repr = np.full(length, None)

        common_positions = np.where(parent1_repr == parent2_repr)[0]
        child_repr[common_positions] = parent1_repr[common_positions]

        genes_in_child = set(child_repr[common_positions])

        remaining_genes = [gene for gene in parent1_repr if gene not in genes_in_child]

        idx = 0
        for i in range(length):
            if child_repr[i] is None:
                child_repr[i] = remaining_genes[idx]
                idx += 1

   

        child = Individual()
        child.use_cyclic_notation(child_repr)
        return child

    def mutation(self, individual: Individual) -> Individual:
        # TODO
        return individual
