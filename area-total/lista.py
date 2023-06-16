from node import Node


class Lista:
    def __int__(self):
        self.head: None | Node = None
        self.tail: None | Node = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            self.tail = new_node
            current.next = self.tail

    def area_total(self):
        pass
