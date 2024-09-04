import logging
import module_12_4 as m
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            man = m.Runner('Skott', speed=-5)
            if man.speed > 0:
                for _ in range(10):
                    man.walk()
                logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            man = m.Runner(15)
            if type(man.name) == str:
                for _ in range(10):
                    man.run()
                logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        man_1 = m.Runner('test 1')
        man_2 = m.Runner('test 2')
        for _ in range(10):
            man_1.run()
            man_2.walk()
        self.assertNotEqual(man_1.distance, man_2.distance)


if __name__ == '__main__':
   unittest.main()

