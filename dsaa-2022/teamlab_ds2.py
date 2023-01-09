from collections import deque
from platform import node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) :
        return str(self.data)

class Stack():
    def __init__(self, first_node : Node = None):
        self.size = 0
        self.top = None

        if first_node is not None:
            self.top = first_node
            self.size += 1
        else:
            self.top = None
            self.size = 0

    def __repr__(self):
        cur_node = self.top
        out = ""
        while cur_node is not None:
            out += str(cur_node.data) + "-->"
            cur_node = cur_node.next 
        return out

    def push(self, new_node : Node): # 데이터 추가
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self): # 데이터 나가
        if self.is_empty():
            raise Exception(" 다 나감")
        return_value = self.top
        self.top = self.top.next # top자리를 넘겨주고
        self.size -= 1

    def is_empty(self):
        return True if self.size ==0 else False

    def get_size(self) :
        return self.size

    def peek(self):
        return self.top

class Queue():
    def __init__(self, node = None):
        self.size = 0
        if node is not None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head = None
            self.tail = None

    def enqueue(self, new_node): # 데이터의 추가
        if self.size == 0 : 
            self.head = new_node
            self.tail = new_node
        else : 
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
 

    def rotate(self):
        if self.size == 0:
            return
        count = 1
        cur_node = self.head
        while(count < self.size and cur_node is not None):
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return

        last_node = cur_node
        while (cur_node.next is not None):
            cur_node = cur_node.next

        cur_node.next = self.head
        self.head = last_node
        last_node.next = None

    def dequeue(self):
        if self.head is not None:
            data = self.head
            self.head = self.head.next 
        else :
            raise Exception("error")
        return data

    def __repr__(self):
        cur_node = self.head
        out = ""
        while cur_node is not None:
            out += str(cur_node.data) + "-->"
            cur_node = cur_node.next

        return out

