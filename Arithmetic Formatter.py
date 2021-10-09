def arithmetic_arranger(problems, solve=False):
    answ = ''
    fst_line = ''
    scnd_line = ''
    dash = ''

    for prbm in problems:
        prb = prbm.split(' ')
        try:
            v1 = int(prb[0])
            op = prb[1]
            v2 = int(prb[2])
            if op == "+":
                val = str(v1 + v2)
            elif op == "-":
                val = str(v1 - v2)
            v1 = str(v1)
            v2 = str(v2)
            if len(problems) > 5:
                return "Error: Too many problems."
            elif len(prb[0]) > 4 or len(prb[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif op == "*" or op == "/":
                return "Error: Operator must be '+' or '-'."
        except ValueError:
            return "Error: Numbers must only contain digits."

        length = max(len(v1), len(v2)) + 2
        upper = str(v1).rjust(length)
        middle = op + str(v2).rjust(length - 1)
        line = '-' * length
        value = str(val).rjust(length)

        if prbm is not problems[-1]:
            fst_line += upper + '    '
            scnd_line += middle + '    '
            dash += line + '    '
            answ += value + '    '

        elif prbm is problems[-1]:
            fst_line += upper
            scnd_line += middle
            dash += line
            answ += value
    if solve:
        arranged_problems = fst_line + '\n' + scnd_line + '\n' + dash + '\n' + answ
    else:
        arranged_problems = fst_line + '\n' + scnd_line + '\n' + dash
    return arranged_problems


print(arithmetic_arranger(['3801 - 2', '123 + 49']))
