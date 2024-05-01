# Suppose you have a single magical cow right now. In any given hour, this cow has a third chance of dying, a third chance of replicating into 2 magical cows, and a third chance of replicating into 3 magical cows. What is the probability that the cows do not all die out eventually?
import random

def simulate(n):
    outcomes = [-1, 1, 2]   
    remained = 0
    for sim in range(n):
        print(f"Running simulation {sim}")
        cows = 1
        for epoch in range(20):
            total = 0
            for cow in range(cows):
                result = random.choice(outcomes)
                total += result
            cows += total
            if cows <= 0:
                break
            # print(f"Epoch {epoch}: {cows}")
        if cows > 0:
            remained += 1
    return remained

rem = simulate(100)
print(f"Probability of not dying out: {rem/100}")



