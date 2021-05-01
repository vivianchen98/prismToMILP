import importlib
import sys
from gurobipy import *
import time
#from parsed_scaledMap import *

def callGroubi(RewardNum,thresholdLower,thresholdUpper,destState,choices,StateNum,choices_sat,InitState,trans,reward,rvalue,c):
    #[6,5,5]
    #[8,2.5,4]
    #[10,1,3]
    #[12,0,1]
    #thresholdLower = [8, 0, 1]
    #thresholdUpper = [12, 3, 4]
    #RewardNum = 3


    m = Model("example")
    #m.Params.OptimalityTol = 1e-2
    #m.Params.timeLimit = 3600.0


    # Create variables for multistrategy value at each state-action pair
    y = {}
    for (s,a) in choices:
        y[s,a] = m.addVar(vtype=GRB.BINARY, name='y_state%d_action%d' % (s, a))
        #y[s,a] = m.addVar(vtype=GRB.BINARY, name='y%d_%d' % (s, a))
    m.update()

    # Create variables for all cumulative value at each state
    x_lower = {}
    x_upper = {}
    for r in range(RewardNum):
        for i in range(StateNum):
            x_lower[r,i] = m.addVar(vtype=GRB.CONTINUOUS, name='x_reward%d_state%d_lower' % (r,i)) #changed to integer from Infinity
            x_upper[r,i] = m.addVar(vtype=GRB.CONTINUOUS, name='x_reward%d_state%d_upper' % (r,i)) #changed to integer from Infinity
            #x_lower[r,i] = m.addVar(vtype=GRB.CONTINUOUS, name='x%d_lower' % i) #changed to integer from Infinity
            #x_upper[r,i] = m.addVar(vtype=GRB.CONTINUOUS, name='x%d_upper' % i) #changed to integer from Infinity
    m.update()

#-------------------------------constraints------------------------------------------------------

    # Add constraints: enforcing at least one allowed action per state
    for s in range(StateNum):
        #print("State Number")
        #print(s)
        if (s == 0):
            #print(quicksum(y[s,a] for s,a in choices.select(s,'*')))
            m.addConstr(c * 1 >= quicksum(y[s,a] for s,a in choices.select(s,'*')))
            m.addConstr(1 <= c * quicksum(y[s,a] for s,a in choices.select(s,'*')))
        else:
            #print("In")
            #print(quicksum(y[s_,a] for s_,a,s in choices_sat.select('*', '*', s)))
            #print("Out")
            #print(quicksum(y[s,a] for s,a in choices.select(s,'*')))
            m.addConstr(c * quicksum(y[s_,a] for s_,a,s in choices_sat.select('*', '*', s)) >= quicksum(y[s,a] for s,a in choices.select(s,'*')))
            m.addConstr(quicksum(y[s_,a] for s_,a,s in choices_sat.select('*', '*', s)) <= c * quicksum(y[s,a] for s,a in choices.select(s,'*')))
    m.update()

    # Add constraints: initial state constraint
    for r in range(RewardNum):
        m.addConstr(x_lower[r, int(InitState)] >= thresholdLower[r])
        m.addConstr(x_upper[r, int(InitState)] <= thresholdUpper[r])
        for item in destState:
            m.addConstr(x_lower[r, item] == 0)
            m.addConstr(x_upper[r, item] == 0)
    #m.addConstr(x_lower[int(InitState)] >= thresholdLower)
    #m.addConstr(x_upper[int(InitState)] <= thresholdUpper)
    #m.addConstr(x_lower[destState] == 0)
    #m.addConstr(x_upper[destState] == 0)
    m.update()

    # Add constraints: transition relations
    for r in range(RewardNum):
        for (s,a) in choices:
            m.addConstr(x_lower[r,s] <= c*(1-y[s,a]) + (quicksum(x_lower[r,t] for s,a,t in trans.select(s,a,'*')) +
                                    quicksum(quicksum(rvalue[r,s,a,t] for r,s,a,t in reward.select(r,s,a,'*')) for r in range(r,r+1))))
            m.addConstr(x_upper[r,s] >= -c*(1-y[s,a]) + (quicksum(x_upper[r,t] for s,a,t in trans.select(s,a,'*')) +
                                    quicksum(quicksum(rvalue[r,s,a,t] for r,s,a,t in reward.select(r,s,a,'*')) for r in range(r,r+1))))
            #m.addConstr(x_lower[r,s] <= c*(1-y[s,a]) + (quicksum(x_lower[t] for s,a,t in trans.select(s,a,'*')) +
                                #quicksum(quicksum(rvalue[r,s,a,t] for r,s,a,t in reward.select(r,s,a,'*')) for r in range(0,1))))
            #m.addConstr(x_upper[r,s] >= -c*(1-y[s,a]) + (quicksum(x_upper[t] for s,a,t in trans.select(s,a,'*')) +
                                #quicksum(quicksum(rvalue[r,s,a,t] for r,s,a,t in reward.select(r,s,a,'*')) for r in range(0,1))))
    m.update()

#------------------------------set objective-----------------------------------------------
    StaticPenalty = quicksum(quicksum(1-y[s,a] for s,a in choices.select(s,'*')) for s in range(StateNum))
    InitValues = quicksum(-x_lower[r,int(InitState)] + x_upper[r,int(InitState)] for r in range(RewardNum))
    #m.setObjective(-x_lower[int(InitState)] + x_upper[int(InitState)] + c * StaticPenalty, GRB.MINIMIZE)
    m.setObjective(InitValues + c * StaticPenalty, GRB.MINIMIZE)

    print("----------------------")
    print(m)
    print("----------------------")
#--------------------------------do not change--------------------------------------

    m.write("out_combined.lp")
    #m.write("out_combined.mps")
    start_time_solve = time.time()
    m.optimize()


    m.write("out_combined.sol")

    # Print solution
    if m.status == GRB.status.OPTIMAL:
        m.write("out_combined.sol")

    # retrieve and print number of solutions in solution pool
    solution_pool_size = m.getAttr('SolCount')
    print ("Solution pool contains {0} solutions".format(solution_pool_size))
    #
    # if (solution_pool_size > 0):
    #
    #     # for i in range(solution_pool_size):
    #     # m.params.solutionNumber = i
    #
    #     CexStateNum = 0
    #     # print all variables with non-zero value
    #     for variable in m.getVars():
    #         value = variable.getAttr('Xn')
    #         type = variable.getAttr('VType')
    #         # if (value > 0):
    #         print("{0}: {1}".format(variable.getAttr('VarName'), value))
    #             # if (type == 'C'):
    #             #     CexStateNum += 1
    #
    # print('Number of cex sentences: %g' % m.objVal)
    # print('Number of cex states: %g' % CexStateNum)
    #print(action_str)
    #I removed the ap_str print out
    return start_time_solve

def callOnlineSolver():
    file = open("lp-output.txt","w+")
    threshold_lower = THRESHOLD_LOWER
    threshold_upper = THRESHOLD_UPPER

    #define variables
    for i in range(StateNum):
        if i != StateNum-1:
            file.write("var x"+ str(i) +"_lower >= 0;\n")
            file.write("var x"+ str(i) +"_upper >= 0;\n")
        else:
            file.write("var x"+ str(i) +"_lower = 0;\n")
            file.write("var x"+ str(i) +"_upper = 0;\n")

    for (s,a) in choices:
        file.write("var y"+str(s)+"_"+str(a)+" >= 0, <= 1, binary;\n")

    # define objective
    sum = ""
    for (s,a) in choices:
        sum += "(1-y"+str(s)+"_"+str(a)+")+"

    file.write("minimize z:  -x0_lower + x0_upper +"+str(c)+"*(" + sum[:-1] + ");\n")

    i = 0 #constraint index

    # define constraint: reachability analysis on y_s,a
    # for state in range(StateNum):
    #     sum = ""
    #     for (s,a) in choices:
    #         if s == state:
    #             sum += "y"+str(s)+str(a)+"+"
    #     # print(sum[:-1])
    #     file.write("subject to c"+str(i)+": " + sum[:-1] + ">= 1;\n")
    #     i += 1;
    for state in range(StateNum):
        in_sum = ""
        for (s_,a_,t_) in choices_sat:
            if t_ == state:
                in_sum += "y"+str(s_)+"_"+str(a_)+"+"
        if state == 0:
            in_sum = " 1 +"
        # print(str(state) + " " + in_sum[:-1])

        out_sum = ""
        for (s,a) in choices:
            if s == state:
                out_sum += "y"+str(s)+"_"+str(a)+"+"
        if(out_sum == ""):
            out_sum = "0 "

        file.write("subject to c"+str(i)+": "+str(c)+" * (" + in_sum[:-1] + ") - (" + out_sum[:-1] + ") >= 0;\n")
        i += 1;
        file.write("subject to c"+str(i)+":  (" + in_sum[:-1] + ") - "+str(c)+" * (" + out_sum[:-1] + ") <= 0;\n")
        i += 1;


    # define constraint: translational relation line
    for (s,a) in choices:
        reward_sum = 0
        trans_sum = ""
        for (s_trans,a_trans,t_trans) in trans:
            if s == s_trans and a == a_trans:
                trans_sum += str(trans[(s_trans,a_trans,t_trans)]) + "* x"+str(t_trans)+"_lower + "
        # print(trans_sum)
        for (index_r, s_r, a_r, t_r) in reward:
            if s_r == s and a_r == a:
                reward_sum += reward[(0,s_r,a_r,t_r)]
        # print(reward_sum)

        file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_lower - "+str(c)+"*(1-y"+str(s)+"_"+str(a)+") - (" + trans_sum[:-3] + ") <= " + str(reward_sum) + ";\n")
        i += 1

    for (s,a) in choices:
        reward_sum = 0
        trans_sum = ""
        for (s_trans,a_trans,t_trans) in trans:
            if s == s_trans and a == a_trans:
                trans_sum += str(trans[(s_trans,a_trans,t_trans)]) + "* x"+str(t_trans)+"_upper + "
        # print(trans_sum)
        for (index_r, s_r, a_r, t_r) in reward:
            if s_r == s and a_r == a:
                reward_sum += reward[(0,s_r,a_r,t_r)]
        # print(reward_sum)

        file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_upper + "+str(c)+"*(1-y"+str(s)+"_"+str(a)+") - (" + trans_sum[:-3] + ") >= " + str(reward_sum) + ";\n")
        i += 1


    # define constraint: initial state thresholds
    file.write("subject to c"+str(i)+": x0_lower >= " + str(threshold_lower) +";\n")
    i+= 1
    file.write("subject to c"+str(i)+": x0_upper <= " + str(threshold_upper) + ";\n")
    i+= 1


    #end
    file.write("end;\n")

    #file.close()

def generate_lp_script(modelname, thresholdLower, thresholdUpper, destState, objectives, alpha, beta, c):
    print("Parsing Model...")
    start_time_overall = time.time()
    model = modelname
    THRESHOLD_LOWER = str(thresholdLower)
    THRESHOLD_UPPER = str(thresholdUpper)

    filename_gurobi = model + ".py"
    filename_trans = model + ".tra"
    filename_labels = model + ".lab"
    filename_reward_1 = model + "1.rew" #total_step
    if(objectives == 2 or objectives == 3):
        filename_reward_2 = model + "2.rew" #risky_step
    if(objectives == 3):
        filename_reward_3 = model + "3.rew" #package_step


    file_trans = open(filename_trans,"r")
    file_labels = open(filename_labels,"r")
    file_reward_1 = open(filename_reward_1,"r") #total_step
    if(objectives == 2 or objectives == 3):
        file_reward_2 = open(filename_reward_2,"r") #risky_step
    if(objectives == 3):
        file_reward_3 = open(filename_reward_3,"r") #package_step

    StateNum = int(file_trans.readline().split()[0])

    tmp = file_labels.readline().split()

    target = []
    labels = ''
    for line in file_labels: #process content of .lab
        tmp = line.split()
        state = tmp[0]
        state = state[:-1]
        for i, s in enumerate(tmp):
            if i>0:
                svalue = int(s)
                if svalue == 0:
                    InitState = state
                elif svalue == 2:
                    target.append(state)
                    #target += state + ', '
                else:
                    labels += '(' + state + ',' + str(svalue-3) + '), '

    trans = {} # in the form of {(s,a,t): prob, ...}
    choices_str = []
    choices_sat_str = []

    actions = []
    choices = tuplelist([])
    choices_sat = tuplelist([])
    trans_dict = {} # {(s,t): a, ...}
    for line in file_trans:
        tmp = line.split()
        if(len(tmp) == 4):
            tmp.append('none')
        if(len(tmp) == 5):
            if tmp[4] not in actions:
                actions.append(tmp[4])
            a = actions.index(tmp[4])
            s = int(tmp[0])
            t = int(tmp[2])
            trans_dict[(s,t)] = a
            if (s,a) not in choices:
                choices.append((s,a))
                choices_str += '(' + tmp[0] + ',' + str(a) + '), '
            trans[(float(tmp[0]),float(a),float(tmp[2]))] = float(tmp[3])
            if (s,a,t) not in choices_sat:
                choices_sat.append((s,a,t))
                choices_sat_str.append((tmp[0],a,tmp[2]))

    ActionNum = len(actions)
    choices_str = choices_str[:-2]
    choices_sat_str = choices_sat_str[:-2]
    trans = tuplelist(trans)

    action_str = '"""'
    for i, a in enumerate(actions):
        action_str += 'action' + str(i) + ': ' + a + '  '
    action_str += '"""'

    reward = {}
    rvalue = {}
    rewards = tuplelist([])
    file_reward_1.readline()
    rewards.append("distance")
    for line in file_reward_1:
        tmp = line.split()
        s = int(tmp[0])
        t = int(tmp[2])
        a = trans_dict[(s,t)]
        reward[(0,float(tmp[0]),float(a),float(tmp[2]))] = float(tmp[3])
        rvalue[(0,float(tmp[0]),float(a),float(tmp[2]))] = float(tmp[3])

    if(objectives == 2 or objectives == 3):
        file_reward_2.readline()
        rewards.append("risk")
        for line in file_reward_2:
            tmp = line.split()
            s = int(tmp[0])
            t = int(tmp[2])
            a = trans_dict[(s,t)]
            reward[(1,int(tmp[0]),int(a),int(tmp[2]))] = float(tmp[3])
            rvalue[(1,int(tmp[0]),int(a),int(tmp[2]))] = float(tmp[3])

    if(objectives == 3):
        file_reward_3.readline()
        rewards.append("package")
        for line in file_reward_3:
            tmp = line.split()
            s = int(tmp[0])
            t = int(tmp[2])
            a = trans_dict[(s,t)]
            maxReward = -1*int(tmp[3])
            reward[(2,int(tmp[0]),int(a),int(tmp[2]))] = int(tmp[3])
            rvalue[(2,int(tmp[0]),int(a),int(tmp[2]))] = int(tmp[3])

    RewardNum = len(rewards)
    #print(reward)
    reward = tuplelist(reward)
    #print(reward)
    #print(rvalue)

    rewards_str = '"""'
    for i, r in enumerate(rewards):
        rewards_str += 'reward' + str(i) + ': ' + r + '  '
    rewards_str += '"""'

    file_trans.close()
    file_labels.close()

    #===========================================================================

    start_time_solve = callGroubi(objectives,thresholdLower,thresholdUpper,destState,choices,StateNum,choices_sat,InitState,trans,reward,rvalue,c)

    return start_time_overall,start_time_solve

def main():
    print("Generate MILP Online")