import random
import teamlab_ds as ds  # 모듈로서 쓰겠다는 거!
# import importlib     #주피터환경에서는 애들 까지 필요
# importlib.reload(ds)
a=ds.Node(2)
b=ds.Node(52)
c=ds.Node(18)

a.next = b
b.next = c
# b = None
# c = None
 
print(a.__doc__) # a에 담긴 주석문서정보를 긁어온다
print(a.__dict__) # a에 담긴 정보들을 dict형태로 긁어온다
print(a)
print(a.next.data)
q = a.data + b.data
print(q) # q = a + b를 하면 b의 값인 52가 나와야하는데 ㅋ

print("1111/////////////////////////////////////")

node_list = []
for _ in range(10000):
    node_list.append(ds.Node(random.randint(1,10000)))   # travers의 과정(데이터 - 데이터 연결해나가는)이라고 보면 된다
for idx in range(1, len(node_list)):
    node_list[idx-1] + node_list[idx]
print(node_list[:3])
print(node_list[0].next.next.data) # 이렇게 하면 노드들끼리연결되어 3번째 리스트값이 출력되어야함.

print("//////2222///////////////////////////////")

node_list = []
for _ in range(5):
    node_list.append(ds.Node(random.randint(1,10000)))   # travers의 과정(데이터 - 데이터 연결해나가는)이라고 보면 된다
for idx in range(1, len(node_list)):
    node_list[idx-1] + node_list[idx]

my_bag = ds.LinkedListBag(node_list[0])
print(node_list)
print(999 in my_bag)
print(len(my_bag))
print(my_bag)

new_node = ds.Node(777)
my_bag.insert(new_node, 3) # 3번째 자리에 777이 들어가게 됨
print(my_bag)

my_bag.remove(777)
print(my_bag)
# print("/////////////////////////////////////")
# # iterable 정의 했기때문에 my bag에서 for문도 돌릴 수 있게되었다!
# for my_node in my_bag:
#     print(my_node)

# print("################################################")
# a1=ds.Node(10)
# b1=ds.Node(20)
# c1=ds.Node(30)

# a1._next = b1
# b1._next = c1
# c1._prev = b1
# b1._prev = a1

# head_node = a1
# tail_node = c1
# cur_node = head_node # 이걸 tail로 바꾸고 밑에 next들을 prev로 바꾸면 역travers 함수지
# while cur_node._next is not None:
#     print(cur_node.data)
#     cur_node = cur_node._next
# print(cur_node.data)

# mybbag = ds.DoublyLinkedListBag() # 실패
# a2=ds.Node(10)
# b2=ds.Node(20)
# c2=ds.Node(30)
# a2._next = b2
# b2._next = c2
# c2._prev = b2
# b2._prev = a2

# head_node = a2
# tail_node = c2
# mybbag.append(a2)
# mybbag.append(b2)
# mybbag.append(c2)
# cur_node = a2
# while cur_node.next is not None:
#     print(cur_node)
#     cur_node = cur_node.next
# print(cur_node)
# print(mybbag.peak())