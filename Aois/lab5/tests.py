import unittest
import MinimizedSDNF
import CreateSDNF



class TestQuineMcCluskey(unittest.TestCase):
    def test_combine_implicants(self):
        self.assertEqual(MinimizedSDNF.combine_implicants(['a', 'b', 'c'], ['a', 'b', '-']), ['a', 'b', '-'])
        self.assertEqual(MinimizedSDNF.combine_implicants(['a', 'b', 'c'], ['a', 'c', 'd']), None)

    def test_Quine_McCluskey(self):
        cnf = [['a', 'b', 'c'], ['a', 'b', '!c'], ['a', '!b', 'c'], ['!a', 'b', 'c']]
        expected_result = [['a', 'b', '-'], ['a', '-', 'c'], ['-', 'b', 'c']]
        self.assertEqual(MinimizedSDNF.Quine_McCluskey(cnf), expected_result)

    def test_implicants_to_string(self):
        implicants = [['a', 'b', '-'], ['a', '-', 'c'], ['-', 'b', 'c']]
        expected_result = '(a | b | -) & (a | - | c) & (- | b | c)'
        self.assertEqual(MinimizedSDNF.implicants_to_string(implicants), expected_result)

    def test_string_to_cnf(self):
        cnf_string = '(a & b & c) | (a & !b & c) | (!a & b & c)'
        expected_result = [['a', 'b', 'c'], ['a', '!b', 'c'], ['!a', 'b', 'c']]
        self.assertEqual(MinimizedSDNF.string_to_cnf(cnf_string), expected_result)

class TestTruthTableToDNF(unittest.TestCase):
    def test_truth_table_to_dnf(self):
        # Пример таблицы истинности
        table = [
            {'a': 0, 'b': 0, 'c': 0, 'result': 0},
            {'a': 0, 'b': 0, 'c': 1, 'result': 1},
            {'a': 0, 'b': 1, 'c': 0, 'result': 1},
            {'a': 0, 'b': 1, 'c': 1, 'result': 1},
            {'a': 1, 'b': 0, 'c': 0, 'result': 1},
            {'a': 1, 'b': 0, 'c': 1, 'result': 1},
            {'a': 1, 'b': 1, 'c': 0, 'result': 1},
            {'a': 1, 'b': 1, 'c': 1, 'result': 0}
        ]

        expected_dnf = '(!a & !b & c) | (!a & b & !c) | (!a & b & c) | (a & !b & !c) | (a & !b & c) | (a & b & !c)'
        self.assertEqual(CreateSDNF.truth_table_to_dnf(table), expected_dnf)
if __name__ == '__main__':
    unittest.main()