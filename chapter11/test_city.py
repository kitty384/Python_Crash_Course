import unittest
from city_function import show_info


class CityTestCase(unittest.TestCase):

    def test_city_conuntry(self):
        formatted_city = show_info('santiago', 'chile')
        self.assertEqual(formatted_city, "Santiago,Chile")

    def test_city_country_population(self):
        formatted_city = show_info('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, "Santiago,Chile - population 5000000")


unittest.main()
