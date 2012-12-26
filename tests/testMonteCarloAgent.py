import unittest
from Agent import MonteCarloAgent

class testAgent(unittest.TestCase):

    def testInitialization(self):
        agent = MonteCarloAgent()
        self.assertEqual(agent.beta, 1.0)
