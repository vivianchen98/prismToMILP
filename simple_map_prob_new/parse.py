#!/usr/bin/python
import sys

# read in model name and the number of objectives
model = sys.argv[1]
ObjNum = int(sys.argv[2])
# read in thresholds for each objectives
THRESHOLD_LOWER = []
THRESHOLD_UPPER = []
for i in range(ObjNum):
    THRESHOLD_LOWER.append(sys.argv[3+2*i])
    THRESHOLD_UPPER.append(sys.argv[4+2*i])


filename_gurobi = model + ".py"
filename_trans = model + ".tra"
filename_labels = model + ".lab"
filename_reward_1 = model + "1.rew" #risky_step
filename_reward_2 = model + "2.rew" #total_step

file_trans = open(filename_trans,"r")
file_labels = open(filename_labels,"r")
file_reward_1 = open(filename_reward_1,"r") #risky_step
file_reward_2 = open(filename_reward_2,"r") #total_step

file = open(filename_gurobi,"w+")

StateNum = file_trans.readline().split()[0]
file.write("StateNum = " + StateNum + "\n")
file.write("ObjNum = " + str(ObjNum) + "\n")

# print thresholds, StateNum, InitState, target to data structure file
threshold_lower_str = "THRESHOLD_LOWER = ["
for t in THRESHOLD_LOWER:
    threshold_lower_str += t + ', '
file.write(threshold_lower_str[:-2]+']\n')

threshold_upper_str = "THRESHOLD_UPPER = ["
for t in THRESHOLD_UPPER:
    threshold_upper_str += t + ', '
file.write(threshold_upper_str[:-2]+']\n\n')


tmp = file_labels.readline().split()

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

# output state-action pairs, s-a-t pairs, transitions, actions, rewards to data structure file
trans = 'trans = {' # in the form of {(s,a,t): prob, ...}
choices_str = 'choices = ['
choices_sat_str = 'choices_sat = ['

actions = []
choices = []
choices_sat = []
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
    if (s,a,t) not in choices_sat:
        choices_sat.append((s,a,t))
        choices_sat_str += '(' + tmp[0] + ',' + str(a) + ',' + tmp[2] + ')' + ', '


file.write("ActionNum = " + str(len(actions)) + "\n")
# print actions
actions_str = 'actions = ['
for a in actions:
    actions_str += '"' + a + '"' + ', '
file.write(actions_str[:-2] + "]\n")
# print action string
action_str = '"""'
for i, a in enumerate(actions):
    action_str += 'action' + str(i) + ': ' + a + '  '
action_str += '"""'
file.write("action_str = " + action_str + "\n\n")


file.write(choices_str[:-2] + "]\n\n")
file.write(choices_sat_str[:-2] + "]\n\n")
file.write(trans[:-2] + "}\n\n")

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
file_reward_2.readline()
rewards.append("risk")
for line in file_reward_2:
    tmp = line.split()
    s = int(tmp[0])
    t = int(tmp[2])
    a = trans_dict[(s,t)]
    reward += '(' + str(1) + ',' + tmp[0] + ',' + str(a) + ',' + tmp[2] + '):' + tmp[3] + ', '
# write to file
file.write("RewardNum = " + str(len(rewards)) + "\n")
file.write(reward[:-2] + "}\n")

# print reward string
rewards_str = '"""'
for i, r in enumerate(rewards):
    rewards_str += 'reward' + str(i) + ': ' + r + '  '
rewards_str += '"""'
file.write("rewards_str = " + rewards_str + "\n\n")


file.close()
file_trans.close()
file_labels.close()
