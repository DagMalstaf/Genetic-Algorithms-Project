

from typing import List
from copy import deepcopy


class Individual():


    _representation : List[int] = list()
    _distance: float = 0

    def __init__(self) -> None:
        pass

    
    def __repr__(self) -> str:
        pass

    def __eq__(self, value: object) -> bool:
        pass

    def __gt__(self, value: object) -> bool:
        pass

    def use_cyclic_notation(self, cyclic_notation: List[int]) -> None:
        pass

    def use_path_notation(self, cyclic_notation: List[int]) -> None:
        pass

    def get_cyclic_representation(self) -> List[int]:
        return deepcopy(self._representation)
    
    def get_distance(self) -> float:
        #TODO: layzy implementation
        return self._distance


    #Iterator along route

    #'Iterator' builder 

    

