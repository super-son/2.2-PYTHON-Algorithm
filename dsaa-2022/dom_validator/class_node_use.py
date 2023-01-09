class Node():
    def __init__(self, data = None, next :'Node'=None, prev = None) :  
        self.data = data 
        self.next = None
        self.prev = prev

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

    def push(self, new_node : Node): 
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception(" 다 나감")
        return_value = self.top
        self.top = self.top.next
        self.size -= 1

    def is_empty(self):
        return True if self.size ==0 else False

    def get_size(self) :
        return self.size

    def peek(self):
        return self.top


def is_validate_dom(dom_text : str) -> bool:

    checking_stack = Stack()
    for i in dom_text.split('<'):
        if i.startswith('/') and '>' in i:
            tag = i[1:].split('>')[0].split(' ')[0]  
            if tag != checking_stack.peek().data:
                    return False
            else : checking_stack.pop()  
            # print(f'태그종료 = {tag}')
        elif '>' in i:
            tag = i.split('>')[0].split(' ')[0]
            checking_stack.push(Node(tag))
            # print(f'태그시작 = {tag}')

    if checking_stack.is_empty() :
        return True 
    else :
        return False