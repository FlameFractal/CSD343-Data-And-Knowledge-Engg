from wumpus import *

while(gameNotOver):
    agent.FillMatrix(matrix.GetPosition(agent.linecurrent, agent.columncurrent))
    agentCell = agent.GetPosition(agent.linecurrent, agent.columncurrent)
    if agentCell.Monster:
        print("oops. monster. agent dead.")
        agent.score -= 1000
        gameNotOver = False
    elif agentCell.pit:
        print("oops. pit. agent dead.")
        agent.score -= 1000
        gameNotOver = False
    elif agentCell.Gold:
        print("\nyay. gold. agent won.")
        agent.score += 1000
        gameNotOver = False
    else:
        play()

print("\n" + str(agent.score)+" Points")