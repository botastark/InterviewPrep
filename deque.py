#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:44:29 2019

@author: botaduisenbay

Double-Ended Queue Deque
D.add_first(e): Add element e to the front of deque D.
D.add_last(e): Add element e to the back of deque D.
D.delete_first( ): Remove and return the first element from deque D;
an error occurs if the deque is empty.
D.delete_last( ): Remove and return the last element from deque D;
an error occurs if the deque is empty.
Additionally, the deque ADT will include the following accessors:
D.first(): Return (but do not remove) the first element of deque D;
an error occurs if the deque is empty.
D.last(): Return (but do not remove) the last element of deque D;
an error occurs if the deque is empty.
D.is_empty( ): Return True if deque D does not contain any elements.
len(D): Return the number of elements in deque D; in Python,
we implement this with the special method len .


"""
class Deque:
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data= [None]* Deque.DEFAULT_CAPACITY 
        #create empty array w/ size of def_cap
        self._size = 0
        self._front = 0
        self._back=0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size==0
    
    def first(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        else:
            return self._data[self._front]
        
    def last(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        else:
            return self._data[self._back]
        
    def delete_first(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        else:
            ans=self._data[self._front]
            self._data[self._front]=None
            self._front = (self._front + 1) % len(self._data)
            self._size = self._size- 1
            return ans
        
    def delete_last(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        else:
            ans=self._data[self._back]
            self._data[self._back]=None
            self._back=(self._back-1)%len(self._data)
            self._size = self._size- 1
            return ans

    def add_first(self,val):
        if self._size==len(self._data):#which is def capacit
            self._resize(2*len(self._data)) #double size of exitsing array
        avail = (self._front-1) % len(self._data) #available cell index of an array in circular configuration 
        self._front=avail
        self._data[avail] = val
        self._size += 1
        
    def add_last(self,val):
        if self._size==len(self._data):#which is def capacit
            self._resize(2*len(self._data)) #double size of exitsing array
        avail = (self._front + self._size) % len(self._data) #available cell index of an array in circular configuration 
        self._back=avail
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
        
        
        
        

    
