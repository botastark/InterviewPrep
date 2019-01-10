#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 02:32:36 2019

@author: botaduisenbay
"""
#from fig import Fig
from DoublyLinkedBase import _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    
    def first(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        return self._header._next._element
    
    def last(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        else:
            return self._trailer._prev._element
    def delete_first(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.isempty():
            raise BaseException("Deque is empty")
        return self._delete_node(self._trailer._prev)
    
    def add_first(self,val):
        return self._insert_between(val, self._header, self._header._next)
    
    def add_last(self,val):
        return self._insert_between(val, self._trailer._prev, self._trailer)
