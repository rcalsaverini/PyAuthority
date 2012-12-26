import unittest
from Agent import Agent

class testAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
    def testPluck(self):
        self.agent.pluck()

    def testGroupSize(self):
        agent = Agent(n=10)
        self.assertEqual(agent.groupSize(), 10)

    def testRandomVertexPair(self):
        (i,j) = self.agent.getRandomVertexPair()
        self.assertGreater(self.agent.groupSize(), i)
        self.assertGreater(self.agent.groupSize(), j)

    def testAddAndRemoveEdge(self):
        agent = Agent(n=10, p = 0)
        self.assertFalse(agent.graph.are_connected(0,1))
        agent.addEdge(0,1)
        self.assertTrue(agent.graph.are_connected(0,1))
        agent.removeEdge(0,1)
        self.assertFalse(agent.graph.are_connected(0,1))

    def testPluckEdge(self):
        agent = Agent(n=10, p =0)
        agent.pluckEdge(1,2)

    def testPluckTillConnectedEmpty(self):
        agent = Agent(n=10, p=0.0)
        agent.pluckTillConnected()
        self.assertTrue(agent.isConnected())

    def testPluckTillConnectedStar(self):
        agent = Agent(n=20, topology='Star')
        agent.pluckTillConnected()
        self.assertTrue(agent.isConnected)

