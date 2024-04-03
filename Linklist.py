# __repr__: hàm trong class (viết tắt: real eval print loop)
class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head 
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self): # hàm này định nghĩa cách ( hình thức) giá trị chuỗi được in ra khi sử dụng hàm print
        return f'Myvalue is : {self.data}'
    
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
llist = Linkedlist()
llist.head = first_node
print(llist)
print(first_node)
