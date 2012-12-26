from Agent import Agent

class MonteCarloAgent(Agent):
    def __init__(self, beta = 1.0, *args, **kwargs):
        super(MonteCarloAgent, self).__init__(*args, **kwargs)
        self.beta = beta
