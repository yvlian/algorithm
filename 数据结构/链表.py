class Node():
    def __init__(self,value,next_node):
        self.value = value
        self.next_node = next_node

class LinkList():
    def __init__(self,head):
        self.head = head

    def locate(self,i):
        node = self.head
        j = 0
        while j < i:
            node = node.next_node
            j += 1
        return node

    def insert(self,node,i):
        if i == 0:
            node.next_node = self.head
            self.head = node
            return
        link_node = self.locate(i-1)
        tmp = link_node.next_node
        link_node.next_node = node
        node.next_node = tmp

    def insert_head(self,node):
        self.insert(node,0)

    def delete(self,i):
        if i == 0:
            self.head = self.head.next_node
            return
        link_node = self.locate(i-1)
        if link_node.next_node is None:
            print('超过链表长度')
            return
        link_node.next_node = link_node.next_node.next_node

    def delete_head(self):
        self.delete(0)

h1 = Node(1,None)
h2 = Node(2,None)
h3 = Node(3,None)
h4 = Node(4,None)

link_list = LinkList(h1)
link_list.insert(h2,1)
link_list.insert(h3,0)
link_list.insert(h4,1)
link_list.delete(0)
link_list.delete(1)
a = 1