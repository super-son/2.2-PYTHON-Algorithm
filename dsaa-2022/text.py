a= [5,10,200,300]
b= [10,200,300]

print(a[2] is b[1]) # true
print(a[3] is b[2]) # false . 256 넘었잖아.

a=[1,2,3,4,5]
b=[1,2,3,4,5]
# a is b는 false 이지만 a=b 해주면 true 된다. 같은 곳을 가르키게되어서!
a=b
a.reverse()
print(b) #b도 변하게된다

# len 함수 안쓰는법
q1 = [1,2,3,4,5]
counter = 0
for i in q1 :
    counter += 1
print(counter)