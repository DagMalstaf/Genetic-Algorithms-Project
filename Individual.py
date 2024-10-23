

from typing import List, Double
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

    def get_cyclic_representation(self) -> List[int]:
        return deepcopy(self._representation)
    
    def get_distance(self) -> Double:
        #TODO: layzy implementation
        return self._distance


    #Iterator along route

    

