class Product(object):
    pass
class Inventory(object):
    def __init__(self) :
        self.__items = [] # __를 추가함으로써 private 변수 선언. 외부에서 타객체가 접근 할 수 없음 
        self.test = 'abc'
    
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")
    
    def get_number_of_items(self):
        return len(self.__items)

    @property  ## decorator라고하는데, 접근할수있도록 해줌 = 숨겨진 변수를 반환하게 해줌 = 안에 있는 정보를 외부로 빼줌
    def items(self):
        return self.__items

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.items.append("abcde")
my_inventory.items.append("efew")
print(my_inventory.items)  # 외부에서 마음대로 추가가 안되게 막아놓은거지


# class Product(object):
#     pass
# class Inventory(object):
#     def __init__(self) :
#         self.items = []
#         self.test ="abc"

#     def add_new_item(self, product):
#         if type(product) == Product:
#             self.items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid Item")
    
#     def get_number_of_items(self):
#         return len(self.items)
    
# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# my_inventory.items.append("abcde")
# my_inventory.items.append("efew")
# print(my_inventory.items) # 이렇게 외부에서도 마음대로 추가가된다는것.