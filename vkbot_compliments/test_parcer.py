import parcer as p
import unittest


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = p.parce()

    def test_get_compliment(self):
        self.assertEqual(type(self.parser), list)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
