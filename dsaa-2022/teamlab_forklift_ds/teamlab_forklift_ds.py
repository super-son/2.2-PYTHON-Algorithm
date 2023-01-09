# 모듈 import 파트
from datetime import datetime
from collections import defaultdict
from optparse import Values

# Test를 위한 Mock Function 파트

# Class 파트
class Node :
    def __init__(self, data = None, next =None, prev = None) :  
        self.data = data 
        self.next = next
        self.prev = prev
        
class ForkliftNode():
    def __init__(self, forklift_name:str=None, location_x:float=None, location_y:float=None, iot_datetime:datetime=None, next:'ForkliftNode'=None) :  
        self.forklift_name = str(forklift_name)
        self.location_x = float(location_x)
        self.location_y = float(location_y)
        self.iot_datetime = datetime(iot_datetime)
        self.next = ForkliftNode(next)

    def __str__(self) :
        return_forklift_info = f"Forklift name : {self._forklift_name}\n" \
                    + f"x coordination : {self._location_x}\n" \
                    + f"y coordination : {self._location_y}\n" \
                    + f"Timestamp : {self._iot_datetime}" 

        return return_forklift_info

    @property
    def forklift_name(self):
        return self._forklift_name 
    @property
    def location_x(self):
        return self._location_x
    @property
    def location_y(self):
        return self._location_y
    @property
    def iot_datetime(self):
        return self._iot_datetime

    @forklift_name.setter 
    def forklift_name(self, value) :
        self._forklift_name = value
    @location_x.setter 
    def location_x(self, value) :
        self._location_x = value
    @location_y.setter 
    def location_y(self, value) :
        self._location_y = value
    @iot_datetime.setter 
    def iot_datetime(self, value) :
        self._iot_datetime = value


class LinkedListBag():
    def __init__(self, first_node : Node = None) -> None:
        self._head = first_node  
        self._tail = first_node 
        if first_node is not None:
            self._size = 1
        else:
            self._size = 0
        
    def append(self, new_node : Node) -> bool:
        try:
            if self._size == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
            return True

        except Exception as e:
            print(e)
            return False

    def insert(self, new_node : Node, index_number : int) -> bool:
        index_counter = 0
        cur_node = self._head
        try:
            if index_number == 0:          
                new_node.next = self._head
                self._head = new_node
                self._size += 1
                return True

            while cur_node is not None:
                if index_number == index_counter:
                    prev_node.next = new_node
                    new_node.next = cur_node
                    self._size += 1
                    return True
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next 
                    index_counter += 1
            return False
        except Exception as e:
            print(e)
            return False

    def remove(self, target_value : int) -> bool:
        cur_node = self._head
        prev_node = cur_node 
        try:
            while cur_node is not None:
                if cur_node.iot_datetime == target_value:
                    prev_node.next = cur_node.next
                    del(cur_node)
                    self._size -= 1
                    return True
                else:    
                    prev_node = cur_node 
                    cur_node = cur_node.next
            return False        
        except Exception as e:
            print(e)
            return False

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator():
    def __init__(self, head_node : Node) -> None:
        self._cur_node = head_node
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node

# 실행 함수 파트 

def load_dataset(filename : str):
    # filename = 'C:\\Users\\hj144\\workspace\\dsaa-2022\\teamlab_forklift_ds\\forklist_move.csv'
    dict_list = defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as h:
        for i in h.readlines()[1:]:
            id_v, fork_id, in_dt, emp_x, emp_y = i.rstrip('\n').split(',')
            dict_list[fork_id].append([emp_x, emp_y, in_dt])
    dataset = dict(dict_list)
    return dataset

def sort_dataset(dataset : dict):
    for key, value in dataset.items():
        value = sorted(value, key=lambda item:item[2])
        dataset[key] = value
    sorted_dataset = dataset
    return sorted_dataset


def build_linkedlistbag(sorted_dataset : dict):
    linkedlist_bag_dict = {}
    for k, values in sorted_dataset.items():
        linkedlist_bag_dict[k] = LinkedListBag()
        for v in values:
            linkedlist_bag_dict[k].append(ForkliftNode(k, v[0],v[1],v[2]))    
    return linkedlist_bag_dict

def reverse_linkedlist(dataset : dict):
    for key, value in dataset.items():
        value = sorted(value, key=lambda item:reversed(item[2]))
        dataset[key] = value
    sorted_dataset = dataset
    return sorted_dataset

def five_min_average_linkedlist(sorted_dataset : dict): # 해야해
    linkedlist_bag_dict = {}
    for k, values in sorted_dataset.items():
        linkedlist_bag_dict[k] = LinkedListBag()
        for v in values:
            linkedlist_bag_dict[k].append(ForkliftNode(k, v[0],v[1],v[2]))    
    return linkedlist_bag_dict

def odd_linkedlist(sorted_dataset : dict):
    linkedlist_bag_dict = {}
    counter=1
    for k, values in sorted_dataset.items():
        linkedlist_bag_dict[k] = LinkedListBag()
        for v in values:
            if counter%2 != 0:
                linkedlist_bag_dict[k].append(ForkliftNode(k, v[0],v[1],v[2]))    
            counter += 1
    return linkedlist_bag_dict

def main():
    DATASET_FILENAME = ""
    dataset = load_dataset("")

if __name__ == "__main__":
    main()
