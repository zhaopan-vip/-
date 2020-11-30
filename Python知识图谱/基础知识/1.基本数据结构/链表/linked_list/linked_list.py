#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/25 3:27 PM
"""

from node import ListNode


class LinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p, count = self.head, 0
        while p:
            if count == index:
                return p.val
            p = p.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = self.head
        self.head = ListNode(val)
        self.head.next = tmp

        if not self.tail:
            self.tail = self.head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.tail:
            self.tail = self.head = ListNode(val)
            return

        self.tail.next = ListNode(val)
        self.tail = self.tail.next

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev, p, count = None, self.head, 0
        while p:
            if count == index:
                # insert at position here
                break
            prev = p
            p = p.next
            count += 1

        if count == 0:
            self.addAtHead(val)
            return

        if count == self.size:
            self.addAtTail(val)
            return

        if count > self.size:
            return

        assert prev is not None
        prev.next = ListNode(val)
        prev.next.next = p

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.size == 0:
            return
        if index < 0 or index >= self.size:
            return
        prev, p, count = None, self.head, 0
        while p:
            if count == index:
                # delete at here
                break
            prev = p
            p = p.next
            count += 1

        if count == 0:
            # remove head
            if self.tail == self.head:
                self.tail = self.head = None
            else:
                tmp = self.head.next
                self.head.next = None
                self.head = tmp
        elif count == self.size - 1:
            # remove tail
            prev.next = None
            self.tail = prev
        else:
            # remove middle
            prev.next = p.next

        self.size -= 1


if __name__ == '__main__':
    obj = LinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)
