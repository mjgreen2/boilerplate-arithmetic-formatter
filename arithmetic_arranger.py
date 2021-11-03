def arithmetic_arranger(problems, solve=None):

    arranged_problems = ""
    listOfProblems = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        converted_string_list = []
        dashline = ""
        converted_string_list = problem.split()

        largest_operand = len(max(converted_string_list, key = len))
        if largest_operand > 4:
            return "Error: Numbers cannot be more than four digits."

        sign = converted_string_list[1]
        if (sign != '+') and (sign != '-'):
            return "Error: Operator must be '+' or '-'."

        try: 
            operand1 = int(converted_string_list[0])
            operand2 = int(converted_string_list[2])
        except:
            return "Error: Numbers must only contain digits."

        dashline = ''.join(["-"] * (largest_operand + 2))

        converted_string_list.append(dashline)

   #     arranged_problems += str(operand1).rjust(largest_operand + 2) + '\n' 
   #     arranged_problems += sign + ' ' + (str(operand2)).rjust(largest_operand) + '\n'
   #     arranged_problems += dashline.rjust(largest_operand + 2) + '\n'

        if (solve == True):
            if (sign == "-"):
                solution = (operand1 - operand2)
            else:
                solution = (operand1 + operand2)
            converted_string_list.append(solution)   

   #         arranged_problems += (str(solution).rjust(largest_operand + 2) + '\r')
        else:
            converted_string_list.append('')
   #         arranged_problems += ('\r')

        listOfProblems.append(converted_string_list)

    #operand1
    arranged_problems += (listOfProblems[0][0]).rjust(len(listOfProblems[0][3]))
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][0]).rjust(len(listOfProblems[i][3]))
    arranged_problems += '\n'

    #sign and operand2
    arranged_problems += (listOfProblems[0][1]) + " " + (listOfProblems[0][2]).rjust(len(listOfProblems[0][3])-2)
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][1]) + " " + (listOfProblems[i][2]).rjust(len(listOfProblems[i][3])-2)
    arranged_problems += '\n'

    #dashed line
    arranged_problems += (listOfProblems[0][3]).rjust(len(listOfProblems[0][3]))
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][3]).rjust(len(listOfProblems[i][3]))

    if (solve == True):
        arranged_problems += '\n'
        arranged_problems += str(listOfProblems[0][4]).rjust(len(listOfProblems[0][3]))
        for i in range (1,len(problems),1):
            arranged_problems += "    "
            arranged_problems += str(listOfProblems[i][4]).rjust(len(listOfProblems[i][3]))

    return arranged_problems