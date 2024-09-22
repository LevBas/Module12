import unittest
import module12_1

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = module12_1.Runner("Test1")
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn1 = module12_1.Runner("Test2")
        for i in range(10):
            rn1.run()
        self.assertEqual(rn1.distance, 100)

    def test_challenge(self):
        rn2 = module12_1.Runner("Test3")
        rn3 = module12_1.Runner("Test4")
        for i in range(10):
            rn2.walk()
            rn3.run()
        self.assertNotEqual(rn2.distance, rn3.distance)


