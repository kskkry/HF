import numpy as np

dict_element_num_to_str = {
    'H':1,
    'He':2,
    'Li':3,
    'Be':4,
    'B':5,
    'C':6,
    'N':7,
    'O':8,
    'F':9,
    'Ne':10,
    'Na':11,
    'Mg':12,
    'Al':13,
    'Si':14,
    'P':15,
    'S':16,
    'Cl':17,
    'Ar':18
}

class Atom():
    def __init__(self, str_element:str,x:float,y:float,z:float) -> None:
        self.element = dict_element_num_to_str[str_element]
        self.x = x
        self.y = y
        self.z = z
    
class Geometry():
    def __init__(self, atom:Atom):
        pass










