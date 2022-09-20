class Data_user:
    __data = dict()
    __values = list()
    __keys = list()
    __size = 0

    def __init__(self, size: int):
        if size >= 0:
            self.__size = size
            # "притянул за уши, т. к. не знал, что включать в инит"

    def add(self, key: any, value: any):
            self.__values.append(value)
            self.__keys.append(key)
            self.__data = dict(zip(self.__keys, self.__values))
            self.__size +=1
            return  self.__data

    def udalit(self, klych):
        self.klych = klych
        del self.__data[klych]
        return print(self.__data)


    def show_all(self):
        print(self.__data)

    def check(self, chek):
        self.chek = chek
        if chek in self.__data:
            print ("Found")
        else:
            print ("Not found")

    def change_name(self, oldname, newname):
        self.oldname = oldname
        self.newname = newname
        self.oldpassword = self.__data[self.oldname]
        del self.__data[oldname]
        self.__data[self.newname]=self.oldpassword
        return print (self.__data)

    def change_pass(self, namech, newpass):
        self.namech = namech
        self.newpass = newpass
        self.oldpass = self.__data[self.namech]
        del self.__data[self.namech]
        self.__data[self.namech] = self.newpass

    def get_size(self):
        return self.__size

a1 = Data_user(5)
a1.add(input("Установите имя пользователя"), input("Установите пароль"))
a1.add(input("Установите имя пользователя"), input("Установите пароль"))
a1.add(input("Установите имя пользователя"), input("Установите пароль"))
a1.show_all()
a1.udalit(input("Определите имя пользователя для удаления!"))
a1.check(input("Определите имя пользователя для поиска!"))
a1.change_name(input("Определите имя пользователя для замены!"), input("Установите новое имя пользователя"))
a1.show_all()
a1.change_pass(input("Определите имя пользователя для замены пароля!"), input("Установите новый пароль"))
a1.show_all()
