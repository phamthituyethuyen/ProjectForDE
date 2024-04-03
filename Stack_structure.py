class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
    def push(self,value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size +=1
        else:
            print('All out of space')
    
    def pop(self):
        if self.size >0:
            item_to_remove = self.top_item
            if self.size ==1:
                self.top_item = None
            else:
                self.top_item = item_to_remove.get_next_value()
            self.size -=1
        else:
            print("No node to pop (totally empty)")
    
    def peek(self):
        if self.size >0:
            return self.top_item.get_value()
        else:
            print("nothing to see here")
            
    def is_empty(self):
        return self.size == 0