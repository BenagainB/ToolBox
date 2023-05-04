# test_FederalTaxes2023.py
""" test cases for 2023FederalTaxes """
# https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
# For the 2023 tax year, there are seven tax rates:
# 10%, 12%, 22%, 24%, 32%, 35% and 37%, the same as in tax year 2022.
# Taxes for the 2023 calendar year are due in April 2024.

import unittest
from FederalTaxes2023 import SingleFiler, MarriedFilingJointly, MarriedFilingSeparately, HeadOfHousehold


class TestSingleFiler(unittest.TestCase):
    """ test class for SingleFiler """

    def setUp(self):
        self.single_guy = SingleFiler()
        # self.node1 = Node(1, None, None)
        # self.node2 = Node(2, None, None)
        # self.node3 = Node(3, None, None)
        # self.node4 = Node(4, None, None)
        # self.node5 = Node(5, None, None)

    def test_creation_of_single_filer(self):
        """ ensure single filer class is instanced """
        self.assertIsInstance(self.single_guy, SingleFiler)

        # self.assertIsNotNone(self.my_linked_list)
        # self.assertIsNotNone(self.node1)
        # self.assertEqual(1, self.node1.get_value())
        # self.node1.set_value(2)
        # self.assertEqual(2, self.node1.get_value())
        # self.assertIsNone(self.node1.get_next())


class TestMarriedFilingJointly(unittest.TestCase):
    """ test class for MarriedFilingJointly """

    def setUp(self):
        self.happy_couple = MarriedFilingJointly()

    def test_creation_of_married_joint_filer(self):
        """ ensure married joint filer class is instanced """
        self.assertIsInstance(self.happy_couple, MarriedFilingJointly)


class TestMarriedFilingSeparately(unittest.TestCase):
    """ test class for MarriedFilingSeparately """

    def setUp(self):
        self.unhappy_couple = MarriedFilingSeparately()

    def test_creation_of_married_joint_filer(self):
        """ ensure married joint filer class is instanced """
        self.assertIsInstance(self.unhappy_couple, MarriedFilingSeparately)


class TestHeadOfHousehold(unittest.TestCase):
    """ test class for MarriedFilingSeparately """

    def setUp(self):
        self.head_of_house = HeadOfHousehold()

    def test_creation_of_married_joint_filer(self):
        """ ensure married joint filer class is instanced """
        self.assertIsInstance(self.head_of_house, HeadOfHousehold)

# python test_SinglyLinkedList.py
    # ...........
    # ----------------------------------------------------------------------
    # Ran 16 tests in 0.000s
    # OK

# pip install pytest
# Use pytest to test all cases beginning with test_ (even if main is not defined)

# pip install coverage
# coverage run SinglyLinkedList.py
# coverage report ass3_SinglyLinkedList.py
    # Name                  Stmts   Miss  Cover
    # -----------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # -----------------------------------------
    # TOTAL                   105      0   100%
# coverage report -m SinglyLinkedList.py
    # Name                  Stmts   Miss  Cover   Missing
    # ---------------------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # ---------------------------------------------------
    # TOTAL                   105      0   100%
# coverage html
    # generates htmlcov folder, view index.html to see clean report

# pip install pytest-cov
# pytest --cov=SinglyLinkedList
    # collected 16 items
    # test_SinglyLinkedList.py .........                                                    [100%]
    # ---------- coverage: platform darwin, python 2.7.18-final-0 ----------
    # Name                  Stmts   Miss  Cover
    # -----------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # -----------------------------------------
    # TOTAL                   105      0   100%
    # ========== 16 passed in 0.11 seconds ======================================================


if __name__ == "__main__":
    unittest.main()
