import numpy as np
from basis import GTO, CGF
from config import Config
from geometry import Atom, Vec
from overlap import compute_gto_overlap, compute_overlap
cfg = Config()

def compute_gto_kinetics(gto1: GTO, gto2: GTO):
    '''
    This function computes kinetics energy integral.
    To compute kinetics, we need computing method to calculate overlap integral
    Ref : P29, Nakai
    '''


