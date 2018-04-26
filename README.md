# Q-learning Robot Navigation

## Introduction

Implement the Q-Learning and Dyna-Q solutions to the reinforcement learning problem - specifically a robot navigation task.

This is Part 3 in a four-part series of **Machine Learning Algorithms for Trading**:

* [**Part 1**](https://github.com/ntrang086/ml_trading_defeat_learners): Implement the Linear Regression Learner and Decision Tree Learner and generate data that works better for one learner than the other.
* [**Part 2**](https://github.com/ntrang086/ml_trading_assess_learners): Implement Random Tree Learner, Bag learner and Insane Learner. Evaluate all the learners implemented in Parts 1 and 2.
* [**Part 3**](https://github.com/ntrang086/q_learning_robot) (this repository): Implement the Q-Learning and Dyna-Q solutions to the reinforcement learning problem.
* [**Part 4**](https://github.com/ntrang086/q_learning_trading): Implement a learning trading agent using Q-learning.


## Code and project details

* **QLearner.py** - Code for Q-learning

  * The constructor `QLearner()` reserves space for keeping track of Q[s, a] for the number of states and actions. It initializes a Q table which records and updates Q value for each action in each state.

  * `query(s_prime, r)`: keeps track of the last state s and the last action a, then uses the new information s\_prime and r to update the Q table. This function returns an integer, which is the next action to take. It chooses a random action with probability rar, and updates rar according to the decay rate radr at each step. It implements Dyna-Q if required.

  * `querysetstate(s)`: A special version of `query()` that sets the state to s, and returns an integer action according to the same rules as `query()` (including choosing a random action sometimes), but it does not execute an update to the Q-table. It also does not update rar. There are two main uses for this method: 1) To set the initial state, and 2) when using a learned policy, but not updating it.


* **testqlearner.py** - Code to test `QLearner.py` with a navigation task. Note that the Q-Learner does not need to be coded specially for this task. In fact the code doesn't need to know anything about it.

### The navigation task

The navigation task takes place in a 10 x 10 grid world. The particular environment is expressed in a CSV file of integers, where the value in each position is interpreted as follows:

	0: blank space.

	1: an obstacle.

	2: the starting location for the robot.

	3: the goal location.

	5: quicksand. 

An example navigation problem (`world01.csv`) is shown below. Following python conventions, [0,0] is upper left, or northwest corner, [9,9] lower right or southeast corner. Rows are north/south, columns are east/west.

	3,0,0,0,0,0,0,0,0,0
	0,0,0,0,0,0,0,0,0,0
	0,0,0,0,0,0,0,0,0,0
	0,0,1,1,1,1,1,0,0,0
	0,5,1,0,0,0,1,0,0,0
	0,5,1,0,0,0,1,0,0,0
	0,0,1,0,0,0,1,0,0,0
	0,0,0,0,0,0,0,0,0,0
	0,0,0,0,0,0,0,0,0,0
	0,0,0,0,2,0,0,0,0,0

In this example the robot starts at the bottom center, and must navigate to the top left. Note that a wall of obstacles blocks its path, and there is some quicksand along the left side. The objective is for the robot to learn how to navigate from the starting location to the goal with the highest total reward. We define the reward for each step as:

	-1 if the robot moves to an empty or blank space, or attempts to move into a wall

	-100 if the robot moves to a quicksand space

	1 if the robot moves to the goal space

Overall, we will assess the performance of a policy as the median reward it incurs to travel from the start to the goal (higher reward is better). We assess a learner in terms of the reward it converges to over a given number of training epochs (trips from start to goal). The problem includes **random actions**. So, for example, if the learner responds with a "move north" action, there is some probability that the robot will actually move in a different direction. For this reason, the "wise" learner develops policies that keep the robot well away from quicksand. We map this problem to a reinforcement learning problem as follows:

	State: The state is the location of the robot, it is computed (discretized) as: column location * 10 + row location.

	Actions: There are 4 possible actions, 0: move north, 1: move east, 2: move south, 3: move west.

	R: The reward is as described above.

	T: The transition matrix can be inferred from the CSV map and the actions.


## Setup

You need Python 2.7.x or 3.x, and the following packages: pandas, numpy, and scipy.

## Data

CSV files for the navigation task are located in the subdirectory `testworlds`.


## Run

To run any script file, use:

```bash
python <script.py>
```

Source: [Part 3](http://quantsoftware.gatech.edu/Machine_Learning_Algorithms_for_Trading) of [Machine Learning for Trading](http://quantsoftware.gatech.edu/Machine_Learning_for_Trading_Course) by Georgia Tech
