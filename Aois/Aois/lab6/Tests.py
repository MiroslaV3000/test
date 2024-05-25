import unittest
import hash_table
from unittest.mock import patch, call
from io import StringIO


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = hash_table.Node("key1", "value1")
        self.assertEqual(node.key, "key1")
        self.assertEqual(node.value, "value1")
        self.assertIsNone(node.next)

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = hash_table.HashTable(20)

    def test_hash_function(self):
        self.assertEqual(self.hash_table.hash_function("ab"), 11)
        self.assertEqual(self.hash_table.hash_function("cd"), 19)
        self.assertEqual(self.hash_table.hash_function("ef"), 7)

    def test_insert(self):
        self.hash_table.insert("ab", "value1")
        self.assertEqual(self.hash_table.find("ab"), "value1")
        self.assertEqual(self.hash_table.size, 1)

        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.find("cd"), "value2")
        self.assertEqual(self.hash_table.size, 2)

        self.hash_table.insert("ab", "new_value1")
        self.assertEqual(self.hash_table.find("ab"), "new_value1")
        self.assertEqual(self.hash_table.size, 2)

    def test_find(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.find("ab"), "value1")
        self.assertEqual(self.hash_table.find("cd"), "value2")
        self.assertIsNone(self.hash_table.find("ef"))

    def test_remove(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.remove("ab"), "value1")
        self.assertEqual(self.hash_table.size, 1)
        self.assertIsNone(self.hash_table.find("ab"))
        self.assertEqual(self.hash_table.find("cd"), "value2")

        self.assertIsNone(self.hash_table.remove("ef"))
        self.assertEqual(self.hash_table.size, 1)

    def test_hash_function_edge_cases(self):
        self.assertEqual(self.hash_table.hash_function("aр"), 2)
        self.assertEqual(self.hash_table.hash_function("zр"), 7)


    def test_insert_collisions(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.hash_table.insert("ef", "value3")
        self.hash_table.insert("gh", "value4")
        self.hash_table.insert("ij", "value5")

        self.assertEqual(self.hash_table.find("ab"), "value1")
        self.assertEqual(self.hash_table.find("cd"), "value2")
        self.assertEqual(self.hash_table.find("ef"), "value3")
        self.assertEqual(self.hash_table.find("gh"), "value4")
        self.assertEqual(self.hash_table.find("ij"), "value5")

    def test_remove_collisions(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.hash_table.insert("ef", "value3")
        self.hash_table.insert("gh", "value4")
        self.hash_table.insert("ij", "value5")

        self.assertEqual(self.hash_table.remove("ab"), "value1")
        self.assertEqual(self.hash_table.size, 4)
        self.assertIsNone(self.hash_table.find("ab"))

        self.assertEqual(self.hash_table.remove("ef"), "value3")
        self.assertEqual(self.hash_table.size, 3)
        self.assertIsNone(self.hash_table.find("ef"))



    def test_all_strings(self):
        test_cases = [
            ("ab", "value1"),
            ("cd", "value2"),
            ("ef", "value3"),
            ("gh", "value4"),
            ("ij", "value5"),
            ("klmnopqrstuvwxyz", "value6"),
            ("абвгдеёжзийклмноп", "value7"),
            ("qrstuvwxyza", "value8"),
            ("абвгдеёжзийклмнопр", "value9"),
            ("stuvwxyzab", "value10")
        ]

        for key, value in test_cases:
            with self.subTest(key=key, value=value):
                self.hash_table.insert(key, value)
                self.assertEqual(self.hash_table.find(key), value)

    def test_remove_all_strings(self):
        test_cases = [
            ("ab", "value1"),
            ("cd", "value2"),
            ("ef", "value3"),
            ("gh", "value4"),
            ("ij", "value5"),
            ("klmnopqrstuvwxyz", "value6"),
            ("абвгдеёжзийклмноп", "value7"),
            ("qrstuvwxyza", "value8"),
            ("абвгдеёжзийклмнопр", "value9"),
            ("stuvwxyzab", "value10")
        ]

        for key, value in test_cases:
            with self.subTest(key=key, value=value):
                self.hash_table.insert(key, value)
                self.assertEqual(self.hash_table.find(key), value)
                self.assertEqual(self.hash_table.remove(key), value)
                self.assertIsNone(self.hash_table.find(key))



    def test_hash_functioned(self):
        self.assertEqual(self.hash_table.hash_function("ab"), 11)
        self.assertEqual(self.hash_table.hash_function("cd"), 19)
        self.assertEqual(self.hash_table.hash_function("ef"), 7)
        self.assertEqual(self.hash_table.hash_function("ёпр"), 14)
        self.assertEqual(self.hash_table.hash_function("епг"), 1)


    def test_insertd(self):
        self.hash_table.insert("ab", "value1")
        self.assertEqual(self.hash_table.find("ab"), "value1")
        self.assertEqual(self.hash_table.size, 1)

        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.find("cd"), "value2")
        self.assertEqual(self.hash_table.size, 2)

        self.hash_table.insert("ab", "new_value1")
        self.assertEqual(self.hash_table.find("ab"), "new_value1")
        self.assertEqual(self.hash_table.size, 2)

    def test_finde(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.find("ab"), "value1")
        self.assertEqual(self.hash_table.find("cd"), "value2")
        self.assertIsNone(self.hash_table.find("ef"))

    def test_removed(self):
        self.hash_table.insert("ab", "value1")
        self.hash_table.insert("cd", "value2")
        self.assertEqual(self.hash_table.remove("ab"), "value1")
        self.assertEqual(self.hash_table.size, 1)
        self.assertIsNone(self.hash_table.find("ab"))
        self.assertEqual(self.hash_table.find("cd"), "value2")

        self.assertIsNone(self.hash_table.remove("ef"))
        self.assertEqual(self.hash_table.size, 1)

if __name__ == '__main__':
    unittest.main()