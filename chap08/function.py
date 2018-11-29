#添加一个人的基本信息
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first;
    profile['last_name'] = last;
    for key,value in user_info.items():
        profile[key] = value
    return profile

def cars_info(name,year,**others):
    car = {}
    car['name'] = name
    car['year'] = year
    for key,value in others.items():
        car[key] = value
    return car



    
