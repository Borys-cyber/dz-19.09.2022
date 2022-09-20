class Queue:
    __data = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def isEmpty(self):
        if self.__data is None:
            print("empty")
        else:
            print("Not empty")
    def isFull(self):
        if self.__size is self.__capacity:
            print("Full")
        else:
            print("Not full")

    def enqueue(self, element: any):
        if self.__size < self.__capacity and element  is "@" or element is '!' or element is '#' or element is '$' or element is '%' :
            self.__data.append(element)
            self.__size += 1
        else:
            print('переполнение/неправильный символ')

    def dequeue(self, element: any, ):
        lis = self.__data
        return lis.remove(element)
        # else:
        #     return None

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size

    def show_all(self):
        print(self.__data)


line = Queue(3)
print(line.get_capacity())
line.enqueue(input("введите символ"))
print(line.show_all())
line.enqueue(input("введите символ"))
print(line.show_all())
line.enqueue(input("введите символ"))
print(line.show_all())
line.dequeue(input("введите символ для удаления"))
print(line.show_all())
line.enqueue(input("введите символ"))
print(line.show_all())
line.isEmpty()
line.enqueue(input("введите символ"))
print(line.show_all())
line.enqueue(input("введите символ"))
print(line.show_all())
