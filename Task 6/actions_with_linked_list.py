from Iterator import *


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        result = "["
        current = self.head
        if current:
            result += str(current.data)
            current = current.next
            while current:
                result += ", " + str(current.data)
                current = current.next
        result += "]"
        return result

    def generate_elements(self, size, a, b):
        our_gen_lst = generator(a, b, size)
        node = Node(next(our_gen_lst))
        self.head = node
        for el in our_gen_lst:
            self.append(el)

    def iterate_elements(self, size, a, b, pos):
        our_it_lst = Iterator(size, a, b)
        for el in our_it_lst:
            self.insert(el, pos)
            break

    def find_index(self, index):
        if index < 0:
            index += self.__len__()
        elif index > (self.__len__() - 1):
            raise IndexError('There no such index in LinkedList')
        position = index
        i, current = 0, self.head
        while current is not None:
            if i == position:
                return current
            current = current.next
            i += 1

    def __getitem__(self, index):
        return self.find_index(index).data

    def __setitem__(self, index, item):
        self.find_index(index).data = item

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, item, position):
        if position == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        i = 0
        while i < position - 1 and n is not None:
            n = n.next
            i += 1
        if n is None:
            raise IndexError('There no such index in LinkedList')
        else:
            new_node = Node(item)
            new_node.next = n.next
            n.next = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def delete_element(self, position):
        if self.is_empty():
            raise IndexError('Empty LinkedList')
        current = self.head
        if position == 0:
            self.head = current.next
            current = None
            return
        for i in range(position - 1):
            current = current.next
            if current is None:
                break
        if position > (self.__len__() - 1):
            raise IndexError('There no such index in LinkedList')
        next = current.next.next
        current.next = None
        current.next = next

    def delete_from_to(self, index1, index2):
        if index2 > self.__len__() or index1 > index2:
            raise ValueError('Index2 not present in the LinkedList and index2 mast be bigger than index1.')
        for i in range(index2 - index1 + 1):
            self.delete_element(index1)

    def pop(self):
        current = self.head
        if current is None:
            raise IndexError('Empty LinkedList')
        if current.next is None:
            self.clear()
            return
        while current.next:
            if current.next.next is None:
                current.next = None
            else:
                current = current.next

    def clear(self):
        current = self.head
        if current is None:
            raise IndexError('Empty LinkedList')
        while current:
            self.head = current.next
            current = self.head

    def minimum(self, size):
        min_multiplication = float('inf')
        for i in range(size - 1):
            if int(self[i] * self[i + 1]) < min_multiplication:
                min_multiplication = self[i] * self[i + 1]
        return min_multiplication

    def print(self):
        text = "{"
        current = self.head
        while current:
            if text != "{":
                text += ", "
            text += str(current.data)
            current = current.next
        text += "}"
        print(text)
