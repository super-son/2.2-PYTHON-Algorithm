# 파이썬의 함수는 일급함수이다. 변수나 데이터구조에 할당이 가능한 객체, 파라메터 혹은 리턴값으로 사용함
def square(x):
    return x*x
def cube(x):
    return x*x*x
def formula(method, argument_list):
    return [method(value) for value in argument_list] # 함수를 파라메터로 사용

f = square
print(f(5))
print(formula(cube, [1,2,3]))

def print_msg(msg):
    def printer():
        print(msg)
    printer() # 함수내에 또다른 함수가 존재 : inner function
print_msg("hello, python")

def print_msg(msg): # 위와 같은 뜻 // inner fuction을 return값으로 반환 : closures 클로져라고 함
    def printer():
        print(msg)
    return printer
another = print_msg("hello, python")
another()
print("////////////////////////////////////////////////")

def star(func):
    def inner(*args, **kwargs): # printer로 사용한 인자모두 데려온다.
        print(args[1]*30)
        func(*args, **kwargs) # printer 함수를 실행시켰다
        print(args[1]*30)
    return inner

@star
def printer(msg,mark):
    print(msg)
printer("Hello", " &")

print("////////////////////////////////////////////////")

def stars(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args, **kwargs)
        print(""*30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%"*30)
        func(*args, **kwargs)
        print("%"*30)
    return inner

@stars
@percent
def printer(msg):
    print(msg)
printer("Hello")