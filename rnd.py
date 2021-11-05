# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:24:06 2021

@author: james
"""

from memory_profiler import profile as mem_profile
import numpy as np

@mem_profile
def make_rnd(n):
    rnd = np.random.random(n).astype(np.float32)
    del rnd
    
if __name__ == '__main__':
    make_rnd(1_000_000)