#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.len = 0
        
    def _loop(self , index):
        node = self.head
        p = 0
        while p < index + 1:
            node = node.next
            p += 1
        
        return node
        
    def get(self, index: int) -> int:
        if self.len <= index or index < 0:
            return -1
        node = self._loop(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if self.len < index:
            return -1

        if index < 0:
            index = 0
        
        self.len += 1

        node = self.head
        for _ in range(index):
            node = node.next
    
        new_node = Node(val)
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        
        if self.len <= index or index < 0:
            return -1
        
        self.len -= 1

        node = self.head
        for _ in range(index):
            node = node.next
        
        node.next.prev = node
        node.next = node.next.next
        
        
        
        