import numpy as np

dict_element_num_to_str = {
    'H':1,
    'He':2,
    'Li':3,
    'Be':4
}

class Atom():
    def __init__(self, str_element:str,x:float,y:float,z:float) -> None:
        self.element = dict_element_num_to_str(str_element)
        self.x = x
        self.y = y
        self.z = z
    
class Geometry():
    def __init__(self, atom:Atom):










