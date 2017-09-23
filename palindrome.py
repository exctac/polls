import unittest


def palindrome(val):
    '''
    Допустим для вычичсления полиндрома, необходмо выполнить следующее условия:
        - Входящее значение может быть строкой или числом (положительным или отрицательным),
        - Длинна строки не менее 2, число двухзначное и выше.
        - Регистр символов строки не учитыввается.
    :param val: 
    :return: bool 
    '''

    error = ValueError("В качестве параметра должны быть непустая строка и минимум двухзначное число!"
                         "Например: 1234321, 'anna' и т.д.")

    if type(val) == str and len(val) >= 2:
        string = val.lower()
    elif (type(val) == int or type(val) == float) and len(str(abs(val))) >= 2:
        string = str(abs(int(val))).lower()
    else:
        raise error
    return string == string[::-1]


class TestPalindrome(unittest.TestCase):

    def my_fun(self):
        pass

    class Test(object):
        pass

    def test_int_true(self):
        self.assertEqual(palindrome(1234321), True)

    def test_int_negative_true(self):
        self.assertEqual(palindrome(-1234321), True)

    def test_int_negative_false(self):
        self.assertEqual(palindrome(-1234329), False)

    def test_int_false(self):
        self.assertEqual(palindrome(1234329), False)

    def test_str_true(self):
        self.assertEqual(palindrome('anna'), True)

    def test_str_false(self):
        self.assertEqual(palindrome('qwerty'), False)

    def test_error_True(self):
        self.assertRaises(ValueError, palindrome, True)

    def test_error_False(self):
        self.assertRaises(ValueError, palindrome, False)

    def test_error_tuple(self):
        self.assertRaises(ValueError, palindrome, tuple())

    def test_error_list(self):
        self.assertRaises(ValueError, palindrome, list())

    def test_error_dict(self):
        self.assertRaises(ValueError, palindrome, dict())

    def test_error_funс(self):
        self.assertRaises(ValueError, palindrome, self.my_fun)

    def test_error_class(self):
        self.assertRaises(ValueError, palindrome, self.Test)

    def test_error_class_inst(self):
        self.assertRaises(ValueError, palindrome, self.Test())

    def test_error_empty(self):
        self.assertRaises(ValueError, palindrome, '')

    def test_error_single_num(self):
        self.assertRaises(ValueError, palindrome, 2)

    def test_error_single_char(self):
        self.assertRaises(ValueError, palindrome, 'a')


if __name__ == '__main__':
    unittest.main()
