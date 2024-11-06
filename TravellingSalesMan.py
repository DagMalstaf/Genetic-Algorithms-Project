import numpy as np
from typing import Tuple
from Parameters import Parameters
from Population import Population
from Variation import Variation
from Selection import Selection
from Elimination import Elimination

class TravellingSalesMan():

    def __init__(self, parameters: Parameters, distance_matrix: np.ndarray) -> None:
        self.parameters = parameters
        self.distanceMatrix = distance_matrix

        self.selection = Selection(self.parameters.get_k_selection())
        self.variation = Variation(self.parameters.get_offspring_size(), self.parameters.get_mutation_rate())
        self.elimination = Elimination(self.parameters.get_k_elimination(), distance_matrix)


    def run(self, distanceMatrix: np.ndarray, population: Population) -> Tuple[float, float, np.ndarray]:
        
        # mu/amt_children should be int

        while population.size < self.parameters.get_population_size() + self.parameters.get_offspring_size() :
            parent1, parent2 = self.selection.select_pair(distanceMatrix, population)
            offspring = self.variation.produce_offspring(parent1, parent2, distanceMatrix)
            population.add_individuals(offspring)
        
        population = self.elimination.eliminate(population)

        objective_values = population.get_objective_values(distanceMatrix)

        best_index = np.argmin(objective_values)
        best_individual = population[best_index]
        best_objective = objective_values[best_index]

        return (
            float(np.mean(objective_values)),            
            best_objective,                       
            best_individual.get_cyclic_representation()
        )
    

    