#Solution to Arithmetic Arranger project
#Created in Visual Studio 2019
#by Michael Green

def arithmetic_arranger(problems, solve = None):

    arranged_problems = ""
    listOfProblems = []
                                                                #Check for proper number of problems (5 or less).
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
                                                                #convert each problem string into list for analysis.
        converted_string_list = []
        dashline = ""
        converted_string_list = problem.split()
                                                                #get largest item in problem. Must be less than 5 digits.
        largest_operand = len(max(converted_string_list, key = len))
        if largest_operand > 4:
            return "Error: Numbers cannot be more than four digits."
                                                                #check sign for addtion or subtraction.
        sign = converted_string_list[1]
        if (sign != '+') and (sign != '-'):
            return "Error: Operator must be '+' or '-'."
                                                                #operands must be digits.
        try: 
            operand1 = int(converted_string_list[0])
            operand2 = int(converted_string_list[2])
        except:
            return "Error: Numbers must only contain digits."
                                                                #All error checks passed. Proceed.
                                                                #Dashed line to seperate problem and solution. 
                                                                #Length covers sign + space + largest operand.
                                                                #Add to end of problem.
        dashline = ''.join(["-"] * (largest_operand + 2))
        converted_string_list.append(dashline)
                                                                #If requested, calculate solution, add to end of problem
        if (solve == True):
            if (sign == "-"):
                solution = (operand1 - operand2)
            else:
                solution = (operand1 + operand2)
            converted_string_list.append(solution)   

        else:
            converted_string_list.append('')
                                                                #end of loop. Add problem to list. 
                                                                #Cycle through loop until all problems processed
        listOfProblems.append(converted_string_list)
                                                                #Format for printing. Use dashed line to right justify
                                                                #operand1 + 4 spaces + next operand1 + 4 spaces + ... newline
    arranged_problems += (listOfProblems[0][0]).rjust(len(listOfProblems[0][3]))
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][0]).rjust(len(listOfProblems[i][3]))
    arranged_problems += '\n'
                                                                #sign + 1 space + operand2 + 4 spaces + next sign + ... new line
    arranged_problems += (listOfProblems[0][1]) + " " + (listOfProblems[0][2]).rjust(len(listOfProblems[0][3])-2)
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][1]) + " " + (listOfProblems[i][2]).rjust(len(listOfProblems[i][3])-2)
    arranged_problems += '\n'
                                                                #dashed line + 4 spaces + next dashed line + ... 
    arranged_problems += (listOfProblems[0][3]).rjust(len(listOfProblems[0][3]))
    for i in range (1,len(problems),1):
        arranged_problems += "    "
        arranged_problems += (listOfProblems[i][3]).rjust(len(listOfProblems[i][3]))
                                                                #If applicable: new line + solution + 4 spaces + ...
    if (solve == True):
        arranged_problems += '\n'
        arranged_problems += str(listOfProblems[0][4]).rjust(len(listOfProblems[0][3]))
        for i in range (1,len(problems),1):
            arranged_problems += "    "
            arranged_problems += str(listOfProblems[i][4]).rjust(len(listOfProblems[i][3]))

    return arranged_problems