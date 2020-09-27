import ecs
import unittest

class TestGetNextCount(unittest.TestCase):
    def test_main(self):
        count_order = ['2', '4', '6']
        self.assertEqual(ecs.get_next_count(count_order, 2), '4')
        self.assertEqual(ecs.get_next_count(count_order, 4), '6')
        self.assertEqual(ecs.get_next_count(count_order, 6), '2')
        self.assertEqual(ecs.get_next_count(count_order, 8), '2')

if __name__ == '__main__':
    unittest.main()
