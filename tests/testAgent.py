import unittest
from Agent import Agent
from numpy import Inf

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
        agent = Agent(n=10, p = 0, topology='ErdosRenyi')
        self.assertFalse(agent.graph.are_connected(0,1))
        agent.addEdge(0,1)
        self.assertTrue(agent.graph.are_connected(0,1))
        agent.removeEdge(0,1)
        self.assertFalse(agent.graph.are_connected(0,1))

    def testPluckEdge(self):
        agent = Agent(n=10, p =0)
        agent.pluckEdge(1,2)

    def testPluckTillConnectedEmpty(self):
        agent = Agent(n=10, topology='Empty')
        agent.pluckTillConnected()
        self.assertTrue(agent.isConnected())

    def testPluckTillConnectedStar(self):
        agent = Agent(n=20, topology='Star')
        agent.pluckTillConnected()
        self.assertTrue(agent.isConnected)

    def testAveragePathLengthFull(self):
        agent = Agent(n=10, topology='Full')
        self.assertEqual(1.0, agent.averagePathLength())

    def testAveragePathLengthEmpty(self):
        agent = Agent(n=10, topology='Empty')
        self.assertEqual(agent.averagePathLength(), Inf)

    def testAveragePathLengthStar(self):
        for j in xrange(5,20):
            n = float(j)
            agent = Agent(n=j, topology='Star')
            self.assertEqual(agent.averagePathLength(),(n-1)*2.0/n )

    def testEdgeOccupation(self):
        n = 10
        for m in xrange(0, 10, 1):
            agent = Agent(n = n, m = m, topology='ErdosRenyi')
            p = float(m)/float(n * (n-1)/2)
            self.assertEqual(agent.edgeOccupation(), p)

