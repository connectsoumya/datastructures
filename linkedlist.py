class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def insert(self, node_data):
        if self.head.data is None:
            self.head = node_data
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node_data

    def delete(self, node_data):
        current_node = self.head
        while current_node.data != node_data:
            previous_node = current_node
            current_node = current_node.next
        next_node = current_node.next
        previous_node.next = next_node
        current_node.next = None



if __name__ == '__main__':
    l = LinkedList()
    for i in range(5):
        node_data = Node(i)
        l.insert(node_data)
    l.delete(3)
    a = 0
