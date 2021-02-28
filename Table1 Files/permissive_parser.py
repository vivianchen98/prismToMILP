import sys

solution = sys.argv[1]

# instantiate filenames
states = [22, 88, 352, 792]

filenames = []
for s in states:
    for i in range(3):
        filenames.append(solution + '_' + str(s) + '_' + str(i+1) + '.sol')
filenames.remove('out_combined_792_1.sol')

# create result file
result = open('permissive_result',"w+")

for filename in filenames:
    file = open(filename, 'r')
    counter = 0

    for line in file:
        y_label = line.split()[0]
        if y_label[0] == 'y': # count the number of enabled y_s,a
            y_value = line.split()[1]
            counter += int(y_value)
    print(counter)
    result.write(filename + ': ' + str(counter) + '\n')
