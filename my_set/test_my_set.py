from unittest import TestCase, main

from my_set import MySet


class TestMySet(TestCase):
    def setUp(self):
        self.set = MySet()

    def test_add(self):
        self.set.add(4)
        self.assertEqual(self.set, {4})

        self.set.add(4)
        self.assertEqual(self.set, {4})

    def test_remove(self):
        self.set = {1, 2, 3}
        self.set.remove(1)
        self.assertEqual(self.set, {2, 3})

    def test_uniqueness(self):
        s = MySet()
        s.add(1)
        s.add(1)
        s.add(1)
        self.assertEqual(s, {1})

if __name__ == '__main__':
    main()