import numpy as np
from typing import Tuple
from Parameters import Parameters
from Population import Population
from Variation import Variation
from Selection import Selection
from Elimination import Elimination

class TravellingSalesMan():

    def __init__(self, matrix: np.ndarray, parameters: Parameters) -> None:
        self.matrix = matrix
        self.parameters = parameters

        self.selection = Selection(self.parameters.get_k_selection())
        self.variation = Variation(self.parameters.get_offspring_size())
        self.elimination = Elimination(self.parameters.get_offspring_size(), self.parameters.get_k_elimination())


    def run(self, population: Population) -> Tuple[float, float, np.ndarray]:
        
        mu = self.parameters.get_offspring_size()
        amt_children = self.parameters.get_offspring_per_recombination()
        # mu/amt_children should be int

        for _ in range(int(mu/amt_children)):
            parent1, parent2 = self.selection.select_pair(population)
            offspring = self.variation.produce_offspring(parent1, parent2)
            population.add_individuals(offspring, self.matrix)
        
        population = self.elimination.eliminate(population)

        objective_values = population.get_objective_values()

        best_index = np.argmin(objective_values)
        best_individual = population[best_index]
        best_objective = objective_values[best_index]

        return (
            float(np.mean(objective_values)),            
            best_objective,                       
            best_individual.get_cyclic_representation()
        )