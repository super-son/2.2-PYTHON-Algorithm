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

def is_validate_dom(dom_text) :
    checking_stack = []
    
    checking_dataset = ['<','>','/',' ','|n','</']
    counter = 0
    data = list(dom_text.strip())
    
    while counter < len(data):
        checking_text = data[counter]

        if checking_text == checking_dataset[0]:
            checking_text_list = []

            while checking_text != checking_dataset[1]:
                checking_text_list.append(checking_text)
                counter += 1
                checking_text = data[counter]
            checking_text_list.append(checking_text)
            checking_text2 = ''.join(checking_text_list)

            if 'item name=' in checking_text2:
                checking_text2 = '<item>'
            if checking_stack != [] and checking_dataset[2] in checking_text2 :
                if checking_stack[-1].replace(checking_dataset[0],checking_dataset[5]) == checking_text2:
                    checking_stack.pop()
                    counter -= 1
                else:
                    return False
            else:
                checking_stack.append(checking_text2)
        if checking_text in [checking_dataset[3], checking_dataset[4]]:
            counter += 1
            checking_text = data[counter]
            continue
        counter += 1     
    if checking_stack != []:
        return False
    if '<' not in dom_text:
            return False

    return True