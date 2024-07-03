class Node: 
    def __init__(self, data, prev_node=None, next_node=None):
        self._data = data
        self._prev_node = prev_node
        self._next_node = next_node

    
    def get_data(self):
        return self._data
    

    def get_prev_node(self):
        return self._prev_node
    

    def set_prev_node(self, prev_node):
        self._prev_node = prev_node

    
    def get_next_node(self):
        return self._next_node

    
    def set_next_node(self, next_node):
        self._next_node = next_node
