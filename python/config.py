import math

class Config(object):
    def __init__(self) -> None:
        self._PI = math.acos(0)*2.0
        self._dict_element_num_to_str = {
            'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8,
            'F':9, 'Ne':10, 'Na':11, 'Mg':12, 'Al':13, 'Si':14, 'P':15, 'S':16,
            'Cl':17, 'Ar':18, 'K':19, 'Ca':20
        }
        self.iter = 100
        
    def get_element_num(self):
        return self._dict_element_num_to_str
    def getPI(self):
        return self._PI