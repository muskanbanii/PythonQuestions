class Person:
    name = "Harry"
    occupation = "software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.info()
# print(a.name, a.networth)
