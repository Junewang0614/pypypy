class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def discribe_restaurant(self):
        print('the restaurant name is ' + self.restaurant_name.upper())
        print('the type of it is ' + self.cuisine_type.lower())

    def open_restaurant(self):
        print('the restaurant is open.')
#创建子类
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['caomei','ciangcao','qiaokeli','xiangyu','huamigua']

    def read_flavors(self):
        for flavor in self.flavors:
            print(flavor)

the_icerestaurant = IceCreamStand('duangduang','bing')
#调用父类方法
the_icerestaurant.discribe_restaurant()
#调用子类方法
the_icerestaurant.read_flavors()


