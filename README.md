###CSD343-Data-And-Knowledge-Engg - Course Labs & Project



# Project README

The goal of this project is to use reinforcement learning to build a game bot. OpenAI's Gym library is used to interface with the game.



## Video

 [Youtube Link](https://www.youtube.com/watch?v=G7Zdvnme73I).



## Game

The game used in this project is called `CartPole`. In this game, the player has to balance a rotating pole on a cart - by moving the cart left (`action=0`) or right (`action=1`)

For each time unit, that the pole stands upright, we get 1 point. Maximum points possible are 200. If the pole tips over then the game ends and the gym environment returns "done" as a value.

The game environment provides us with four observations which we can use to make our decision :
1. Cart's position

2. Cart' velocity

3. Pole's angle with the cart

4. Pole's angular velocity

   ​

## Algorithms

1. **Random** - choose the action randomly
2. **Random Weighted -** use a linear weighted combination of the four observations using random weights
3. **Noisy Weighted -** improve the weights in the second algorithm by inducing noise every time
4. **Hardcoded -** a set of weights calculated by taking mean of ten thousand successful games




## Run the project

- Install `python3`
- Install the dependencies using pip -  `gym` and `numpy`
- open a terminal and run the command `python gamebot_cartpole.py x` where x=1,2,3,4 for running one of the four algorithms