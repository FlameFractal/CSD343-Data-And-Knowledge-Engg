#Wumpus World - Report - Group 26

<br>

[TOC]

<br>

## 1. Problem Statement
<br>
The gameboard environment is an `n`x`n` grid consisting of four objects - the agent (player), wumpus (deadly monster), pits, and a gold bar (objective).

The agent has to navigate around the unknown board, by moving in four compass directions, avoiding the deadly pits and wumpus, in an objective to collect the gold bar at the end. 

The agent can observe his environment with the help of boolean sensors that detect pit and wumpus in an *adjacent cells* (four compass directions including neighbouring cells in direction of movement) , and gold in the current cell.

<br>

## 2. Initial state assumptions
<br>
- Agent starts the game at cell [0,0] and it cannot contain wumpus, gold or pit.
- The wumpus, gold and pits are stationery i.e. always remain at the same one cell throughout the game
- The wumpus, gold and pits are exclusive cells i.e. no two can be in the same cell

<br>


## 3. Environment detection aids
<br>
- A stench in the current cell - indicates wumpus in one of the adjacent cells
- A breeze in the current cell - indicates pit/wormhole in one of the adjacent cells
- A glitter in the current cell - indicates gold bar in the current cell

<br>

## 4. Additional changes
<br>
- Some pits could be "indeterminable" wormholes of two types:

  - Wormholes that transport the agent to a different cell in the same board
  - Wormholes that transport the agent to a next level board's start state altogether. The agent returns to the original board on either dying or collecting the gold of the new board. 

- Each boundary cell is automatically a "determinable" wormhole to the neighbouring cell in the movement of direction and hence it cannot contain an "indeterminable" wormhole of the two types described above. 

- The new board may further contain wormholes too which gives the agent a chance to increase his score.

- The complexity of the new board will be greater than the previous where complexity is defined as the average probability of dying (based on number and position of deadly pits)


<br>

## 5. Scoring table
<br>
| Task                        | Points                                   |
| --------------------------- | ---------------------------------------- |
| Collecting the gold bar     | +1000                                    |
| Dying (monster/pit)         | -1000 (Game over if in first level board) |
| Travelling through wormhole | -50                                      |
| Using arrow                 | -10                                      |
| Moving in compass direction | -1                                       |


<br>
## 6. Group Members
<br>
1. Akanksha Jojwan
2. Saksham Rastogi
3. Samarjoy Pandit
4. Saurabh Datir
5. Vishal Gauba