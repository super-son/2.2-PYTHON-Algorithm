import teamlab_ds2 as ds2
from collections import deque
stack_ex = []
stack_ex.append(" 1 ")
stack_ex.append(" 2 ")
stack_ex.append(" 3 ") # append가 push 한거임
stack_ex.pop()
print(stack_ex)


my_stack = ds2.Stack()
my_node = ds2.Node(10)
my_stack.push(my_node)
my_node = ds2.Node(20)
my_stack.push(my_node)
my_node = ds2.Node(30)
my_stack.push(my_node)
my_node = ds2.Node(40)
my_stack.push(my_node)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())

print("//////////////////////////")

ex_list = deque([50,30,20,10]) # deque 라는 패키지를 import 할 수 도 있었지
ex_list.append(100)
print(ex_list.popleft()) # 이렇게 deque구조를 활용해 쉽게 앞에있는것도 없앨 수 있다
ex_list.rotate()
print(ex_list) # top에 있는애를 맨 앞으로 

my_queue = ds2.Queue()
my_queue.enqueue(ds2.Node(10))
my_queue.enqueue(ds2.Node(20))
my_queue.enqueue(ds2.Node(30))
print(my_queue)
my_queue.rotate()
print(my_queue)

print("//////////////////////////")
print(eval("5+10")) # 문자열끼리도 숫자처럼 더해줌 

def postfix_calculator(postfix_exp : list):
    postfix_stack = []
    for element in elelement_list:
        if element.isdigit():
            postfix_stack.append(element) 
        else:
            val_2 = int(postfix_stack.pop())
            val_1 = int(postfix_stack.pop())
            result = eval(f"{val_1} {element} {val_2}") # eval 개사기
            
            postfix_stack.append(result)
        print(postfix_stack)
    return postfix_stack[0]

post_fix_data = "5 3 + 8 2 - *"
elelement_list = post_fix_data.split()
postfix_calculator(elelement_list)

print("//////////////////////////")
output_list = []
pregress_stack = []
def infix_to_postfix(expression): #input expression
    
    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
    PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 

    stack = [] # initially stack empty
    output = '' # initially output empty


    for ch in expression:
        if ch not in OPERATORS:  
            output+= ch
        elif ch=='(': 
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]: # 이 부분 중요
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()

    return output
exp = " 5 * 3 + 12 / (4+ 3 +7)"
exp_list = exp.split()
print(infix_to_postfix(exp_list))

