from Population import Population
from EvolutionaryFunctions import EvolutionaryFunctions


class Elimination():

    def __init__(self, offspring_size: int, pick_k: int) -> None:
        self.offspring_size = offspring_size
        self.pick_k = pick_k

    def eliminate(self, population: Population) -> Population:
 
        for _ in range(self.offspring_size):
            individual = EvolutionaryFunctions.k_tournament(population, self.pick_k, min)
            population.remove_individual(individual)

        return population
        