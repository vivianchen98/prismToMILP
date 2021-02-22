import os
import re
#from parse import *
from generate_lp import *
import time

#GLOBALS
eastMovements = [(1,1),(1,2),(1,3),(1,4),(3,1),(4,3)]
westMovements = [(4,2),(4,3),(5,2),(5,3),(5,4),(5,5)]
southMovements = [(1,1),(1,3),(1,5),(2,1),(2,3),(2,5),(3,2),(3,3),(3,5),(4,1),(4,4),(4,5)]

eastMovementsConnect = [(1,5),(5,5)]
southMovementsConnect = [(5,1)]

eastMovementsRisky1 = [(3,1)]
westMovementsRisky1_5 = [(4,2)]
southMovementsRisky1 = [(4,1),(4,4)]
southMovementsRisky1_5 = [(3,2)]

eastMovementsPackage = [(3,1)]
westMovementsPackage = [(4,2),(5,5)]
southMovementsPackage = [(2,1),(2,3),(3,2),(3,3),(4,1),(4,4)]

def findPackageStates(rows,cols):
    package1 = ""
    package2 = ""
    package3 = ""

    rowsAdd = int(((rows/5)))
    colsAdd = int(((cols/5)))

    for state in eastMovementsPackage:
        if(rows == 5 and state == southMovements[-1]):
            package1 = package1 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            package1 = package1 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                package1 = package1 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                package1 = package1 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == eastMovementsPackage[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #package1 = package1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                package1 = package1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in westMovementsPackage:
        if(rows == 5 and state == southMovements[-1]):
            package2 = package2 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            package2 = package2 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                package2 = package2 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                package2 = package2 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == westMovementsPackage[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #package2 = package2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                package2 = package2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in southMovementsPackage:
        if(rows == 5 and state == southMovements[-1]):
            package3 = package3 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            package3 = package3 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                package3 = package3 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                package3 = package3 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == southMovementsPackage[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #package3 = package3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                package3 = package3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    #print("Packages")
    #print(package1)
    #print(package2)
    #print(package3)
    x = package1.rfind("|")
    package1 = package1[:x]
    y = package2.rfind("|")
    package2 = package2[:y]
    a = package3.rfind("|")
    package3 = package3[:a]

    return(package1,package2,package3)

def findRiskyStates(rows,cols):
    risky1 = ""
    risky2 = ""
    risky3 = ""
    risky4 = ""

    rowsAdd = int(((rows/5)))
    colsAdd = int(((cols/5)))

    for state in eastMovementsRisky1:
        if(rows == 5 and state == southMovements[-1]):
            risky1 = risky1 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            risky1 = risky1 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                risky1 = risky1 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                risky1 = risky1 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == eastMovementsRisky1[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #risky1 = risky1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                risky1 = risky1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in westMovementsRisky1_5:
        if(rows == 5 and state == southMovements[-1]):
            risky2 = risky2 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            risky2 = risky2 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                risky2 = risky2 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                risky2 = risky2 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == westMovementsRisky1_5[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #risky2 = risky2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                risky2 = risky2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in southMovementsRisky1:
        if(rows == 5 and state == southMovements[-1]):
            risky3 = risky3 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            risky3 = risky3 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                risky3 = risky3 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                risky3 = risky3 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == southMovementsRisky1[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #risky3 = risky3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                risky3 = risky3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in southMovementsRisky1_5:
        if(rows == 5 and state == southMovements[-1]):
            risky4 = risky4 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            risky4 = risky4 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                risky4 = risky4 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                risky4 = risky4 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == southMovementsRisky1_5[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #risky4 = risky4 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                risky4 = risky4 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    #print("Risky")
    #print(risky1)
    #print(risky2)
    #print(risky3)
    #print(risky4)

    x = risky1.rfind("|")
    risky1 = risky1[:x]
    y = risky2.rfind("|")
    risky2 = risky2[:y]
    a = risky3.rfind("|")
    risky3 = risky3[:a]
    b = risky4.rfind("|")
    risky4 = risky4[:b]

    return(risky1,risky2,risky3,risky4)

def findConnectionMovements(rows,cols):
    connect1 = ""
    connect2 = ""

    if(rows == 5):
        return(connect1, connect2)

    rowsAdd = int(((rows/5)))
    colsAdd = int(((cols/5)))

    for state in eastMovementsConnect:
        connect1 = connect1 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                connect1 = connect1 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                if(state[1]+addC == cols):
                    continue
                connect1 = connect1 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                if(state == eastMovementsConnect[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    connect1 = connect1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                else:
                    connect1 = connect1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in southMovementsConnect:
        connect2 = connect2 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                connect2 = connect2 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                if(state[0]+addR == rows):
                    continue
                connect2 = connect2 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                if(state == southMovementsConnect[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    connect2 = connect2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                else:
                    connect2 = connect2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    #print("Connections")
    #print(connect1)
    #print(connect2)
    if(rows != 5):
        x = connect1.rfind("|")
        connect1 = connect1[:x]
        y = connect2.rfind("|")
        connect2 = connect2[:y]

    return(connect1,connect2)

def findOverallMovements(rows,cols):
    string1 = ""
    string2 = ""
    string3 = ""

    rowsAdd = int(((rows/5)))
    colsAdd = int(((cols/5)))

    for state in eastMovements:
        if(rows == 5 and state == eastMovements[-1]):
            string1 = string1 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            string1 = string1 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                string1 = string1 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                string1 = string1 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == eastMovements[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #string1 = string1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                string1 = string1 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in westMovements:
        if(rows == 5 and state == westMovements[-1]):
            string2 = string2 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            string2 = string2 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                string2 = string2 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                string2 = string2 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == westMovements[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #string2 = string2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                string2 = string2 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    for state in southMovements:
        if(rows == 5 and state == southMovements[-1]):
            string3 = string3 + "(r="+str(state[0])+" & c="+str(state[1])+")"
        else:
            string3 = string3 + "(r="+str(state[0])+" & c="+str(state[1])+") | "
        for i in range(1,rowsAdd):
            for j in range(1,rowsAdd):
                addR = i*5
                addC = j*5
                string3 = string3 + "(r="+str(state[0]+addR)+" & c="+str(state[1])+") | "
                string3 = string3 + "(r="+str(state[0])+" & c="+str(state[1]+addC)+") | "
                #if(state == southMovements[-1] and i == rowsAdd-1 and j == rowsAdd-1):
                    #string3 = string3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+")"
                #else:
                string3 = string3 + "(r="+str(state[0]+addR)+" & c="+str(state[1]+addC)+") | "

    #print("Overall")
    #print(string1)
    #print(string2)
    #print(string3)
    if(rows != 5):
        x = string1.rfind("|")
        string1 = string1[:x]
        y = string2.rfind("|")
        string2 = string2[:y]
        a = string3.rfind("|")
        string3 = string3[:a]

    return(string1,string2,string3)

def findDestination(rows,cols):
    row = rows
    col = cols-4
    return(row,col)

def createPrismFile(rows,cols,objectives):
    if(os.path.exists("scaled_file.prism")):
        os.remove("scaled_file.prism")
    f = open("scaled_file.prism", "a")
    f.write("mdp\n")
    f.write("\n")
    f.write("module map\n")
    f.write("\n")

    f.write("// Define Grid\n")
    f.write("r:[1.."+str(rows)+"] init 1;  // Rows\n")
    f.write("c:[1.."+str(cols)+"] init 1;  // Columns\n")
    f.write("\n")

    f.write("// Destination\n")
    row,col = findDestination(rows,cols)
    f.write("[stop] (r="+str(row)+" & c="+str(col)+") -> true;\n")
    f.write("\n")

    f.write("// Overall Movements\n")
    string1,string2,string3 = findOverallMovements(rows,cols)
    f.write("[move_east] "+string1+" -> (c'=c+1);\n")
    f.write("[move_west] "+string2+" -> (c'=c-1);\n")
    f.write("[move_south] "+string3+" -> (r'=r+1);\n")
    connect1,connect2 = findConnectionMovements(rows,cols)
    if(connect1 != ""):
        f.write("[move_east] "+connect1+" -> (c'=c+1);\n")
    if(connect2 != ""):
        f.write("[move_south] "+connect2+" -> (r'=r+1);\n")
    f.write("\n")
    f.write("endmodule\n")
    f.write("\n")

    f.write("// Labels\n")
    f.write("label \"target\" = (r="+str(row)+" & c="+str(col)+");\n")
    f.write("\n")

    if(objectives == 1 or objectives == 2 or objectives == 3):
        f.write("// Total Step Reward\n")
        f.write("rewards  \"total_step\"\n")
        f.write("[move_east] true : 1;\n")
        f.write("[move_west] true : 1;\n")
        f.write("[move_south] true : 1;\n")
        f.write("[stop] true : 0;\n")
        f.write("endrewards\n")
        f.write("\n")

    if(objectives == 1 or objectives == 2 or objectives == 3):
        f.write("// Risky Step Reward\n")
        f.write("rewards \"risky_step\"\n")
        risky1,risky2,risky3,risky4 = findRiskyStates(rows,cols)
        f.write("[move_east] "+risky1+" : 1;\n")
        f.write("[move_west] "+risky2+" : 1.5;\n")
        f.write("[move_south] "+risky3+" : 1;\n")
        f.write("[move_south] "+risky4+" : 1.5;\n")
        f.write("endrewards\n")
        f.write("\n")

    if(objectives == 3):
        f.write("// Package Step Reward\n")
        f.write("rewards \"package_step\"\n")
        package1,package2,package3 = findPackageStates(rows,cols)
        f.write("[move_east] "+package1+" : 1;\n")
        f.write("[move_west] "+package2+" : 1;\n")
        f.write("[move_south] "+package3+" : 1;\n")
        f.write("endrewards\n")
        f.write("\n")

    f.close()

def calculateThresholds(alpha,beta,objectives):
    print("Calculating Thresholds....")
    upperBound = []
    lowerBound = []

    matrix1 = []
    o = open("resultsLog.txt", "r")
    if(objectives == 1 or objectives == 2):
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
                    if(objectives == 1 and i%2 == 0):
                        matrix1.append([float(newline[i])])
                    if(objectives == 2 and i%2 == 0):
                        matrix1.append([float(newline[i]),float(newline[i+1])])
    else:
        holder = []
        connections = []
        for line in o:
            if "[(" in line:
                newline = ""
                for c in line:
                    if(c == "[" or c == "]" or c == "(" or c == ")"):
                        newline = newline
                    else:
                        newline = newline + c
                newline = newline.split(",")
                holder.append(newline)
        for i in range(len(holder[0])):
            if(i%2 == 0):
                matrix1.append([float(holder[0][i]),float(holder[0][i+1])])
                connections.append(float(holder[0][i]))
        for i in range(len(holder[1])):
            if(i%2 == 0 and float(holder[1][i]) in connections):
                for j in matrix1:
                    if(j[0] == float(holder[1][i])):
                        j.append(float(holder[1][i+1]))
        #print(matrix1)
        holdMatrix = []
        for i in matrix1:
            if(len(i) == 3):
                holdMatrix.append(i)
        matrix1 = holdMatrix

    timeLower = alpha[0] - beta[0]
    if(timeLower<0):
        timeLower = 0
    timeHigher = alpha[0] + beta[0]
    riskLower = 0
    riskHigher = 0
    packageLower = 0
    packageHigher = 0

    if(objectives == 2 or objectives == 3):
        riskLower = alpha[1] - beta[1]
        if(riskLower<0):
            riskLower = 0
        riskHigher = alpha[1] + beta[1]

    if(objectives == 3):
        packageLower = alpha[2] - beta[2]
        if(packageLower < 0):
            packageLower = 0
        packageHigher = alpha[2] + beta[2]

    totalLower = timeLower+riskLower+packageLower
    totalHigher = timeHigher+riskHigher+packageHigher
    timeLower = timeLower/totalLower
    timeHigher = timeHigher/totalHigher
    matrix2 = [[timeLower,timeHigher]]

    if(objectives == 2 or objectives == 3):
        riskLower = riskLower/totalLower
        riskHigher = riskHigher/totalHigher
        matrix2.append([riskLower,riskHigher])
    if(objectives == 3):
        packageLower = packageLower/totalLower
        packageHigher = packageHigher/totalHigher
        matrix2.append([packageLower,packageHigher])

    ans = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]

    #print(matrix1)
    #print(matrix2)
    #print(ans)

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

    #if(col1Min < col1Numbers[col2Index]):
        #lowerBound = col1Min
        #upperBound = col1Numbers[col2Index]
    #else:
        #lowerBound = col1Numbers[col2Index]
        #upperBound = col1Min

    if(matrix1[col1Index][0] < matrix1[col2Index][0]):
        lowerBound.append(matrix1[col1Index][0])
        upperBound.append(matrix1[col2Index][0])
    else:
        lowerBound.append(matrix1[col2Index][0])
        upperBound.append(matrix1[col1Index][0])
    if(matrix1[col1Index][1] < matrix1[col2Index][1]):
        lowerBound.append(matrix1[col1Index][1])
        upperBound.append(matrix1[col2Index][1])
    else:
        lowerBound.append(matrix1[col2Index][1])
        upperBound.append(matrix1[col1Index][1])
    if(matrix1[col1Index][2] < matrix1[col2Index][2]):
        lowerBound.append(matrix1[col1Index][2])
        upperBound.append(matrix1[col2Index][2])
    else:
        lowerBound.append(matrix1[col2Index][2])
        upperBound.append(matrix1[col1Index][2])

    #print(upperBound)
    #print(lowerBound)
    return upperBound,lowerBound

def findDestState():
    destState = 0
    b = open("scaled_file.tra", "r")
    for line in b:
        if "stop" in line:
            line = line.split(" ")
            destState = int(line[0])

    #print("This is the dest state:")
    #print(destState)

    return destState

def findPermissiveStates():
    pstates = 0
    pstatesHold = {}
    p = open("out_combined.sol", "r")
    for line in p:
        if "y" in line:
            offindex = line.index("_")
            hold = line.split(" ")
            line = line[1:offindex]
            if int(hold[1]) == 1:
                if line in pstatesHold and pstatesHold[line] == 1:
                    pstates = pstates + 1
                    pstatesHold[line] = pstatesHold[line] + 1
                elif line in pstatesHold and pstatesHold[line] > 1:
                    pstatesHold[line] = pstatesHold[line] + 1
                else:
                    pstatesHold[line] = 1
    return pstates

def main():
    print("BEGIN")
    if(os.path.exists("output_file.txt")):
        os.remove("output_file.txt")
    output = open("output_file.txt","w+")

    b = open("evaluationBatch.txt", "r")
    for line in b:
        if(os.path.exists("scaled_file.prism")):
            os.remove("scaled_file.prism")
        if(os.path.exists("scaled_file.tra")):
            os.remove("scaled_file.tra")
        if(os.path.exists("scaled_file.sta")):
            os.remove("scaled_file.sta")
        if(os.path.exists("scaled_file.lab")):
            os.remove("scaled_file.lab")
        if(os.path.exists("scaled_file1.rew")):
            os.remove("scaled_file1.rew")
        if(os.path.exists("scaled_file2.rew")):
            os.remove("scaled_file2.rew")
        if(os.path.exists("scaled_file3.rew")):
            os.remove("scaled_file3.rew")
        if(os.path.exists("parsed_scaledMap.py")):
            os.remove("parsed_scaledMap.py")
        if(os.path.exists("lp-output.txt")):
            os.remove("lp-output.txt")
        print("Deleted Old Files")

        if(line[0] != "#"):
            line = line.split(";")
            numberOfStates = int(line[0])
            rows = int(line[0])
            cols = int(line[0])
            objectives = int(line[1])
            alpha = line[2].split(",")
            alpha = [float(i) for i in alpha]
            beta = line[3].split(",")
            beta = [float(i) for i in beta]
            c = int(line[4])

            output.write("NxN Size:"+str(numberOfStates)+"\n")
            output.write("Objectives:"+str(objectives)+"\n")
            output.write("Preferences:"+str(alpha)+"\n")
            output.write("Uncertainty:"+str(beta)+"\n")

            print("Creating A " + str(rows) + " By " + str(cols) + " Map With " +str(objectives)+ " Objective(s).")

            #print("Enter N-Value:")
            #numberOfStates = int(input())
            #rows = numberOfStates
            #cols = numberOfStates
            #print("Enter Number of Objectives:")
            #objectives = int(input())
            #print("Enter Lower Threshold:")
            #thresholdLower = input()
            #print("Enter Upper Threshold:")
            #thresholdUpper = input()
            #print("Creating A " + str(rows) + " By " + str(cols) + " Map With " +str(objectives)+ " Objective(s).")

            createPrismFile(rows,cols,objectives)

            print("Calling Prism...")

            if(objectives == 1):
                os.system("sh prism -javastack 1g scaled_file.prism propertiesfile12.pctl -exportmodel .tra,sta,lab -exporttransrewards scaled_file.rew -exportresults resultsLog.txt")
            elif(objectives == 2):
                os.system("sh prism -javastack 1g scaled_file.prism propertiesfile12.pctl -exportmodel .tra,sta,lab -exporttransrewards scaled_file.rew -exportresults resultsLog.txt")
            else:
                os.system("sh prism -javastack 1g scaled_file.prism propertiesfile3.pctl -exportmodel .tra,sta,lab -exporttransrewards scaled_file.rew -exportresults resultsLog.txt")

            thresholdUpper,thresholdLower = calculateThresholds(alpha,beta,objectives)
            destState = findDestState()

            output.write("Upper Threshold:"+str(thresholdUpper)+"\n")
            output.write("LowerThreshold:"+str(thresholdLower)+"\n")
            print("Model Files Exported (.tra, .sta, .lab, .rew)!")
            countStates = len(open("scaled_file.sta").readlines(  ))-1
            countTransitions = len(open("scaled_file.tra").readlines(  ))-1
            output.write("MDP States:"+str(countStates)+"\n")
            output.write("MDP Transitions:"+str(countTransitions)+"\n")

            print("Generating MILP")
            start_time_overall,start_time_solve = generate_lp_script("scaled_file",thresholdLower,thresholdUpper,destState,objectives,alpha,beta,c)
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
