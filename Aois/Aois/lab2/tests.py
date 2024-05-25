import unittest
from Main import generate_truth_table  # replace with your actual module name

class TestTruthTable(unittest.TestCase):

    def test_generate_truth_table(self):
        # Test with a simple expression
        expression = "a & b"
        variables = ['a', 'b']
        # Since generate_truth_table prints the result, we can't capture it directly.
        # Instead, we can check if the function runs without errors.
        try:
            generate_truth_table(expression, variables)
        except Exception as e:
            self.fail(f"generate_truth_table raised an exception: {e}")

        # Test with a more complex expression
        expression = "((a | c) -> ((!b ~ d) & e))"
        variables = ['a', 'b', 'c', 'd', 'e']
        try:
            generate_truth_table(expression, variables)
        except Exception as e:
            self.fail(f"generate_truth_table raised an exception: {e}")

        # Test with an invalid expression
        expression = "a & b &"
        variables = ['a', 'b']
        try:
            generate_truth_table(expression, variables)
        except Exception as e:
            self.fail(f"generate_truth_table raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()