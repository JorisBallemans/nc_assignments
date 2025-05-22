from strategy import Strategy

INTERACTION_MATRIX = {
    (Strategy.COOPERATIVE, Strategy.COOPERATIVE): (1.25, 1.25),
    (Strategy.COOPERATIVE, Strategy.DOMINANT): (0.5, 1.5),
    # (Strategy.COOPERATIVE, Strategy.GREEDY): (0, 2),

    (Strategy.DOMINANT, Strategy.COOPERATIVE): (1.5, 0.5),
    (Strategy.DOMINANT, Strategy.DOMINANT): (0.25, 0.25),
    # (Strategy.DOMINANT, Strategy.GREEDY): (0, 0.5),

    # (Strategy.GREEDY, Strategy.COOPERATIVE): (2, 0),
    # (Strategy.GREEDY, Strategy.DOMINANT): (0.5, 0),
    # (Strategy.GREEDY, Strategy.GREEDY): (0, 0),
}
INTERACTION_MATRIX_MINORITY_DEATH = {
    (Strategy.COOPERATIVE, Strategy.COOPERATIVE): (1.75, 1.75),
    (Strategy.COOPERATIVE, Strategy.DOMINANT): (0.5, 1.5),
    # (Strategy.COOPERATIVE, Strategy.GREEDY): (0, 2),

    (Strategy.DOMINANT, Strategy.COOPERATIVE): (1.5, 0.5),
    (Strategy.DOMINANT, Strategy.DOMINANT): (0.75, 0.75),
    # (Strategy.DOMINANT, Strategy.GREEDY): (0, 0.5),

    # (Strategy.GREEDY, Strategy.COOPERATIVE): (2, 0),
    # (Strategy.GREEDY, Strategy.DOMINANT): (0.5, 0),
    # (Strategy.GREEDY, Strategy.GREEDY): (0, 0),
}