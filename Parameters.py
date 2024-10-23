

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

    
    
