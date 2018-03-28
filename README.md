# Machine Learning Algorithms for Trading (Part 3)

## Implement the Q-Learning and Dyna-Q solutions to the reinforcement learning problem.

Major files:

**1) QLearner.py**

* The constructor `QLearner()` reserves space for keeping track of Q[s, a] for the number of states and actions. It initializes a Q table which records and updates Q value for each action in each state.

* `query(s_prime, r)`: keeps track of the last state s and the last action a, then uses the new information s\_prime and r to update the Q table. This function returns an integer, which is the next action to take. It chooses a random action with probability rar, and updates rar according to the decay rate radr at each step. It implements Dyna-Q if required.

* `querysetstate(s)`: A special version of `query()` that sets the state to s, and returns an integer action according to the same rules as `query()` (including choosing a random action sometimes), but it does not execute an update to the Q-table. It also does not update rar. There are two main uses for this method: 1) To set the initial state, and 2) when using a learned policy, but not updating it.


**2) testqlearner.py**: contains code to test `QLearner` with a navigation task. The navigation task takes place in a 10 x 10 grid world. The particular environment is expressed in a CSV file of integers. CSV files are located in the directory testworlds.


## Setup

You need Python 2.7.x or 3.x, and the following packages: pandas, numpy, and scipy.


## Run

To run any script file, use:

```bash
python <script.py>
```

Source: [Part 3](http://quantsoftware.gatech.edu/Machine_Learning_Algorithms_for_Trading) of [Machine Learning for Trading](http://quantsoftware.gatech.edu/Machine_Learning_for_Trading_Course) by Georgia Tech
