def get_info():
    with open("input.txt", "r") as file:
        data = file.readlines()

    report = []
    for line in data:
         report.append(line.strip().split(" "))
    
    return report

def solution1(report):
    
    safety = []
    unsafe = inc = dec = 0

    for level in report:
        for lvl in range(len(level) - 1):            
            if abs(int(level[lvl]) - int(level[lvl + 1])) > 3:
                unsafe += 1   
                break    
            if int(level[lvl]) < int(level[lvl + 1]):
                inc += 1
            elif int(level[lvl]) > int(level[lvl + 1]):
                dec += 1
                   
        if not unsafe:
            if inc == len(level) - 1 or dec == len(level) - 1:
                 safety.append(level)

        unsafe = inc = dec = 0        

    return len(safety)

def solution2(report):
    
    new_report = []
    safe = 0

    for level in report:
        teste = level.copy()
        for i in range(len(level)): 
            teste.pop(i)
            new_report.append(teste)
            teste = level.copy()

        if solution1(new_report) > 0:
            safe += 1
        new_report = []
    
    return(safe)

report = get_info()
print(f"Safe: {solution1(report)}")
print(f"Problem Dampener: {solution2(report)}")