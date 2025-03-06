
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link
    
    def __len__(self):
        if self.link is None: return 1
        return 1 + len(self.link)
    
    def get_tail(self):
        """Returns the data stored in the tail node"""
        if self.link is None:
            return self.data
        return self.link.get_tail()
    
    def add_last(self, data):
        """Adds a node containing data to the end of this list"""
        if self.link is None:
            self.link = Node(data)
        else:
            self.link.add_last(data)
    
    def total(self):
        """Recursively calculates the sum of all items in the list"""
        if self.link is None:
            return self.data
        return self.data + self.link.total()
    
    def remove_last(self):
        """Removes the last node from this list and returns (new head, data from tail)"""
        if self.link is None:
            return None, self.data
        
        if self.link.link is None:
            data = self.link.data
            self.link = None
            return self, data
        
        new_head, data = self.link.remove_last()
        return self, data
    
    def reverse(self, prev=None):
        """Reverses the linked list recursively"""
        if self.link is None:
            self.link = prev
            return self
        
        new_head = self.link.reverse(self)
        self.link = prev
        return new_head



