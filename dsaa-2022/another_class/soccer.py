class SoccerPlayer(object): 
    # 객체를 만들때 정의해주는 역할을 하지
    def __init__(self, name : str, position : str, back_number : int): # 타입힌트를 주는것
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self): # abc를 프린트하면 주소값만 나오다가 이거하니 string을 출력해주네
        return "Hello My name is %s. I am %s , %d" %(self.name, self.position, self.back_number)
        # __str__ 같은 형식들은 정해진 함수이름이다!

    def __add__(self, other):
        return self.name + other.name

    def change_back_number(self, new_number): # 이렇게 self를 넣어주는것은 필수다
        print("선수의 등번호를 변경합니다 : From %d to %d" % \
            (self.back_number, new_number))
        self.back_number = new_number

abc = SoccerPlayer('son','FW', 7) # abc는 객체, soocerplayer은 클래스
ddd = SoccerPlayer('park','WF',13)

print(abc)
print(abc + ddd) # __add__를 부르는거임
ddd.change_back_number(4)
print("나는이제 %d번이지롱" %ddd.back_number)
print("/////////////////////////////")

class superson(SoccerPlayer): #상속받을 객체를 넣어준다.
    def __init__(self, name: str, position: str, back_number: int, check_date):
        super().__init__(name, position, back_number)
        self.check_date = check_date

    def do_work(self):
        print("아들로서 열심히 공부")
        super().change_back_number(9)

q=superson("super_son",3,3,78)
print(q.name, q.position)
print(q.do_work())