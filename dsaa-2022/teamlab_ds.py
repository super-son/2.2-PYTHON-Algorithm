from typing import Any # Any는 이렇게 임포트를 해주는게 졸다.

class Node :
    '''
    this is practice
    '''
    def __init__(self, data : Any = None, next :'Node'=None, prev = None)  ->  None : #자기 클래스라서 따옴표해줘야 인식가능함, 화살표는 return 값 0이라는 뜻
        # data는 any로 넣어주세요라는 주석에다가 None이라는 초기값
        '''
        Args:
            data = ~~
            next = ~~
        '''
        self._data = data #self._data 라고 코드바꾸면 정보를 숨길수있는 코드임
        self._next = None
        self._prev = prev

    @property
    def data(self):
        '''data'''
        return self._data 

    @property
    def prev(self):
        '''data'''
        return self._prev

    @property
    def next(self):
        '''next'''
        return self._next

    @data.setter # 들어오는 값들에 접근을 할 수 있도록 설정
    def data(self, value : Any) -> None:
        self._data = value

    @next.setter
    def next(self, node : 'Node') -> None:
        self._next = node

    def __str__(self) -> str: # 이거해주면 주피터 print(a) 했을때 주소말고 밑에것들 보여줘
        return_str = f"i have a data : {self._data}\n" \
                    + f"i have next node :  {id(self._next)}"
        return return_str

    def __repr__(self) -> str: # 이거해주면 주피터 a 했을때 밑에것들 보여준다
        return_str = f"i have a data : {self.data}  " \
                    + f"i have next node :  {id(self._next)} \n"
        return return_str     

    def __add__(self, other) -> None: # 노드끼리 더해보고싶다 a+b
        self._next = other

class LinkedListBag(object) : #object안써도 되는거 당연
    """
    ~~~
    """

    def __init__(self, first_node : Node = None) -> None:
        super().__init__()
        self._head = first_node
        self._tail = first_node

        if first_node is None: # 여기서 부터 count 함수는 진짜 에바네
            self._size = 0
        else:
            self._size = self._count()

    def _count(self) -> int:
        counter = 0
        cur_node = self._head
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        return counter

    def append(self, new_node : Node) -> bool :
        try:
            if self._size == 0:
                self._head = new_node
                self._tail = new_node
            else :
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
            return True

        except Exception as e:
            print(e)
            return False



    def __contains__(self, target : int):
        cur_node = self._head
        while cur_node is not None: # cur node라는 것도 같이 만들어서 같이 노드를 돌면서 특정 값을 찾는 역할
            if cur_node.data == target:
                return True
            cur_node = cur_node.next
        else:
            return False

    def __len__(self):
        return self._size

    def __repr__(self) -> str: # 보여지는 것을 다르게
        cur_node = self._head
        if self._size == 0:
            return None
            
        return_str = ""
        while cur_node is not None:
            return_str += f"{cur_node.data} -> "
            cur_node = cur_node.next
        return_str += f"End of Linked List"
        return return_str

    def insert(self, new_node : Node, index_number : int) -> bool:
        index_counter = 0
        cur_node = self._head

        if index_number == 0:          # 0번째에 insert 안되는것을 막아주기
            new_node.next = self._head
            self._head = new_node
            self._size += 1
            return True

        while cur_node is not None:
            if index_number == index_counter:
                #우리는 값을 찾았다!!
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next # 얘는 계속 전진
                index_counter += 1
        return False

    def remove(self, target_value : int) -> bool:
        cur_node = self._head

        while cur_node is not None:
            if cur_node.data == target_value: 
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next # 얘는 계속 전진
        return False

    def __iter__(self): # iterable 순환하는 함수를 만들거야. 리스트에 for i in list 하는것도 iterable한거임.
        return _BagIterator(self._head)

    @property
    def head(self) -> Node :
        return self._head
    
class _BagIterator(): # def __ iter 하면서 같이 만들어준것
    def __init__(self, head_node) -> None:
        self._cur_node = head_node

    def __iter__(self):
        return self
        
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node

class DoublyLinkedListBag:
    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new_node : 'Node'):
        if self.head is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def insert(self):
        pass

    def remove(self, target_data):
        if self.size ==0:
            raise ValueError("nono")

        cur_node = self.head
        if target_data == self.head.data:
            self.head = self.head.next
            self.head.prev = None
            return 
        if target_data == self.tail.data:
            self.tail = self.head.prev
            self.tail.next = None
            return
        while cur_node.prev is not None:
            if target_data == cur_node.data:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
                cur_node = None
                break
            else :
                    cur_node = cur_node.next 
        else:        
            raise ValueError("nono")
     
    def peak(self):
        return self.tail

    def __repr__(self) :
        pass