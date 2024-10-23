

from typing import List, Func, Int, Bool
from Individual import Individual
from Population import Population


class EvolutionaryFunctions():

   @staticmethod
   def k_tournament(population: Population, k: int, selection_function: Func[List[Individual], Individual]) -> Individual:
      pass

    
   @staticmethod
   def non_duplicants_check(path :List[Int], number_of_cities: Int = -1) -> Bool:
      number_of_cities = number_of_cities if number_of_cities != -1 else len(path) 

      sum_of_all_numbers = number_of_cities*(number_of_cities + 1) / 2
      sum_of_all_entries_in_path = sum(path)
      return sum_of_all_entries_in_path == sum_of_all_numbers
