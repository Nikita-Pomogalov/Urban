import module_12_1 as m
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        man = m.Runner('Skott')
        for _ in range(10):
            man.walk()
        self.assertEqual(man.distance, 50)

    def test_run(self):
        man = m.Runner('Skott')
        for _ in range(10):
            man.run()
        self.assertEqual(man.distance, 100)

    def test_challenge(self):
        man_1 = m.Runner('test 1')
        man_2 = m.Runner('test 2')
        for _ in range(10):
            man_1.run()
            man_2.walk()
        self.assertNotEqual(man_1.distance, man_2.distance)



