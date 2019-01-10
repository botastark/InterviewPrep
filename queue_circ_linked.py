#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:55:59 2019

@author: botaduisenbay
"""

class CircularQueue:
    class _Node:

        __slots__ = '_element','_next' # streamline memory usage

        def __init__(self, element, next): # initialize node’s fields
            self._element = element # reference to user’s element
            self._next = next

    def __init__(self):
        self._tail = None # reference to the tail node
        self._size = 0
        
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def first(self):
        if self.is_empty:
            raise BaseException("Queue is empty")
        head=self._tail._element
        return head._element
    
    def enqueue(self,val):
        new=self._Node(val, None)
        if self.is_empty:
            new._next=new #circularity . point to itself
        else:
            new._next=self._tail._next
            self._tail._next=new
        self._tail=new
        self._size+=1
        
    def dequeue(self):
        if self.is_empty:
            raise BaseException("Queue is empty")

        oldhead=self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next=oldhead._next
        self._size-=1
        return oldhead._element
        
    def rotate(self):
        # ”””Rotate front element to the back of the queue.”””
        if self. size > 0:
            self. tail = self. tail. next # old head becomes new tail
        