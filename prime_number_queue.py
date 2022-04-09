from linked_list2 import LinkedList
from prime_and_anagram import anagram


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        return self.list.insert_at_beg(data)

    def dequeue(self):
        return self.list.remove_last()

    def display(self):
        return self.list.display()


if __name__ == "__main__":
    queue = Queue()
    num1 = 1
    num2 = 1000
    list_ = anagram(num1, num2)
    for val in list_:
        queue.enqueue(val)
    queue.display()