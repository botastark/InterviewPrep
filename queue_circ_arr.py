#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:00:57 2019

@author: botaduisenbay
"""

class queue_circ_arr:
    
    DEFAULT_CAPACITY = 3
    
    def __init__(self):
        self._data= [None]* queue_circ_arr.DEFAULT_CAPACITY 
        #create empty array w/ size of def_cap
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size==0
    
    def first(self):
        if self.isempty():
            raise BaseException("Queue is empty")
        else:
            return self._data[self._front]
        
    def dequeue(self):
        if self.isempty():
            raise BaseException("Queue is empty")
        else:
            ans=self._data[self._front]
            self._data[self._front]=None
            self._front = (self._front + 1) % len(self._data)
            self._size = self._size- 1
            return ans

    def enqueue(self,val):
        if self._size==len(self._data):#which is def capacit
            self._resize(2*len(self._data)) #double size of exitsing array
        avail = (self._front + self._size) % len(self._data) #available cell index of an array in circular configuration 
        self._data[avail] = val
        self._size += 1
    
    def _resize(self, capacity):
        old = self._data
        self._data = [None]*capacity
        walk = self._front # we'll rewrite array starting frm front cell (first to dequeue)
        for k in range(self._size): # only consider existing elements
            self. data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
            self. front = 0
        
        
        
        

    
