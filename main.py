class Vehicle:
    __colors=["red","blue","green","white","black"]
    def __init__(self,owner,model,ep,color):
        self.owner=owner
        self.__model = model
        self.__ep = ep
        self.__color= color
    def get_model(self):
        return f"Модель: {self.__model}"
    def get_ep(self):
        return f"Мошьность двигателя: {self.__ep}"
    def get_color(self):
        return f"Цвет {self.__color}"
    def print_info(self):
        print(self.get_model())
        print(self.get_ep())
        print(self.get_color())
        print(f"Владелец:{self.owner}")
    def set_color(self,new_color):
        if new_color.lower() in self.__colors:
            self.__color=new_color
        else:
            print(f"нельзя помнеять цвет на {new_color}")
class Sedan(Vehicle):
    __limit=5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, "white")


vehicle1.print_info()


vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()