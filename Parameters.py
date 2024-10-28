from typing import Any, Dict
import yaml 

class Parameters:
    _parameters_dict: Dict[str, Any] = {}

    def __init__(self, filename) -> None:
        try:
            with open(filename, 'r') as file:
                self._parameters_dict = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
    
    def get_parameter(self, param_name: str, default: Any = None) -> Any:
        return self._parameters_dict.get(param_name, default)

    def get_population_size(self) -> int:
        return self._parameters_dict.get("population_size", 100)
    
    def get_offspring_size(self) -> int:
        return self._parameters_dict.get("offspring_size", 100)
    
    def get_offspring_per_recombination(self) -> int:
        return self._parameters_dict.get("offspring_per_recombination", 2)
    
    def get_k_selection(self) -> int:
        return self._parameters_dict.get("k_selection", 5)
    
    def get_k_elimination(self) -> int:
        return self._parameters_dict.get("k_elimination", 5)
