import unittest
from utils import init_ca

class TestUtils(unittest.TestCase):
    def test_init_ca(self):
        size = 5
        center_value = 100
        acutal_result = init_ca(size, center_value)
        self.assertEqual(size, acutal_result.size)
        self.assertEqual(center_value, acutal_result[0][2])

if __name__ == "__main__":
    unittest.main()