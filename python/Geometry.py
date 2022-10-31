from distutils.command.config import config
import numpy as np
from config import Config
cf = Config()

class Atom():
    def __init__(self, str_element:str,x:float,y:float,z:float) -> None:
        self.element = cf.dict_element_num_to_str[str_element]
        self.x = x
        self.y = y
        self.z = z
    
class Geometry():
    def __init__(self, atom:Atom):
        pass










