# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from memory_profiler import profile as mem_profile
import random

@mem_profile
def for_loop(n):
    x = []

    for i in range(n):
        x.append(random.random())
        
    return x
    
if __name__ == '__main__':
    result = for_loop(1_000_000)