import numpy as np

def search(arr, x):  
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def sentinel(lst, target):
    size = len(lst)
    lst.append(target)
    i = 0
    while(lst[i]!= target):
        i += 1
    if(i == size):
        return None
    else:
        return i

def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)


class Node() :
    def __init__(self,value) :
        self.value = value
        self.next = None
class Linked_List() :
    def __init__(self) :
        self.head = None

    def insert(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = Node(value)
    def search(self, value):
        temp = self.head
        while temp : 
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def print_LL(self):
        temp  =self.head
        if not temp : 
            print(None)
        while temp :
            if temp.next:
                print(temp.value,"-->",end=" ")
            else:
                print(temp.value)
            temp = temp.next

    # 이 자리에 linked list 구현된 코드 삽입
class Hash_table() :
    def __init__(self,size) :
        self.size = size
        self.hashtable = [None]*self.size
        for x in range(self.size) :
            self.hashtable[x] = Linked_List()
        
    def hash(self,key) :
        # Hash function is h(x) = x%10
        return key%10
    
    def insert_key(self,key) :
        index = self.hash(key)
        self.hashtable[index].insert(key)
        
    def search_key(self,key) :
        index = self.hash(key)
        boolean = self.hashtable[index].search(key)
        return boolean
    
    def print_HT(self) :
        print("Hash table is :- \n")
        print("Index \t\tValues\n")
        for x in range(self.size) :
            print(x,end="\t\t")
            self.hashtable[x].print_LL()

import random
# print(search([2,3,4,5,6],5))
# print(sentinel([2,3,4,5,6],5))
# print(binary_search_recursive([2,3,4,5,6],5,0,5))
HT = Hash_table(10)
for i in range(10):
    ran = random.randint(0,100)
    HT.insert_key(ran)
HT.print_HT()
