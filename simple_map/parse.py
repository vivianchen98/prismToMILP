#!/usr/bin/python

import sys

model = sys.argv[1]
THRESHOLD_LOWER = sys.argv[2]
THRESHOLD_UPPER = sys.argv[3]
# pref = sys.argv[3]
# uncertainty = sys.argv[4]


filename_gurobi = model + ".py"
filename_trans = model + ".tra"
filename_labels = model + ".lab"
filename_reward_1 = model + "1.rew" #risky_step
# filename_reward_2 = model + "2.rew" #total_step

file_trans = open(filename_trans,"r")
file_labels = open(filename_labels,"r")
file_reward_1 = open(filename_reward_1,"r") #risky_step
# file_reward_2 = open(filename_reward_2,"r") #total_step

file = open(filename_gurobi,"w+")

file.write("THRESHOLD_LOWER = " + THRESHOLD_LOWER + "\n")
file.write("THRESHOLD_UPPER = " + THRESHOLD_UPPER + "\n")

StateNum = file_trans.readline().split()[0]
file.write("StateNum = " + StateNum + "\n")

tmp = file_labels.readline().split()
# print(tmp)

target = 'target = ['
labels = ''
for line in file_labels: #process content of .lab
    tmp = line.split()
    # print(tmp)
    state = tmp[0]
    state = state[:-1]
    for i, s in enumerate(tmp):
        # print(i, s)
        if i>0:
            svalue = int(s)
            if svalue == 0:
                InitState = state
            elif svalue == 2:
                target += state + ', '
            else:
                labels += '(' + state + ',' + str(svalue-3) + '), '

file.write("InitState = " + InitState + "\n")
file.write(target[:-2] + "]\n\n")

trans = 'trans = {' # in the form of {(s,a,t): prob, ...}
choices_str = 'choices = ['
actions = []
choices = []
trans_dict = {} # {(s,t): a, ...}
for line in file_trans:
    tmp = line.split()
    if tmp[4] not in actions:
        actions.append(tmp[4])
    a = actions.index(tmp[4])
    s = int(tmp[0])
    t = int(tmp[2])
    trans_dict[(s,t)] = a
    if (s,a) not in choices:
        choices.append((s,a))
        choices_str += '(' + tmp[0] + ',' + str(a) + '), '
    trans += '(' + tmp[0] + ',' + str(a) + ',' + tmp[2] + '):' + tmp[3] + ', '


file.write("ActionNum = " + str(len(actions)) + "\n")

file.write(choices_str[:-2] + "]\n\n")
file.write(trans[:-2] + "}\n")

# print action string
action_str = '"""'
for i, a in enumerate(actions):
    action_str += 'action' + str(i) + ': ' + a + '  '
action_str += '"""'
file.write("action_str = " + action_str + "\n\n")

# encode reward 1: riksy_step
# rewards = []
# rewards.append("risky_step")
# reward_1 = 'reward_1, rvalue_1 = multidict({' # in the form of {(s,t): r, ...}
# file_reward_1.readline() #ignore first line in reward transition file_trans
# for line in file_reward_1:
#     tmp = line.split()
#     reward_1 += '(' + tmp[0] + ',' + tmp[2] + '):' + tmp[3] + ', '
# file.write(reward_1[:-2] + "})\n")
# file.write("reward_1 = tuplelist(reward_1)\n\n")
#
# # encode reward 2: total_step
# rewards.append("total_step")
# reward_2 = 'reward_2, rvalue_2 = multidict({' # in the form of {(s,t): r, ...}
# file_reward_2.readline() #ignore first line in reward transition file_trans
# for line in file_reward_2:
#     tmp = line.split()
#     reward_2 += '(' + tmp[0] + ',' + tmp[2] + '):' + tmp[3] + ', '
# file.write(reward_2[:-2] + "})\n")
# file.write("reward_2 = tuplelist(reward_2)\n\n")

# encode rewards together
reward = 'reward = {'
rewards = []
# process reward 1
file_reward_1.readline()
rewards.append("dist")
for line in file_reward_1:
    tmp = line.split()
    s = int(tmp[0])
    t = int(tmp[2])
    a = trans_dict[(s,t)]
    reward += '(' + str(0) + ',' + tmp[0] + ',' + str(a) + ',' + tmp[2] + '):' + tmp[3] + ', '
# process reward 2: dist index 1
# file_reward_2.readline()
# rewards.append("total_step")
# for line in file_reward_2:
#     tmp = line.split()
#     s = int(tmp[0])
#     t = int(tmp[2])
#     a = trans_dict[(s,t)]
#     reward += '(' + str(1) + ',' + tmp[0] + ',' + str(a) + ',' + tmp[2] + '):' + tmp[3] + ', '
# write to file
file.write("RewardNum = " + str(len(rewards)) + "\n")
file.write(reward[:-2] + "}\n")

# print reward string
rewards_str = '"""'
for i, r in enumerate(rewards):
    rewards_str += 'reward' + str(i) + ': ' + r + '  '
rewards_str += '"""'
file.write("rewards_str = " + rewards_str + "\n\n")

# print preference and ambiguity values for each reward
# alpha = (0.4, 0.6)
# beta = (0.1, 0.1)
#
# alpha_str = 'alpha = ['
# beta_str = 'beta = ['
# for r in range(len(rewards)):
#     alpha_str += str(alpha[r]) + ', '
#     beta_str += str(beta[r]) + ', '
# file.write(alpha_str[:-2] + "]\n")
# file.write(beta_str[:-2] + "]\n\n")



file.close()
file_trans.close()
file_labels.close()
