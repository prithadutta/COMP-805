import unittest
class Lab4Test(unittest.TestCase):

    def test_square_nums(self):
        """
        Tests lab4.square_nums()
        """
        func=lab4.square_nums
        print ("In test_square_nums")
        case1= [1, 2, 3]
        expected1= [1, 4, 9]
        self.assertEqual(func(case1), expected1)

    def test_switch_case(self):
        """
        Tests lab4.switch_case()
        """
        func=lab4.switch_case
        print("In test_switch_case")
        case1= ["Apple", "I am student"]
        expected1= ["apple", "i am student"]
        self.assertEqual(func(case1), expected1)

    def test_only_even(self):
        """
        Tests lab4.only_even()
        """
        func=lab4.only_even
        print("In test_only_even")
        case1=["Apples", 46, 88, "apple"]
        expected1=["Apples", 46, 88]
        self.assertEqual(func(case1), expected1)

    def test_greatest_difference(self):
        """
        Tests lab4.greatest_difference()
        """
        func=lab4.greatest_difference
        print("In test_greatest_difference")
        case1=[3, 5, 10, 15]
        expected1=12
        self.assertEqual(func(case1), expected1)

    def test_make_title(self):
        """
        Tests lab4.make_title()
        """
        func=lab4.make_title
        print("In test_make_title")
        case1=["apple", "banana is fruit"]
        expected1=["Apple", "Banana Is Fruit"]
        self.assertEqual(func(case1), expected1)

    def test_test_title(self):
        """
        Tests lab4.test_title()
        """
        func=lab4.test_title
        print("In test_test_title")
        case1=["APPLE", "Banana is fruit"]
        expected1=["APPLE"], ["Banana is fruit"]
        self.assertEqual(func(case1), expected1)

    def test_create_word(self):
        """
        Tests lab4.create_word()
        """
        func=lab4.create_word
        print("In test_create_word")
        case1=["a", "p", "p", "l", "e", "5@students"]
        expected1=["a", "p", "p", "l", "e"]
        self.assertEqual(func(case1), expected1)

    def test_three_times_nums(self):
        """
        Tests lab4.three_times_nums()
        """
        func=lab4.three_times_nums
        print("In test_three_times_nums")
        case1=[4, 5, 6]
        expected1=[12, 15, 18]
        self.assertEqual(func(case1), expected1)

    def test_keep_lowercase(self):
        """
        Tests lab4.keep_lowercase()
        """
        func=lab4.keep_lowercase
        print("In test_keep_lower_case")
        case1=["APPLE", "apple"]
        expected1=["apple"]
        self.assertEqual(func(case1), expected1)

    def multiplication_total_of(self):
        """
        Tests lab4.multiplication_total_of()
        """
        func=lab4.multiplication_total_of
        print("In test_multiplication_total_of")
        case1=[5, 3, 10]
        expected1=[150]
        self.assertEqual(func(case1), expected1)

    def lessthan_5(self):
        """
        Tests lab4.lessthan_5()
        """
        func=lab4.lessthan_5
        print("In test_lessthan_5")
        case1=[5, 3, 10]
        expected1=[3]
        self.assertEqual(func(case1), expected1)

    def subtraction_of(self):
        """
        Tests lab4.subtraction_of()
        """
        func=lab4.subtraction_of
        print("In test_subtraction_of")
        case1=[5, 10, 15]
        expected1=[5,5]
        self.assertEqual(func(case1), expected1)

    def double_nums(self):
        """
        Tests lab4.double_nums()
        """
        func=lab4.double_nums
        print("In test_double_nums")
        case1=[5, 10, 20]
        expected1=[10,20,40]
        self.assertEqual(func(case1), expected1)

    def remove_special_characters(self):
        """
        Tests lab4.remove_special_characters()
        """
        func=lab4.remove_special_characters
        print("In test_remove_special_characters")
        case1=["Apple", "Banana@", "50students"]
        expected1=["Apple", "50students"]
        self.assertEqual(func(case1), expected1)



if __name__=='__main__':
    try:
        import lab4
        print("lab4.py module found.Testing...")
        unittest.main()
    except ImportError:
        print("Missing lab4.py module")
