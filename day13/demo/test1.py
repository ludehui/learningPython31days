'''
# 定义一个销售北京现代车的店类
class CarStore(object):
    def order(self, typeName):
        # 根据客户的不同要求，生成不同的类型的车
        if typeName == "伊兰特":
            car = YilanteCar()
        elif typeName == "索纳塔":
            car = SuonataCar()
        return car
'''

# 定义伊兰特车类
class YilanteCar(object):
    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义索纳塔车类
class SuonataCar(object):
        # 定义车的方法

    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义途胜车类
class TuSheng(object):
        # 定义车的方法

    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


'''
因为考虑到还有其它的车型，如果考虑到上面CarStore类，需要修改方法

'''


# 用来生成具体的对象,这是使用方法实现，一般使用类实现(工厂类)
def createCar(typeName):
    car  = None
    if typeName == "伊兰特":
        car = YilanteCar()
    elif typeName == "索纳塔":
        car = SuonataCar()
    elif typeName == "途胜":
        car = TuSheng()
    return car


# 定义一个销售北京现代车的店类
class CarStore(object):
    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        car = createCar(typeName)
        return car


cs = CarStore()
snt = cs.order('索纳塔')
if snt!=None:
    snt.move()
