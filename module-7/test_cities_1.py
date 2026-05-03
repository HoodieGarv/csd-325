# 5/4/2026
# Module 7 Assignment - CSD-325
# Garvin Stewart

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        """Verify Santiago, Chile produces the correct string."""
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
