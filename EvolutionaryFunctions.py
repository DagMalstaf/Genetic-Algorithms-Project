

from random import sample
from typing import List, Callable
from Individual import Individual
from Population import Population


class EvolutionaryFunctions():

   @staticmethod
   def k_tournament(population: Population, k: int, selection_function: Callable[[List[Individual]], Individual]) -> Individual:
        """
        Get k random individuals from the population, then select one according to a selection_fuction.
        examples selection_function: min(), max()
        """
        if k > population.get_size():
            raise Exception()
        sampled_individuals = sample(population.get(), k)
        individual = selection_function(sampled_individuals, key=lambda ind: ind.get_distance())
        return individual

    
    