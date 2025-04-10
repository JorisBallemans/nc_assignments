from agent import Agent
from strategy import Strategy as S

def main():
    a1 = Agent(1, S.COOPERATIVE)
    print(a1)

if __name__ == "__main__":
    main()