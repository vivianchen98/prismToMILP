import sys

solution = sys.argv[1]

# instantiate filenames
index = [2, 3]

filenames = []
for i in index:
    filenames.append(solution + str(i) + '_table2_high.sol')
    filenames.append(solution + str(i) + '_table2_low.sol')

# print(filenames)
# filenames = ['out_combined_table1.sol', 'out_combined_teamform2_table1.sol']

# create result file
matrix = []

result = open('permissive_result',"w+")
for filename in filenames:
    print("Processing " + filename)
    file = open(filename, 'r')
    counter = 0
    reachable_states = {}

    s_a_ct = 0

    for line in file:
        y_label = line.split()[0]
        if y_label[0] == 'y': # count the number of enabled y_s,a
            s = y_label.split('_')[1]
            # print(line.split()[1])
            # print(int(round(float(line.split()[1]))))
            y_value = int(round(float(line.split()[1])))

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
    matrix.append([counter, total_y_num])

# print(matrix)

result.write("-------------------- model, enabled, reachable -------------------------\n")
i = 0
for filename in filenames:
    result.write(filename + '-' + str(matrix[i][0]) + '-' + str(matrix[i][1]) + '\n')
    i += 1
