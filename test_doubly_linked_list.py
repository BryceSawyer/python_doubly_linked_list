import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_add_head_node(self):
        dll = DoublyLinkedList()
        dll.add_head_node(1)
        dll.add_head_node(2)
        self.assertEqual(dll.stringify_list(), "2 <-> 1 <-> ")

    def test_add_tail_node(self):
        dll = DoublyLinkedList()
        dll.add_tail_node(1)
        dll.add_tail_node(2)
        self.assertEqual(dll.stringify_list(), "1 <-> 2 <-> ")

    def test_remove_head_node(self):
        dll = DoublyLinkedList()
        dll.add_head_node(1)
        dll.add_head_node(2)
        dll.remove_head_node()
        self.assertEqual(dll.stringify_list(), "1 <-> ")
        dll.remove_head_node()
        self.assertEqual(dll.stringify_list(), "")

    def test_remove_tail_node(self):
        dll = DoublyLinkedList()
        dll.add_tail_node(1)
        dll.add_tail_node(2)
        dll.remove_tail_node()
        self.assertEqual(dll.stringify_list(), "1 <-> ")
        dll.remove_tail_node()
        self.assertEqual(dll.stringify_list(), "")

    def test_remove_by_data(self):
        dll = DoublyLinkedList()
        dll.add_head_node(1)
        dll.add_head_node(2)
        dll.add_tail_node(3)
        dll.add_tail_node(4)
        self.assertEqual(dll.stringify_list(), "2 <-> 1 <-> 3 <-> 4 <-> ")
        dll.remove_by_data(3)
        self.assertEqual(dll.stringify_list(), "2 <-> 1 <-> 4 <-> ")
        dll.remove_by_data(2)
        self.assertEqual(dll.stringify_list(), "1 <-> 4 <-> ")
        dll.remove_by_data(4)
        self.assertEqual(dll.stringify_list(), "1 <-> ")
        dll.remove_by_data(1)
        self.assertEqual(dll.stringify_list(), "")

    def test_remove_by_data_empty_list(self):
        dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            dll.remove_by_data(10)

    def test_remove_by_data_not_found(self):
        dll = DoublyLinkedList()
        dll.add_head_node(1)
        with self.assertRaises(ValueError):
            dll.remove_by_data(10)

    def test_list_len(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.list_len(), 0)
        dll.add_head_node(1)
        self.assertEqual(dll.list_len(), 1)
        dll.add_tail_node(2)
        self.assertEqual(dll.list_len(), 2)
        dll.remove_head_node()
        self.assertEqual(dll.list_len(), 1)
        dll.remove_tail_node()
        self.assertEqual(dll.list_len(), 0)


if __name__ == '__main__':
    unittest.main()
    