import module_12_2 as m
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = m.Runner('Усейн', 10)
        self.runner_2 = m.Runner('Андрей', 9)
        self.runner_3 = m.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results.values():
            print(res)

    def test_race_1(self):
        tour = m.Tournament(90, self.runner_1, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_race_2(self):
        tour = m.Tournament(90, self.runner_2, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_race_3(self):
        tour = m.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = tour.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()



