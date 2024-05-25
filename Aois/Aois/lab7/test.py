import unittest
from io import StringIO
import sys
import Main

class TestMatrixFunctions(unittest.TestCase):

    def setUp(self):
        self.matrix = [[0 for _ in range(16)] for _ in range(16)]



    def test_write_conjunction_word(self):
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 2)
        self.matrix = Main.write_conjunction_word(self.matrix, 1, 2, 3)
        word = Main.read_word_by_index(self.matrix, 3)
        self.assertEqual(word, "1001001100110011")

    def test_write_sheffer_word(self):
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 2)
        self.matrix = Main.write_sheffer_word(self.matrix, 1, 2, 3)
        word = Main.read_word_by_index(self.matrix, 3)
        self.assertEqual(word, "0110110011001100")

    def test_find_nearest_value(self):
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110010", 2)
        result = Main.find_nearest_value(self.matrix, "1001001100110011")
        self.assertEqual(result, 0)

    def test_find_nearest_value_below(self):
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110010", 2)
        result = Main.find_nearest_value_below(self.matrix, "1001001100110011")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()