#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 01:55:27 2019

@author: botaduisenbay
"""
class _DoublyLinkedBase:
    __slot__='_element','_prev','_next'
    
    class _Node:
        def __init__(self, element,prev,next):
            self._element=element
            self._prev=prev
            self._next=next
            
    def __init__(self):
        self._header=self._Node(None, None, None)
        self._trailer=self._Node(None, None, None)
        self._header._next=self._trailer
        self._trailer._prev=self._header
        self._size=0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size==0
    
    def _insert_between(self, e, predecessor, successor):
        new=self._Node(e,predecessor, successor)
        predecessor._next=new
        successor._prev=new
        self. size += 1
        return new
    def _delete_node(self, node):
        predecessor=node._prev
        successor=node._next
        predecessor._next=node._next
        successor._prev=predecessor
        self._size =self._size - 1
        element = node._element
        node. prev = node. next = node. element = None
        return element
    
        
    
        
