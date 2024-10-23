

from typing import List, Double, Int
from copy import deepcopy


class Individual():


    _representation : List[int] = list()
    _distance: Double = 0

    def __init__(self) -> None:
        pass

    
    def __repr__(self) -> str:
        pass

    def __eq__(self, value: object) -> bool:
        pass

    def __gt__(self, value: object) -> bool:
        pass

    def use_cyclic_notation(self, cyclic_notation: List[Int]) -> None:
        pass

    def use_path_notation(self, cyclic_notation: List[Int]) -> None:
        pass

    def get_cyclic_representation(self) -> List[int]:
        return deepcopy(self._representation)
    
    def get_distance(self) -> Double:
        #TODO: layzy implementation
        return self._distance


    #Iterator along route

    #'Iterator' builder 

    

