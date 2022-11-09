import math

class Config(object):
    def __init__(self) -> None:
        self._PI = math.acos(0)*2.0
        self._dict_element_str2num = {
            'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8,
            'F':9, 'Ne':10, 'Na':11, 'Mg':12, 'Al':13, 'Si':14, 'P':15, 'S':16,
            'Cl':17, 'Ar':18, 'K':19, 'Ca':20
        }
        self._dict_element_num2str = {
            1:'H', 2:'He', 3:'Li', 4:'Be', 5:'B', 6:'C', 7:'N', 8:'O',
            9:'F', 10:'Ne', 11:'Na', 12:'Mg', 13:'Al', 14:'Si', 15:'P', 16:'S',
            17:'Cl', 18:'Ar', 19:'K', 20:'Ca'
        }
        self.iter = 100
        
    def get_element_num(self):
        return self._dict_element_str2num
    
    def get_element_str(self):
        return self._dict_element_num2str
    
    def getPI(self):
        return self._PI