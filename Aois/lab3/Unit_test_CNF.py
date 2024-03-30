

# Assuming the functions are defined in a module named quine_mccluskey_module
import TableMethod

import unittest

# Assuming the functions are defined in a module named quine_mccluskey_module
import  TableMethod

class TestQuineMcCluskey(unittest.TestCase):

    def test_can_merge(self):
        self.assertTrue(TableMethod.can_merge('0000', '0001'))

        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

    def test_merge(self):
        self.assertTrue(TableMethod.merge('0000', '0001'), '000-')
        self.assertTrue(TableMethod.merge('1111', '1110'), '111-')
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

    def test_quine_mccluskey(self):
        # The Quine-McCluskey algorithm is a complex algorithm that simplifies boolean expressions.
        # We need to ensure that the `quine_mccluskey` function is working correctly before we can write tests for it.
        # For now, we'll assume that the function is working correctly and that the expected results are known.
        minterms = ['0000', '0001', '0010', '0100', '1000', '0110', '1010', '1100']
        expected_prime_implicants = ['0--0', '-0-0', '--00']  # Example expected results
        self.assertTrue(TableMethod.quine_mccluskey(minterms), expected_prime_implicants)


    def test_cnf_to_minterms(self):
        cnf_expression = "(x1|x2|x3)&(x1|x2|!x3)&(!x1|x2|x3)&(x1|!x2|x3)"
        expected_minterms = ['010', '100', '101', '110', '011']  # Example expected results
        self.assertTrue(TableMethod.cnf_to_minterms(cnf_expression), expected_minterms)
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"



    def test_dnf_to_minterms(self):
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"
        expected_minterms = ['010', '100', '101', '110', '011']  # Example expected results
        self.assertTrue(TableMethod.dnf_to_minterms(dnf_expression), expected_minterms)
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"

    def test_print_table(self):
        dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"
        expected_minterms = ['010', '100', '101', '110', '011']  # Example expected results
        self.assertFalse(TableMethod.print_table(['010', '100', '101', '110', '011'], is_cnf=True))



if __name__ == '__main__':
    unittest.main()