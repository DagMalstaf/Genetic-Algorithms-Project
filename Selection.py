import EvolutionaryFunctions
from Individual import Individual
from Population import Population
from typing import List, Tuple


class Selection:
    def __init__(self, k: int) -> None:
        self.k = k

    def select(self, population: Population, num_pairs: int) -> List[Tuple[Individual, Individual]]:

        selected_pairs = []
        for _ in range(num_pairs):
            parent1 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
            parent2 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
            selected_pairs.append((parent1, parent2))
        return selected_pairs

