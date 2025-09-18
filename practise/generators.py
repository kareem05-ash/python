# This File Contains Applications On Generators In Python

###########################################################################################
# App_1: Lazy File Reading
print('*' * 20, "# App_1: Lazy File Reading", '*' * 20)
def log_parser(path, keyword): 
    with open(f"{path}", 'r') as file:
        for count, line in enumerate(file.readlines()):
            if keyword in line: yield (count, line)
        file.close()

ERROR = log_parser("F:\GitHub\python\practise\mydir\mylog.log", "ERROR")
CRITICAL = log_parser("F:\GitHub\python\practise\mydir\mylog.log", "CRITICAL")
WARNING = log_parser("F:\GitHub\python\practise\mydir\mylog.log", "WARNING")

print('-' *10)
for n, error in ERROR: print(f"Error In Line_{n+1}: {error}")
print('-' *10)
for n, critical in CRITICAL: print(f"Critical In Line_{n+1}: {critical}")
print('-' *10)
for n, warning in WARNING: print(f"Warning In Line_{n+1}: {warning}")
print('-' *10)
###########################################################################################
# App_2: Infinite Sequence Generator
print('*' * 20, "# App_2: Infinite Sequence Generator", '*' * 20)
def gen_fibo():
    q_1, q_2 = 1, 0
    yield q_2; yield q_1
    while True: 
        q = q_1 + q_2
        yield q
        q_1, q_2 = q, q_1

fibo = gen_fibo()
for _ in range(15): print(next(fibo))
##########################################################################################