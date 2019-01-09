#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:34:08 2019

@author: botaduisenbay
"""
    
class LinkedStack:
    
    class _Node:
        
        __slots__ = '_element','_next' # streamline memory usage
        
        def __init__(self, element, next): # initialize node’s fields
            self._element = element # reference to user’s element
            self._next = next

    def __init__(self):
        self._head = None # reference to the head node
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size==0
        
    def push(self, val):

        self._head=self._Node(val,self._head)
        self._size+=1
        
    def top(self):
        if self.is_empty():
            raise BaseException("Stack is empty")
        return self._head._element
        
    def pop(self):
        if self.is_empty():
            raise BaseException("Stack is empty")
        ans=self._head._element
        self._head._element=None
        self._head=self._head._next
        self._size-=1
        return ans
    
        
    
        