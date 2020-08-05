class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node()

    def append(self, node_data):
        node_data = Node(node_data)
        if self.head.data is None:
            self.head = node_data
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node_data
            current_node.next.previous = current_node

    def prepend(self, node_data):
        node_data = Node(node_data)
        node_data.next = self.head
        self.head.previous = node_data
        self.head = node_data

    def delete(self, node_data):
        current_node = self.head
        while current_node.data != node_data:
            previous_node = current_node
            current_node = current_node.next
        next_node = current_node.next
        previous_node.next = next_node
        next_node.previous = previous_node
        current_node.next = None
        current_node.previous = None

    def search(self, node_data):
        current_node = self.head
        while current_node.data != node_data:
            previous_node = current_node
            current_node = current_node.next
        next_node = current_node.next
        return previous_node, next_node


if __name__ == '__main__':
    l = DoublyLinkedList()
    for i in range(5):
        l.append(i)
    for i in range(3):
        l.prepend(i)
    l.delete(3)
    a = 0
