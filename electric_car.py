class Car():
    def __init__(self, make, years, model):
        """初始化描述汽车的属性"""
        self.make = make
        self.years = years
        self.model = model
        self.odometer_reading = 0

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


class ElectricCar(Car):
    """电动汽车的奇特之处"""

    def __init__(self, make, years, model):
        """初始化父类的属性"""
        super().__init__(make, years, model)
        self.battery_size


my_tesla = ElectricCar("TESLA", 2020, "model's")
print(my_tesla.get_descriptive_name())
