from strategy import Strategy
from interaction import INTERACTION_MATRIX


class Agent:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.reputation = dict()
        # self.persuasiveness = betavariate(0.5, 2)
        self.food = 0

    def __str__(self):
        return f"Agent {self.id}, strategy: {self.strategy} and persuasiveness: {self.persuasiveness:.2f}"

    def set_strategy(self, strategy : Strategy):
        self.strategy = strategy

    def set_food(self, food):
        self.food += food

    def update_reputation(self, id, d_reputation):
        if id not in self.reputation:
            self.reputation[id] = 0
        self.reputation[id] += d_reputation

    def interact_with(self, other):
        food_self, food_other = INTERACTION_MATRIX[(self.strategy, other.strategy)]
        self.set_food(food_self)
        other.set_food(food_other)

