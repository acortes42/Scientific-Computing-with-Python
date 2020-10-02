def arithmetic_arranger(*problems):
    arr = "\n"
    problemLen = len(problems[0])
    problemsSplit = []

    if problemLen > 5:  
        return ("Error: Too many problems.")
    for n in range(problemLen):
        problemsSplit.insert(n, problems[0][n].split(" "))
    for num in range(problemLen):
        if len(problemsSplit[num][0]) > 4 or len(problemsSplit[num][2]) > 4:
            return("Error: Numbers cannot be more than four digits.")
        for i in range(len(problemsSplit[num][0])):
            if problemsSplit[num][0][i] < "0" or problemsSplit[num][0][i] > "9":
                return("Error: Numbers must only contain digits.")    
        if problemsSplit[num][1] != '+' and problemsSplit[num][1] != '-':
            return("Error: Operator must be '+' or '-'.")
        for i in range(len(problemsSplit[num][2])):
            if problemsSplit[num][2][i] < "0" or problemsSplit[num][2][i] > "9":
                return("Error: Numbers must only contain digits.") 

    for pl in range(problemLen):
        arr += " " * (6 - len(problemsSplit[pl][0]))
        arr += problemsSplit[pl][0] + "   "
    arr += "\n"
    for pl in range(problemLen):
        
        for n in range(6 - len(problemsSplit[pl][2])):
            if ((6 - len(problemsSplit[pl][2]) - n) == 2):
                arr += problemsSplit[pl][1]
                continue
            arr += " "
        arr += problemsSplit[pl][2] + "   "
    arr += "\n"
    for pl in range(problemLen):
        arr += "  " + "----" + "   "
    if (len(problems) == 2 and problems[1] == False):
        return arr
    arr += "\n"
    for pl in range(problemLen):
        if problemsSplit[pl][1] == "+":
            x = str(int(problemsSplit[pl][0]) + int(problemsSplit[pl][2]))
        else :
            x = str(int(problemsSplit[pl][0]) - int(problemsSplit[pl][2]))
        for n in range(6 - len(x)):
            arr += " "
        arr += x + "   "

    return arr

def main():

    print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
    return 1

if __name__ == "__main__":
    main()