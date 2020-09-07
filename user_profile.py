def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name + " rolled over!")


my_dog = Dog('zzzzz', 6)
# print("my dog's name is " + my_dog.name.title() + '.')
# print("my dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


class Car():
    def __init__(self, make, years, model):
        """初始化描述汽车的属性"""
        self.make = make
        self.years = years
        self.model = model
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.years) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('这个车跑了' + str(self.odometer_reading) + 'km!')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表增加指定的值"""
        self.odometer_reading += miles


my_new_car = Car('audi', 2016, 'a8')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(120)
my_new_car.read_odometer()
my_used_car = Car('subaru', 2013, 'outback')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(20000)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# class Car():
#     - - snip- -
# my_new_car = Car()
