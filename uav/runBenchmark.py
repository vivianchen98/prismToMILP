import os
import re
#from parse import *
from generate_lp_benchmark import *
import time



def calculateThresholds(alpha,beta,objectives):
    print("Calculating Thresholds....")
    upperBound = []
    lowerBound = []

    matrix1 = []
    o = open("resultsLog.txt", "r")
    for line in o:
        if "[(" in line:
            newline = ""
            for c in line:
                if(c == "[" or c == "]" or c == "(" or c == ")"):
                    newline = newline
                else:
                    newline = newline + c
            newline = newline.split(",")
            for i in range(len(newline)):
                if(objectives == 2 and i%2 == 0):
                   matrix1.append([float(newline[i]),float(newline[i+1])])
    #print(matrix1)


    matrix2 = []
    for i in range(objectives):
        preLower = alpha[i] - beta[i]
        if (preLower < 0):
            preLower = 0
        preUpper = alpha[i] + beta[i]
        if (preUpper > 1):
            preUpper = 1
        matrix2.append([preLower,preUpper])
    #print(matrix2)

    ans = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    ans[i][j] += matrix1[i][k] * matrix2[k][j]

    #print(ans)


    col1Numbers = []
    col2Numbers = []
    for i in range(len(ans)):
        col1Numbers.append(ans[i][0])
        col2Numbers.append(ans[i][1])
    col1Min = min(col1Numbers)
    col2Min = min(col2Numbers)
    col1Index = col1Numbers.index(col1Min)
    col2Index = col2Numbers.index(col2Min)
    for i in range(objectives):
        if(matrix1[col1Index][i] < matrix1[col2Index][i]):
            lowerBound.append(matrix1[col1Index][i]-0.01)
            upperBound.append(matrix1[col2Index][i]+0.01)
        else:
            lowerBound.append(matrix1[col2Index][i]-0.01)
            upperBound.append(matrix1[col1Index][i]+0.01)

    #print(upperBound)
    #print(lowerBound)

    return upperBound,lowerBound

def findDestState():
    destState = []
    b = open("uav.lab", "r")
    b.readline()
    for line in b:
        tmp = line.split()
        state = tmp[0]
        state = int(state[:-1])
        for i, s in enumerate(tmp):
            if i>0:
                label = int(s)
                if label == 2:
                    destState.append(state)

    #print("These are the destination states:")
    #print(destState)

    return destState

def findPermissiveStates():
    pstates = 0
    pstatesHold = {}
    p = open("out_combined.sol", "r")
    for line in p:
        if "y" in line:
            offindex = line.index("_")
            onindex = line.index("_action")
            hold = line.split(" ")
            line = line[offindex:onindex]
            if float(hold[1]) == 1.0:
                print(hold)
                if line in pstatesHold and pstatesHold[line] == 1:
                    pstates = pstates + 1
                    pstatesHold[line] = pstatesHold[line] + 1
                elif line in pstatesHold and pstatesHold[line] > 1:
                    pstatesHold[line] = pstatesHold[line] + 1
                else:
                    print("add")
                    pstatesHold[line] = 1

    #print("These are the pstates:")
    #print(pstatesHold)
    #print("")

    return pstates

def main():
    print("BEGIN")
    if(os.path.exists("output_file.txt")):
        os.remove("output_file.txt")
    output = open("output_file.txt","w+")

    objectives = 2
    alpha = [0.1,0.9]
    beta = [0.1,0.1]
    c = 10000

    output.write("NxN Size: UAV \n")
    output.write("Objectives:"+str(objectives)+"\n")
    output.write("Preferences:"+str(alpha)+"\n")
    output.write("Uncertainty:"+str(beta)+"\n")

    # print("Calling Prism...")
    #
    # os.system("sh prism -javastack 1g uav.prism uav.props -exportmodel .tra,sta,lab -exporttransrewards uav.rew  -exportresults resultsLog.txt")
    # print("Model Files Exported (.tra, .sta, .lab, .rew)!")

    thresholdUpper,thresholdLower = calculateThresholds(alpha,beta,objectives)
    output.write("Upper Threshold:"+str(thresholdUpper)+"\n")
    output.write("Lower Threshold:"+str(thresholdLower)+"\n")

    destState = findDestState()

    countStates = len(open("uav.sta").readlines(  ))-1
    countTransitions = len(open("uav.tra").readlines(  ))-1
    output.write("MDP States:"+str(countStates)+"\n")
    output.write("MDP Transitions:"+str(countTransitions)+"\n")

    print("Generating MILP")
    start_time_overall,start_time_solve = generate_lp_script("uav",thresholdLower,thresholdUpper,destState,objectives,alpha,beta,c)
    end_time_overall = time.time()
    print("MILP Generated and Solved!")

    a = len(open("out_combined.lp").readlines(  ))
    output.write("MILP Lines:"+str(a)+"\n")

    pstates = findPermissiveStates()
    output.write("Permissive States:"+str(pstates)+"\n")

    bvaribles = 0
    rvaribles = 0
    b = open("out_combined.sol","r")
    for line in b:
        if "y" in line:
            bvaribles = bvaribles + 1
        if "x" in line:
            rvaribles = rvaribles + 1
    output.write("Binary Variables:"+str(bvaribles)+"\n")
    output.write("Real Variables:"+str(rvaribles-1)+"\n")

    output.write("Overall MILP Execution Time:"+str(end_time_overall-start_time_overall)+"\n")
    output.write("MILP Solve Execution Time:"+str(end_time_overall-start_time_solve)+"\n")
    output.write("\n")

    print("END")
    output.close()

main()
