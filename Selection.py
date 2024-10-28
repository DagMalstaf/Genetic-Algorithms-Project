from EvolutionaryFunctions import EvolutionaryFunctions
from Individual import Individual
from Population import Population
from typing import List, Tuple


class Selection:
    def __init__(self, k: int) -> None:
        self.k = k
        self.selection_function = min

    def select_amt(self, population: Population, num_pairs: int) -> List[Tuple[Individual, Individual]]:

        selected_pairs = []
        for _ in range(num_pairs):
            parent1 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
            parent2 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
            selected_pairs.append((parent1, parent2))
        return selected_pairs
    
    def select_pair(self, population: Population) -> Tuple[Individual, Individual]:
        parent1 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
        parent2 = EvolutionaryFunctions.k_tournament(population, self.k, self.selection_function)
        return parent1, parent2

