# python类
# pass为占位，先搭建类架构，再用具体的函数替换pass完善类
class  Animals:
    pass
class Mammals(Animals):
    pass
class Cats(Mammals):
    pass
# 类里定义函数，语法规定第一个参数必须是self
# __int__函数，在新对象实例化会自动运行，给新对象赋初始值
class Animals:
    def breathe(self):
        print("breathing")
    def move(self):
        print("moving")
    def eat(self):
        print("eating fooda")
class Mammals(Animals):
    def breasfeed(self):
        print("feeding young") 
class Cats(Mammals):
    def __init__(self,spots):
        self.spots = spots
        self.catch_mouse()
        self.breathe()
    def catch_mouse(self):
        print("catch mouse")
# 调用属性-类名.属性名
# 调用方法-类名.方法名()
kitty = Cats(10)
print(kitty.spots)
kitty.catch_mouse()
kitty.move()
kitty.breasfeed()
# 类中调用本类或者父类方法-self.方法()
# 类中调用本类或者父类属性-self.属性名