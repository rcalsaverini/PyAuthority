import unittest
from Agent import MonteCarloAgent
from numpy import exp

class testAgent(unittest.TestCase):

    def testInitialization(self):
        agent = MonteCarloAgent()
        self.assertEqual(agent.beta, 1.0)


    def testAcceptPropositionEnergyDecrease(self):
        agent = MonteCarloAgent()
        self.assertTrue(agent.acceptProposition(0.0, -1.0))

    def testAcceptPropositionEnergyIncrease(self):
        agent = MonteCarloAgent(beta=1.0)
        Enew = 1.0
        Eold = 0.0
        p = exp(-1.0 * (Enew - Eold))
        naccept = 0
        ntotal = 100000
        for i in xrange(ntotal):
            naccept += int(agent.acceptProposition(Eold, Enew))
        q = float(naccept)/float(ntotal)
        self.assertAlmostEqual(q, p, delta = 1e-2)

