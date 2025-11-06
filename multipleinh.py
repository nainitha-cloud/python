class Cars:
    def speak(self):
        print("Has automated and manual cars")

class Mustang(Cars):
    def black(self):
        print("Mustang has its own charm")

class Mcooper(Cars):
    def s(self):
       print("Mcooper is unique design and it's manufactured by BMW")

mustang = Mustang()
mcooper = Mcooper()

mustang.black()
mcooper.s()
