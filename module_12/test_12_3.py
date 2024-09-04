import module_12_1 as m
import unittest
import module_12_2 as n


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        man = m.Runner('Skott')
        for _ in range(10):
            man.walk()
        self.assertEqual(man.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        man = m.Runner('Skott')
        for _ in range(10):
            man.run()
        self.assertEqual(man.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        man_1 = m.Runner('test 1')
        man_2 = m.Runner('test 2')
        for _ in range(10):
            man_1.run()
            man_2.walk()
        self.assertNotEqual(man_1.distance, man_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = n.Runner('Усейн', 10)
        self.runner_2 = n.Runner('Андрей', 9)
        self.runner_3 = n.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results.values():
            print(res)

    def test_race_1(self):
        tour = n.Tournament(90, self.runner_1, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_race_2(self):
        tour = n.Tournament(90, self.runner_2, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_race_3(self):
        tour = n.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()



