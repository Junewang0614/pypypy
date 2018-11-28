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

the_restaurant = Restaurant('zhongcanting','zhong')
print(the_restaurant.restaurant_name)
print(the_restaurant.cuisine_type)
the_restaurant.discribe_restaurant()
the_restaurant.open_restaurant()

