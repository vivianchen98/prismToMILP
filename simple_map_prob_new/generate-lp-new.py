from simple_map_prob_new import *

file = open("lp-output.txt","w+")

#define variables
for n in range(ObjNum):
    for i in range(StateNum):
        if i != StateNum-1:
            file.write("var x"+ str(i) +"_lower_obj" + str(n+1) + " >= 0;\n")
            file.write("var x"+ str(i) +"_upper_obj" + str(n+1) + " >= 0;\n")
        else:
            file.write("var x"+ str(i) +"_lower_obj" + str(n+1) + " = 0;\n")
            file.write("var x"+ str(i) +"_upper_obj" + str(n+1) + " = 0;\n")

for (s,a) in choices:
    file.write("var y"+str(s)+"_"+actions[a]+" >= 0, <= 1, binary;\n")

# define objective
sum = ""
for (s,a) in choices:
    sum += "(1-y"+str(s)+"_"+actions[a]+")+"
x_sum = ""
for n in range(ObjNum):
    x_sum += " - x0_lower_obj" + str(n+1) + " + x0_upper_obj" + str(n+1)
file.write("minimize z:  " + x_sum + " + 100*(" + sum[:-1] + ");\n")

i = 0 #constraint index

# define constraint: reachability analysis on y_s,a
for state in range(StateNum):
    in_sum = ""
    for (s,a,t) in choices_sat:
        if t == state and t != s:
            in_sum += "y"+str(s)+"_"+actions[a]+"+"
    if state == 0:
        in_sum = " 1 +"
    # print(str(state) + " " + in_sum[:-1])

    out_sum = ""
    for (s,a) in choices:
        if s == state:
            out_sum += "y"+str(s)+"_"+actions[a]+"+"
    # print(str(state) + " " + out_sum[:-1])

    file.write("subject to c"+str(i)+": 100 * (" + in_sum[:-1] + ") - (" + out_sum[:-1] + ") >= 0;\n")
    i += 1;
    file.write("subject to c"+str(i)+":  (" + in_sum[:-1] + ") - 100 * (" + out_sum[:-1] + ") <= 0;\n")
    i += 1;


# define constraint: translational relation line
for n in range(ObjNum):
    for (s,a) in choices:
        reward_sum = 0
        trans_sum = ""
        for (s_trans,a_trans,t_trans) in trans:
            if s == s_trans and a == a_trans:
                trans_sum += str(trans[(s_trans,a_trans,t_trans)]) + "* x"+str(t_trans)+"_lower_obj" + str(n+1) + " + "
        # print(trans_sum)
        for (index_r, s_r, a_r, t_r) in reward:
            if s_r == s and a_r == a and index_r == n:
                reward_sum = reward[(index_r,s_r,a_r,t_r)]
        # print(reward_sum)

        file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_lower_obj" + str(n+1) + " - 100*(1-y"+str(s)+"_"+actions[a]+") - (" + trans_sum[:-3] + ") <= " + str(reward_sum) + ";\n")
        i += 1

    for (s,a) in choices:
        reward_sum = 0
        trans_sum = ""
        for (s_trans,a_trans,t_trans) in trans:
            if s == s_trans and a == a_trans:
                trans_sum += str(trans[(s_trans,a_trans,t_trans)]) + "* x"+str(t_trans)+"_upper_obj" + str(n+1) + "  + "
        # print(trans_sum)
        for (index_r, s_r, a_r, t_r) in reward:
            if s_r == s and a_r == a and index_r == n:
                reward_sum = reward[(index_r,s_r,a_r,t_r)]
        # print(reward_sum)

        file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_upper_obj" + str(n+1) + " + 100*(1-y"+str(s)+"_"+actions[a]+") - (" + trans_sum[:-3] + ") >= " + str(reward_sum) + ";\n")
        i += 1


    # define constraint: initial state thresholds
    file.write("subject to c"+str(i)+": x0_lower_obj" + str(n+1) + " >= " + str(THRESHOLD_LOWER[n]) +";\n")
    i+= 1
    file.write("subject to c"+str(i)+": x0_upper_obj" + str(n+1) + " <= " + str(THRESHOLD_UPPER[n]) + ";\n")
    i+= 1


print("action_str = " + action_str + "\n\n")


#end
file.write("end;\n")

file.close()
