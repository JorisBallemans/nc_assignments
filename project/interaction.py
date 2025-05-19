from strategy import Strategy

INTERACTION_MATRIX = {
    (Strategy.COOPERATIVE, Strategy.COOPERATIVE): (1, 1),
    (Strategy.COOPERATIVE, Strategy.DOMINANT): (0.5, 1.5),
    # (Strategy.COOPERATIVE, Strategy.GREEDY): (0, 2),

    (Strategy.DOMINANT, Strategy.COOPERATIVE): (1.5, 0.5),
    (Strategy.DOMINANT, Strategy.DOMINANT): (1, 1),
    # (Strategy.DOMINANT, Strategy.GREEDY): (0, 0.5),

    # (Strategy.GREEDY, Strategy.COOPERATIVE): (2, 0),
    # (Strategy.GREEDY, Strategy.DOMINANT): (0.5, 0),
    # (Strategy.GREEDY, Strategy.GREEDY): (0, 0),
}