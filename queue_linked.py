#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:27:47 2019

@author: botaduisenbay
"""

class LinkedQueue:

    class _Node:

        __slots__ = '_element','_next' # streamline memory usage

        def __init__(self, element, next): # initialize node’s fields
            self._element = element # reference to user’s element
            self._next = next

    def __init__(self):
        self._head = None # reference to the head node
        self._size = 0
        self._tail = None
        
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):

        return self._size
    
    def first(self):
        if self.is_empty():
            raise BaseException("Queue is empty")
        return self._head._element
        
    def enqueue(self,val):
        new=self._Node(val, None)
        if self.is_empty():
            self._head=new
        else:
            self._tail._next=new
        self._tail=new
        self._size+=1
        
    def dequeue(self):
        if self.is_empty():
            raise BaseException("Queue is empty")
        ans=self._head._element
        temp=self._head._next
        self._head=temp
        if self.is_empty():
            self._tail=None
        self._size-=1
        return ans
        
