#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:10:55 2019

@author: botaduisenbay
"""

class queue_arr:
    def __init__(self,s):
        self._data=s
        
    def isempty(self):
        return len(self._data)==0
    
    def dequeue(self):
        if self.isempty():
            raise BaseException("Queue is empty")
        else:
            
            return self._data.pop(0)

    def enqueue(self,val):
        self._data.append(val)
        
    def first(self):
        return self._data[0]
    
    def __len__(self):
        return len(self._data)