from strategy import Strategy
from interaction import INTERACTION_MATRIX


class Agent:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.reputation = dict()
        self.food = 0
        self.positive_last_interaction = dict()      

    def __str__(self):
        return f"Agent {self.id}, strategy: {self.strategy} and persuasiveness: {self.persuasiveness:.2f}"

    def set_strategy(self, strategy : Strategy):
        self.strategy = strategy

    def set_food(self, food):
        self.food = food

    def update_reputation(self, id, d_reputation):
        if id not in self.reputation:
            self.reputation[id] = 0
        self.reputation[id] += d_reputation
        
    def update_positive_last_interaction(self, other):
        if other.strategy == Strategy.COOPERATIVE:
            self.positive_last_interaction[other.id] = True
        if other.strategy == Strategy.DOMINANT:
            self.positive_last_interaction[other.id] = False
        
    def get_positive_last_interaction(self, other):
        if other.id not in self.positive_last_interaction:
            return None
        return self.positive_last_interaction[other.id]

    def interact_with(self, other):
        food_self, food_other = INTERACTION_MATRIX[(self.strategy, other.strategy)]
      #  print(f"Agent with strategy {self.strategy} interacts with agent with strategy {other.strategy} and receives food {food_self} and {food_other} respectively")
        self.set_food(food_self)
        other.set_food(food_other)

