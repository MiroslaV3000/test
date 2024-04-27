import unittest
import Create_Table
import Find_CDNF
import Find_SKNF

class TestTruthTable(unittest.TestCase):
    def test_simple_expression(self):
        expression = 'A&B'
        expected_output = [{'A': 0, 'B': 0, 'result': 0},
                           {'A': 0, 'B': 1, 'result': 0},
                           {'A': 1, 'B': 0, 'result': 0},
                           {'A': 1, 'B': 1, 'result': 1}]
        self.assertEqual(Create_Table.truth_table(expression), expected_output)

    def test_complex_expression(self):
        expression = 'A&B|C'
        expected_output = [{'A': 0, 'B': 0, 'C': 0, 'result': 0},
                           {'A': 0, 'B': 0, 'C': 1, 'result': 1},
                           {'A': 0, 'B': 1, 'C': 0, 'result': 0},
                           {'A': 0, 'B': 1, 'C': 1, 'result': 1},
                           {'A': 1, 'B': 0, 'C': 0, 'result': 0},
                           {'A': 1, 'B': 0, 'C': 1, 'result': 1},
                           {'A': 1, 'B': 1, 'C': 0, 'result': 1},
                           {'A': 1, 'B': 1, 'C': 1, 'result': 1}]
        self.assertEqual(Create_Table.truth_table(expression), expected_output)

    def test_expression_with_negation(self):
        expression = 'A&!B'
        expected_output = [{'A': 0, 'B': 0, 'result': 0},
                           {'A': 0, 'B': 1, 'result': 0},
                           {'A': 1, 'B': 0, 'result': 1},
                           {'A': 1, 'B': 1, 'result': 0}]
        self.assertEqual(Create_Table.truth_table(expression), expected_output)

class TestTruthTableToDNF(unittest.TestCase):
    def test_simple_truth_table(self):
        table = [{'A': 0, 'B': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'result': 0},
                 {'A': 1, 'B': 0, 'result': 0},
                 {'A': 1, 'B': 1, 'result': 1}]
        expected_output = '(A & B)'
        self.assertEqual(Find_CDNF.truth_table_to_dnf(table), expected_output)

    def test_complex_truth_table(self):
        table = [{'A': 0, 'B': 0, 'C': 0, 'result': 0},
                 {'A': 0, 'B': 0, 'C': 1, 'result': 1},
                 {'A': 0, 'B': 1, 'C': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'C': 1, 'result': 1},
                 {'A': 1, 'B': 0, 'C': 0, 'result': 0},
                 {'A': 1, 'B': 0, 'C': 1, 'result': 1},
                 {'A': 1, 'B': 1, 'C': 0, 'result': 1},
                 {'A': 1, 'B': 1, 'C': 1, 'result': 1}]
        expected_output = '(!A & !B & C) | (!A & B & C) | (A & !B & C) | (A & B & !C) | (A & B & C)'
        self.assertEqual(Find_CDNF.truth_table_to_dnf(table), expected_output)

    def test_truth_table_with_negation(self):
        table = [{'A': 0, 'B': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'result': 0},
                 {'A': 1, 'B': 0, 'result': 1},
                 {'A': 1, 'B': 1, 'result': 0}]
        expected_output = '(A & !B)'
        self.assertEqual(Find_CDNF.truth_table_to_dnf(table), expected_output)

class TestTruthTableToCNF(unittest.TestCase):
    def test_simple_truth_table(self):
        table = [{'A': 0, 'B': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'result': 0},
                 {'A': 1, 'B': 0, 'result': 0},
                 {'A': 1, 'B': 1, 'result': 1}]
        expected_output = '(A | B) & (A | !B) & (!A | B)'
        self.assertEqual(Find_SKNF.truth_table_to_cnf(table), expected_output)

    def test_complex_truth_table(self):
        table = [{'A': 0, 'B': 0, 'C': 0, 'result': 0},
                 {'A': 0, 'B': 0, 'C': 1, 'result': 1},
                 {'A': 0, 'B': 1, 'C': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'C': 1, 'result': 1},
                 {'A': 1, 'B': 0, 'C': 0, 'result': 0},
                 {'A': 1, 'B': 0, 'C': 1, 'result': 1},
                 {'A': 1, 'B': 1, 'C': 0, 'result': 1},
                 {'A': 1, 'B': 1, 'C': 1, 'result': 1}]
        expected_output = '(A | B | C) & (A | !B | C) & (!A | B | C)'
        self.assertEqual(Find_SKNF.truth_table_to_cnf(table), expected_output)

    def test_truth_table_with_negation(self):
        table = [{'A': 0, 'B': 0, 'result': 0},
                 {'A': 0, 'B': 1, 'result': 0},
                 {'A': 1, 'B': 0, 'result': 1},
                 {'A': 1, 'B': 1, 'result': 0}]
        expected_output = '(A | B) & (A | !B) & (!A | !B)'
        self.assertEqual(Find_SKNF.truth_table_to_cnf(table), expected_output)

if __name__ == '__main__':
    unittest.main()
