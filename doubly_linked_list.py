from node import Node

class DoublyLinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._list_length = 0


    def list_len(self):
        return self._list_length
    
    
    def inc_list_len(self):
        self._list_length += 1

    
    def dec_list_len(self):
        self._list_length -= 1

    
    def empty(self):
        return self.list_len() == 0
    
    
    def _remove_node(self, node):
        prev_node = node.get_prev_node()
        next_node = node.get_next_node()

        if prev_node:
            prev_node.set_next_node(next_node)
        else:
            self.set_head_node(next_node)

        if next_node:
            next_node.set_prev_node(prev_node)
        else:
            self.set_tail_node(prev_node)

        self.dec_list_len()
    

    def get_head_node(self):
        return self._head_node
    

    def set_head_node(self, new_head):
        self._head_node = new_head


    def add_head_node(self, data):
        new_head = Node(data)

        if not self.empty():
            current_head = self.get_head_node()
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
            self.set_head_node(new_head)
        
        else:
            self.set_head_node(new_head)
            self.set_tail_node(new_head)
        
        self.inc_list_len()

    
    def remove_head_node(self):
        if not self.empty():
            node_to_remove = self.get_head_node()
            self._remove_node(node_to_remove)
            

    def remove_by_data(self, data_to_remove):
        if self.empty():
            raise ValueError("Empty list")
        
        start_pointer = self.get_head_node()
        end_pointer = self.get_tail_node()

        while start_pointer is not None and end_pointer is not None:
            if start_pointer.get_data() == data_to_remove:
                self._remove_node(start_pointer)
                return
            
            if end_pointer.get_data() == data_to_remove:
                self._remove_node(end_pointer)
                return
            
            if start_pointer == end_pointer or start_pointer.get_next_node() == end_pointer:
                break

            start_pointer = start_pointer.get_next_node()
            end_pointer = end_pointer.get_prev_node()

        raise ValueError(f"Data '{data_to_remove}' not found in the list.")
        

    def get_tail_node(self):
        return self._tail_node


    def set_tail_node(self, new_tail):
        self._tail_node = new_tail

    
    def add_tail_node(self, data):
        new_tail = Node(data)

        if not self.empty():
            current_tail = self.get_tail_node()
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
            self.set_tail_node(new_tail)
        else: 
            self.set_tail_node(new_tail)
            self.set_head_node(new_tail)
        
        self.inc_list_len()


    def remove_tail_node(self):
        if not self.empty():
            node_to_remove = self.get_tail_node()
            self._remove_node(node_to_remove)
           

    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_data() != None:
                string_list += str(current_node.get_data()) + " <-> "
            current_node = current_node.get_next_node()
        return string_list
    