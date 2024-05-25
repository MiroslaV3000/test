import unittest
import itertools

class TestFunctions(unittest.TestCase):

    def test_generate_truth_table(self):
        expression = "a & b"
        variables = ['a', 'b']
        result = generate_truth_table(expression, variables)
        self.assertEqual(result, '(!a | !b)')

    def test_truth_table(self):
        formula = "a & b"
        num_variables = 2
        result = truth_table(formula, num_variables)
        expected_result = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
        self.assertEqual(result, expected_result)

    def test_four_and_three_karnaugh_map(self):
        table = [(0, 0, 0, 0), (0, 1, 0, 1), (1, 0, 1, 0), (1, 1, 1, 1)]
        count_of_row = 2
        result = four_and_three_karnaugh_map(table, count_of_row)
        expected_result = [[0, 1], [1, 0]]
        self.assertEqual(result, expected_result)

    def test_two_karnaugh_map(self):
        table = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
        result = two_karnaugh_map(table)
        expected_result = [[0, 1], [1, 0]]
        self.assertEqual(result, expected_result)

    def test_sknf_to_binary(self):
        sknf = "(!a | !b) & (a | !c)"
        result = sknf_to_binary(sknf)
        expected_result = ['(1,0,1)', '(0,1,0)']
        self.assertEqual(result, expected_result)

    def test_group_by_units(self):
        binary_clauses = ['(1,0,1)', '(0,1,0)']
        result = group_by_units(binary_clauses)
        expected_result = {1: ['(1,0,1)'], 2: ['(0,1,0)']}
        self.assertEqual(result, expected_result)

    def test_karno_compare_constituents(self):
        constituents = {1: ['(1,0,1)'], 2: ['(0,1,0)']}
        result = karno_compare_constituents(constituents)
        expected_result = ['(1,*,1)']
        self.assertEqual(result, expected_result)

    def test_karno_compare_elements(self):
        elements = ['(1,*,1)']
        result = karno_compare_elements(elements)
        expected_result = ['(*,*,1)']
        self.assertEqual(result, expected_result)

    def test_karno_min(self):
        dict_data = {1: ['(1,0,1)'], 2: ['(0,1,0)']}
        array_data = [['(1,*,1)']]
        binary_output = ['(1,0,1)', '(0,1,0)']
        result = karno_min(dict_data, array_data, binary_output)
        expected_result = "Нет совпадений"
        self.assertEqual(result, expected_result)

    def test_karno_check(self):
        array_data = ['(*,*,1)']
        result = karno_check(array_data)
        expected_result = "!b & a "
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()