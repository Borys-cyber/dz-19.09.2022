class Queue_priority:
    __data = list()
    __priority = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def add(self, element: any, priority: int):
        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__priority.append(priority)
            self.__size += 1
        else:
            print('переполнение/overflow')

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

    def dequeue(self, element: any, ):
        lis = self.__data
        return lis.remove(element)

    def pop(self):
        if self.__size > 0:

            max_priority = max(self.__priority)

            index_max_priority = self.__priority.index(max_priority)

            popping = self.__data.pop(index_max_priority)

            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return popping
        else:
            print('пусто/empty')
            return None
    def peek(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            pick = self.__data[index_max_priority]
            return print(pick)

    def show_all(self):
        print(self.__data)


    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size

line = Queue_priority(int(input("Установите вместимость очереди!")))
print(line.get_capacity())
line.add((int(input("Установите элемент очереди!"))),(int(input("Установите приоритет элемента очереди!"))))
line.show_all()
line.add((int(input("Установите элемент очереди!"))), (int(input("Установите приоритет добавляемого элемента очереди!"))))
line.show_all()
line.pop()
line.show_all()
line.isEmpty()
line.isFull()
line.show_all()
line.add(1,2)
line.show_all()
line.peek()