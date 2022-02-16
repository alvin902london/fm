import unittest
from app.question2 import Question2

class TestQuestion2(unittest.TestCase):

    def setUp(self):
        self.test = Question2()
        self.data = {
            # example case 2a
            'app/example_data1.txt': {
                'light red': {'bright white': 1, 'muted yellow': 2},
                'dark orange': {'bright white': 3, 'muted yellow': 4},
                'bright white': {'shiny gold': 1},
                'muted yellow': {'shiny gold': 2, 'faded blue': 9},
                'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
                'dark olive': {'faded blue': 3, 'dotted black': 4},
                'vibrant plum': {'faded blue': 5, 'dotted black': 6}
            },
            # example case 2b
            'app/example_data2.txt': {
                'shiny gold': {'dark red': 2},
                'dark red': {'dark orange': 2},
                'dark orange': {'dark yellow': 2},
                'dark yellow': {'dark green': 2},
                'dark green': {'dark blue': 2},
                'dark blue': {'dark violet': 2},
            },
            # # edge case: cycle
            # 'app/example_data3.txt': {
            #     'bright turquoise': { "muted green": 2},
            #     'muted green': { "bright turquoise": 5}
            # },
            # edge case: larger number
            'app/example_data4.txt': {
                "bright white": {"shiny gold": 1000000000000},
                "light red": {"bright white": 100000000000000, "muted yellow": 2},
                "shiny gold": {"muted yellow": 1000000000000000000000000}
            }
        }
        self.error_msg = f"Invalid rules: cycle detected"

    def tearDown(self):
        pass

    def test_parse_file(self):
        for fp, data in self.data.items():
            with self.subTest(fp=fp, data=data):
                result = self.test.parse_file(fp)
                self.assertEqual(result, data)

    def test_topological_sort(self):
        self.test.query = 'shiny gold'
        for data, expected in zip(self.data.values(), [[4, 32], [0, 126], [self.error_msg, self.error_msg]]):
            with self.subTest(data=data):
                self.test.prerequisites = data
                q2a, q2b = self.test.topological_sort()
                self.assertEqual(q2a, expected[0])
                self.assertEqual(q2b, expected[1])
        
        self.test.query = 'hermes'
        for data, expected in zip(self.data.values(), [[0, 0], [0, 0], [self.error_msg, self.error_msg]]):
            with self.subTest(data=data):
                self.test.prerequisites = data
                q2a, q2b = self.test.topological_sort()
                self.assertEqual(q2a, expected[0])
                self.assertEqual(q2b, expected[1])
        
        self.test.query = 'light red'
        self.test.prerequisites = self.data['app/example_data4.txt']
        q2a, q2b = self.test.topological_sort()
        self.assertEqual(q2a, 0)
        self.assertEqual(q2b, 100000000000000000000000100000000000100000000000002)

if __name__ == '__main__':
    unittest.main()