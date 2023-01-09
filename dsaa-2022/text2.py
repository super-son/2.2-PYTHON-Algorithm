from numpy import array

a = 25
b = 25

print(a is b) #메모리공간의 비교, 파이썬에서는 메모리공간(id)을 잡고 변수명으로 접근한다. [정적메모리]-5 ~ +256은 같은 공간을 가르키기에 true가 나오지만
# 각각 257이라고하면 is에도 false가 나와야하는게 정상!
print(a == b) #값의 비교
print(id(a))
# a가 가르키는 공간을 b도 가르키는 거야!

a=[5,4,3,2,1] # 파이썬의 list / 파이썬에서 list는 공간추가시 .append 가능하나, c나 java는 array 범위보다 커지면 에러난다
b=[1,2,3,5,4] # 파이썬은 알아서 크기를 잡아주거든 : dynamic typing 특징.! 타이핑하는 시점에 공간을 잡아줌 / 대신 속도를 포기 int나 float는 2의 32승, 문자열은 하나당 2바이트 차지
b = a
print(a is b)
a.sort()
print(b) # a와 b가 같은 공간을 가르키기 때문에 같이 변한다

c=[2,3,4]
d=[2,3,4]
print(c is d) # 같다고 한적도 없음
print(c[0] is d[0]) # 각각의 원소들은 같은공간을 가르키고 있지
# list는 flexible하고 array에 고정된 공간, 대용량 데이터에 대해서는 array를 사용하는게 낫겠지. 공간을 계속 찾는 비용도 들고하니까, 대신 array는 공간낭비가 올수 있지

print(range(1,10,2))
for x in range(1,10,2):
    print(x)

sum = 0
for i in range(10):
    print(sum)
    sum += 1

two = 2
while two < 22 :
    two += 5
    print(two)

print('///////////////////////////////')

print(1 > 5 if True else False) # 이러한 문법도 가능 [삼항연산자] : 근데 좀 읽기가 어려움..
# sort는 return이 없는 함수이다!! // 함수의 종류에는 return이 내장된것과 아닌것들이 있다.
# 대신 sorted를 사용하면 return 가능
def a():
    return "hello"
b=a()
print(a(), b)

def c():
    print("hello")
d=c()
print(c(), d) # return이 아니므로 none인것처럼 sort도 마찬가지

t = [5,4,3,21]
v1 =t.sort()
v2 =sorted(t)
print(t, t.sort(), v1, v2) # ㅠㅠㅠ..

# complexity  알고리즘의 복잡도



