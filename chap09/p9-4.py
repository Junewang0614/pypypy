class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def discribe_restaurant(self):
        print('the restaurant name is ' + self.restaurant_name.upper())
        print('the type of it is ' + self.cuisine_type.lower())


    def open_restaurant(self):
        print('the restaurant is open.')

    def set_number_served(self,set_number = 0):
        set_number = input()
        self.set_number = set_number
        print(self.set_number)

    def increment_number_served(self,number):
        self.set_number = int(self.set_number) + number 
    
    def read_number(self):
        print(self.set_number)


#修改属性值
the_restaurant = Restaurant('zhongcanting','zhong')
the_restaurant.number_served = 500
print(the_restaurant.number_served)

#输入实参
the_restaurant.set_number_served()

#参数递增
the_restaurant.increment_number_served(100)
the_restaurant.read_number()

#报错总结
#1.input()输入类型是字符串，需要int（）转化为数值
#2.在类中可操作的变量皆为self.name
#3.搞清个个变量之间的关系
