from unittest.case import TestCase

from economic_dybdahl_rest.usecases.get_products_in.product_numbers_string_splitter import split_product_number_string


class TestProductNumbersStringSplitter(TestCase):

    def test_split_01(self):
        split_str = None
        result = split_product_number_string(split_str)
        self.assertEqual([], result)

    def test_split_02(self):
        split_str = ''
        result = split_product_number_string(split_str)
        self.assertEqual([], result)

    def test_split_03(self):
        split_str = '[]'
        result = split_product_number_string(split_str)
        self.assertEqual([], result)

    def test_split_04(self):
        split_str = '[12gfyasd782ehgd]'
        result = split_product_number_string(split_str)
        self.assertEqual(['12gfyasd782ehgd'], result)

    def test_split_05(self):
        split_str = '[1, 2, 3]'
        result = split_product_number_string(split_str)
        self.assertEqual(['1', '2', '3'], result)

    def test_split_06(self):
        split_str = '[1,2,3]'
        result = split_product_number_string(split_str)
        self.assertEqual(['1', '2', '3'], result)

    def test_split_07(self):
        split_str = '[9cc35e458a1bc06d6a, e5dd470f69a4200716,\'2b1af06c97cea918eb\']'
        result = split_product_number_string(split_str)
        self.assertEqual(['9cc35e458a1bc06d6a', 'e5dd470f69a4200716', '2b1af06c97cea918eb'], result)
