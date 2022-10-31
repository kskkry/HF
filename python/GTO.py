import numpy as np

class GTO(object):
    def __init__(self, alpha, coeff) -> None:
        self.alpha = alpha
        self.coeff = coeff

class CGF(object):
    def __init__(self, GTO_list:list) -> None:
        self.size = len(GTO_list)
        self.GTO_list = GTO_list
        pass



