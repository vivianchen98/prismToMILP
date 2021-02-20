from simple_map import *

# define decision points
decision_pts = []
unique_states = set()

for (s,a) in choices:
    if s not in unique_states:
        unique_states.add(s)
    else:
        decision_pts.append(s)
# print(decision_pts)

# write pre-decision property file
pre_decision_props = open("pre-decision.props","w+")
for dp in decision_pts:
    pre_decision_props.write("R{\"dist\"}min=? [F s=" + str(dp) + "]\n\n")
pre_decision_props.close()
# then run prism with model and pre_decision_props

# write post-decision property file
post_decision_props = open("post-decision.props","w+")
post_decision_props.write("R{\"dist\"}min=? [F \"dest\"]\n\n")
post_decision_props.write("R{\"dist\"}max=? [F \"dest\"]\n\n")
post_decision_props.close()

for dp in decision_pts:
    # modify simple_map.prism with new init state number
    model_file = open('simple_map.prism', 'r')
    lines = model_file.readlines()

    new_model_file = open("simple_map" + str(dp) + ".prism", "w+")

    for line in lines:
        if "init" in line:
            new_model_file.write("s:[0..7] init " + str(dp) + ";  // state 0 to 4")
        else:
            new_model_file.write(line)
    new_model_file.close()
    model_file.close()
# then run prism with model0 and pre_decision_props

# prism generate log files.....

cost_matrix = {0: [0, 6,12], 1: [2,6,10], 4:[5,3,5]}
#in the format of {dp: [pre_cost, min post_cost, max post_cost]}
