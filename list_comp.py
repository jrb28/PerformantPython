# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from memory_profiler import profile as mem_profile
import random

@mem_profile
def list_comp(n):
    x =  [random.random() for i in range(n)]
    return x
    
if __name__ == '__main__':
    result = list_comp(1_000_000)