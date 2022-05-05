import unittest
from validators import validate_equation, compile_equation, get_equation_result
  
class TestValidators(unittest.TestCase):

    def test_valid_equation_sould_return_true(self):
        self.assertTrue(validate_equation('(2x+5)^2-9'))
    
    def test_equation_should_not_have_alphabet_except_x(self):
        self.assertFalse(validate_equation('(2x+5)^2-9y'))

    def test_equation_should_not_have_2_consecutive_x(self):
        self.assertFalse(validate_equation('xx'))
    
    def test_empty_string_should_return_false(self):
        self.assertFalse(validate_equation(''))

    def test_compile_equation_should_add_missing_astrisks(self):
        self.assertEqual(compile_equation('2x+3'), '2*x+3')
    
    def test_compile_equation_should_remove_spaces(self):
        self.assertEqual(compile_equation('2 x + 3'), '2*x+3')

    def test_compile_equation_should_replace_caret_with_double_asterisk(self):
        self.assertEqual(compile_equation('x^2+5'), 'x**2+5')
    
    def test_compile_equation_should_raise_exception_for_invalid_equation(self):
        with self.assertRaises(SyntaxError) as e:
            compile_equation('2xy+z')
            invalid_exception = e.exception
            self.assertEqual(invalid_exception, SyntaxError)

    def test_get_equation_result_returns_float_for_valid_input(self):
        self.assertEqual(type(get_equation_result('2x+3', 1)), float)
    
    def test_get_equation_result_returns_inf_for_division_by_zero(self):
        self.assertEqual(get_equation_result('2x+3/x', 0), float('inf'))

    def test_get_equation_raises_exception_for_invalid_input(self):
        with self.assertRaises(SyntaxError) as e:
            get_equation_result('2xy', 0)
            invalid_exception = e.exception
            self.assertEqual(invalid_exception, SyntaxError)

if __name__ == '__main__':
    unittest.main()
