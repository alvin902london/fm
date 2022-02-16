import unittest
from app.question1 import Question1

class TestQuestion1(unittest.TestCase):

    def test_dropping(self):
        data = [
            [3, 0.66, 1.5, 3], 
            [3, 0.8, 1.5, 7],
            [3, 1, 1.5, -1],
            [1000, 0.99, 500, 137]
        ]

        for d in data:
            with self.subTest(d=d):
                test = Question1(d[0], d[1], d[2])
                self.assertEqual(test.dropping(), d[3])  

if __name__ == '__main__':
    unittest.main()