import unittest
from typing import Any, Optional, Iterable

class Node:
    def __init__(self, item: Any, link: Optional['Node'] = None) -> None:
        '''
        docstring
        '''
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        '''
        docstring
        '''
        return f"Node({self.item})"


class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        '''
        docstring
        '''
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._length = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self) -> int:
        '''
        docstring
        '''
        return self._length

    def get_head(self) -> Any:
        '''
        docstring
        '''
        return self._head.item if self._head else None

    def get_tail(self) -> Any:
        '''
        docstring
        '''
        return self._tail.item if self._tail else None

    def add_first(self, item: Any) -> None:
        '''
        docstring
        '''
        new_node = Node(item, self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._length += 1

    def add_last(self, item: Any) -> None:
        '''
        docstring
        '''
        new_node = Node(item)
        if self._tail:
            self._tail.link = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._length += 1

    def remove_first(self) -> Any:
        '''
        docstring
        '''
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty LinkedList.")

        removed_item = self._head.item
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return removed_item

    def remove_last(self) -> Any:
        '''
        docstring
        '''
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty LinkedList.")

        if self._head == self._tail:
            removed_item = self._head.item
            self._head = self._tail = None
        else:
            current = self._head
            while current.link and current.link != self._tail:
                current = current.link

            removed_item = self._tail.item
            current.link = None
            self._tail = current

        self._length -= 1
        return removed_item


    
class TestNode(unittest.TestCase):
    def test_setup(self):
        '''
        docstring
        '''
        Node1 = Node('something', 'something')
        self.assertEqual(Node1.item, 'something')
        self.assertEqual(Node1.link, 'something')

    def test_repr(self):
        '''
        docstring
        '''
        Node1 = Node('something', 'something')
        self.assertEqual(repr(Node1), "Node('something')")
    

class testLinkedList(unittest.TestCase):
    def test_setup(self):
        '''
        docstring
        '''
        LL1 = LinkedList()
        self.assertEqual(LL1.get_head(), None)
        self.assertEqual(LL1.get_tail(), None)

    def test_add_last(self):
        '''
        docstring
        '''
        LL1 = LinkedList()
        for i in range(10):
            LL1.add_last(i)

    def test_add_first(self):
        '''
        docstring
        '''
        LL1 = LinkedList()
        for i in range(10):
            LL1.add_first(i)

    def initialize_new_list(self):
        LL2 = LinkedList(['a', 'b','c'])


if __name__ == "__main__":
    unittest.main()
