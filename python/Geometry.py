from distutils.command.config import config
import numpy as np
from config import Config
cfg = Config()

class Vec(object):
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getz(self):
        return self.z


class Atom(Vec):
    def __init__(self,str_element,x,y,z) -> None:
        super().__init__(x,y,z)
        self.element = cfg.get_element_num()[str_element]
        #print(self.element,self.x,self.y,self.z)

    
class Geometry(object):
    def __init__(self, atom_list:list):
        pass










