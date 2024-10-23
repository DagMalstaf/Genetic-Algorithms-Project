from typing import Any, Dict


class Parameters():

    _parameters_dict: Dict[str,Any] = dict()

    def __init__(self) -> None:
        pass


    def read_yaml(self, filename: str) -> None:
        pass

    #gettters for parameters

    def get_population_size(self) -> int:
        # TODO
        return 100
    
    def get_offspring_size(self) -> int:
        # TODO
        return 100
    
    def get_offspring_per_recombination(self) -> int:
        # TODO
        return 2
    
    def get_k_selection(self) -> int:
        # TODO
        return 5
    
    def get_k_elimination(self) -> int:
        # TODO
        return 5

    
    
