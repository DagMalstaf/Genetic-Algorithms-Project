from Population import Population
from EvolutionaryFunctions import EvolutionaryFunctions


class Elimination():

    def __init__(self, pick_k: int) -> None:
        self.pick_k = pick_k

    def eliminate(self, population: Population) -> Population:

        while (population.get_current_population_size() != population.get_original_population_size()):
            individual = EvolutionaryFunctions.k_tournament(population, self.pick_k, max)
            population.remove_individual(individual)

        return population
        