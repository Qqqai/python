class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        print(self.name)
        print(self.__age)

    def __str__(self):
        return self.name + str(self.__age)

    def __del__(self):
        return self.__str__()

p = Person("zhangsan", 18)
print(p.name)
print(p.__del__())