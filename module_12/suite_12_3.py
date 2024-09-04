import unittest
import test_12_3

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

test = unittest.TextTestRunner(verbosity=2)
test.run(suite)