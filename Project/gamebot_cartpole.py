# openai's gym [game environment], numpy [matrix mult, random], sys [command line args]
import gym
import numpy
import sys
env = gym.make('CartPole-v0')


# algo 1 - play game randomly
def random_play():
    observation = env.reset()
    high_score = 0

    for i in range(10000):
        env.render()
        for _ in range(200):
            score = 0
            
            action = numpy.random.randint(2)    # random 0 or 1
            observation, reward, done, info = env.step(action)
            score += reward
            
            if done:
                break

        print("score of game"+str(i)+" : "+str(score))
        if score>=high_score:
            high_score = score

    return score


# algo 2 - random weighted parameters
def random_weighted():
    high_score = 0
    
    for i in range(10000):
        
        weights = numpy.random.rand(4) * 2 - 1  # four random numbers between -1 and 1
        score = play_episode(env, weights)
        print("score of game"+str(i)+" : "+str(score))
        
        if score >= high_score:
            high_score = score
        
        if score == 200:
            break


# algo 3 - weighted parameters improved by noise
def noisey_weighted():
    weights = numpy.random.rand(4) * 2 - 1  # four random numbers between -1 and 1 , initial random weights
    noise_scaling = 0.1
    high_score = 0
    prev_score = 0
    # add noise, play an episode, if new highscore then update, quit if perfect score achieved
    for i in range(10000):
        
        new_weights = weights + (numpy.random.rand(4) * 2 - 1) * noise_scaling    # add some noise to improve weights
        score = play_episode(env, new_weights)
        print("score of game"+str(i)+" : "+str(score))
        
        # if score<=prev_score:
        #     noise_scaling += 0.01
        # prev_score = score
                
        if score >= high_score:
            high_score = score
            weights = new_weights
 
        if score == 200:
            break


# hard coded weights
def hard_coded():
    weights = [ 0.73365729, -0.89746462, 0.22559287, -0.96368349 ]
    high_score = 0  
    
    for i in range(10000):
        
        score = play_episode(env, weights)
        print("score of game"+str(i)+" : "+str(score))


# play the game [weighted params] one time
def play_episode(env, weights):
    observation = env.reset()
    score = 0
    env.render()
    
    for _ in range(200):
        
        if numpy.matmul(weights, observation) > 0 :
            action = 0
        else:
            action = 1
        
        observation, reward, done, info = env.step(action)
        score += reward
        
        if done:
            break

    return score


if __name__ == "__main__":
    if sys.argv[1]=='1':
        random_play()
    elif sys.argv[1]=='2':
        random_weighted()
    elif sys.argv[1]=='3':
        noisey_weighted()
    elif sys.argv[1]=='4':
        hard_coded()