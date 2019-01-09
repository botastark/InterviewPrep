#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 07:31:19 2019

@author: botaduisenbay
"""

class stack_arr:
    def __init__(self,s):
        self._data=s
        self._top=len(s)-1
    def isempty(self):
        return len(self._data)==0
    
    def getSize(self):
        return len(self._data)
    def pop(self):

        if self.isempty():
            raise BaseException("Stack is empty")
        else:   
            return self._data.pop()
    

    def push(self,val):
        self._top+=1
        self._data.append(val)
        
