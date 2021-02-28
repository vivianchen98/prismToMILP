import sys

solution = sys.argv[1]

# instantiate filenames
states = [22, 88, 352, 792]

filenames = []
for s in states:
    for u in ['bottom', 'top']:
        filenames.append(solution + '_' + str(s) + '_3_' + u + '.sol')

# create result file
result = open('permissive_result',"w+")
for filename in filenames:
    file = open(filename, 'r')
    counter = 0
    reachable_states = {}

    s_a_ct = 0

    for line in file:
        y_label = line.split()[0]
        if y_label[0] == 'y': # count the number of enabled y_s,a
            s = y_label.split('_')[1]
            y_value = int(line.split()[1])

            if s not in reachable_states:
                reachable_states[s] = [y_value]
            else:
                reachable_states[s].append(y_value)

            counter += y_value
    print("sum of y", counter)
    result.write(filename + ': ' + str(counter) + '\n')


    total_y_num = 0
    for s in reachable_states:
        ys = reachable_states[s]
        # print(ys)
        if sum(ys) > 0:
            total_y_num += len(ys)

    print("total reachable y num", total_y_num)
    result.write('total y num for ' + filename + ': ' + str(total_y_num) + '\n')
