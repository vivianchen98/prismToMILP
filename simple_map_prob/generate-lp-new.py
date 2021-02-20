from simple_map_prob import *

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
# print(sum[:-1])
file.write("minimize z:  -x0_lower + x0_upper + 100*(" + sum[:-1] + ");\n")

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
    # print(str(state) + " " + out_sum[:-1])

    file.write("subject to c"+str(i)+": 100 * (" + in_sum[:-1] + ") - (" + out_sum[:-1] + ") >= 0;\n")
    i += 1;
    file.write("subject to c"+str(i)+":  (" + in_sum[:-1] + ") - 100 * (" + out_sum[:-1] + ") <= 0;\n")
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
            reward_sum = reward[(0,s_r,a_r,t_r)]    
    # print(reward_sum)

    file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_lower - 100*(1-y"+str(s)+"_"+str(a)+") - (" + trans_sum[:-3] + ") <= " + str(reward_sum) + ";\n")
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
            reward_sum = reward[(0,s_r,a_r,t_r)]
    # print(reward_sum)

    file.write("subject to c" + str(i) + ": " + "x"+str(s)+"_upper + 100*(1-y"+str(s)+"_"+str(a)+") - (" + trans_sum[:-3] + ") >= " + str(reward_sum) + ";\n")
    i += 1


# define constraint: initial state thresholds
file.write("subject to c"+str(i)+": x0_lower >= " + str(threshold_lower) +";\n")
i+= 1
file.write("subject to c"+str(i)+": x0_upper <= " + str(threshold_upper) + ";\n")
i+= 1


print("action_str = " + action_str + "\n\n")


#end
file.write("end;\n")

file.close()
