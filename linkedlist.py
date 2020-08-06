class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
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

    def prepend(self, node_data):
        node_data = Node(node_data)
        node_data.next = self.head
        self.head = node_data

    def delete(self, node_data):
        current_node = self.head
        while current_node.data != node_data:
            previous_node = current_node
            current_node = current_node.next
        next_node = current_node.next
        previous_node.next = next_node
        current_node.next = None

    def search(self, node_data):
        current_node = self.head
        while current_node.data != node_data:
            current_node = current_node.next
        next_node = current_node.next
        return next_node



if __name__ == '__main__':
    l = LinkedList()
    for i in range(5):
        l.append(i)
    for i in range(2):
        l.prepend(i)
    l.delete(3)
    a = 0
