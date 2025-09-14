# Assignment_1
import os
for x in range(1, 51):
    if x != 25: 
        myfile = open(f"practise/txts/txt{x}.txt", "w")
        myfile.write(f"Kareem Ashraf Mostafa => {x}\n")
        myfile.close()
    else: 
        special_file = open("practise/txts/special-text.txt", "w")
        special_file.close()

print(os.getcwd())  # Current Working Directory: "F:\GitHub\python"
print(os.path.dirname(__file__))    # Directory of this file: "F:\GitHub\python\practise"
print(os.path.basename(__file__))   # The name of the working directory
print(len(os.listdir(os.path.dirname(__file__))))   # The number of elements in the specified directory

# Assignment_2
app_file = open("practise/txts/txt1.txt", "a")
for x in range(50): app_file.write("Appended => Kareem Ashraf Mostafa\n")
app_file.close()

# Assignment_3
file = open("practise/txts/txt1.txt", "r")
file.seek(0)
print(f"Number of lines is => {len(file.readlines())}")
file.seek(0)
print(f"Number of words is => {len(file.read().split())}")
file.seek(0)
print(f"Number of chars is => {len(file.read())}")
file.seek(0)
data = file.read()
count = 0
for character in data: 
    if character == 'K': count += 1 
print(f"Number of 'K' char is => {count}")


# Assignment_4

for x in range(41, 51):
    os.remove(f"practise/txts/txt{x}.txt")


####################################################################################################
# Application_1
print(70 * '#', '\n', 10 * '*', 'App_1: File Analyzer Tool', 10 * '*')

# First, we need to write some data to the file
file = open("practise/data.txt", "w")
for x in range(50): 
    if x != 24: file.write(f"[{str(x+1).zfill(2)}]  => Kareem Ashraf Mostafa\n")
    else: file.write("[25]  => ThisIsTheLongestWord\n")
file.close()
# Second, we will read this data

def count_lines(filename):  # This function returns the number of lines in the file
    with open(f"practise/{filename}", "r") as file:
        lines = len(file.readlines())
        file.close()
    return lines
    
def count_words(filename):  # This function returns the number of words in the file
    with open(f"practise/{filename}", "r") as file:
        words = len(file.read().split())
        file.close()
    return words

def count_chars(filename): # This fucntion returns the number of characters in the file
    with open(f"practise/{filename}", "r") as file:
        chars = len(file.read())
        file.close()
    return chars

def find_longest_word(filename):    # This function returns the longest word in the file
    with open(f"practise/{filename}", "r") as file: 
        words = file.read().split()
        long = words[0]
        for word in words: 
            if len(word) > len(long): long = word
        file.close()
    return long

def gen_report(filename):   # This function displays a report of all statistics
    print(f"Number of lines: {count_lines(filename)}")
    print(f"Number of words: {count_words(filename)}")
    print(f"Number of chars: {count_chars(filename)}")
    print(f"The longest word: {find_longest_word(filename)}")
        
gen_report("data.txt")



####################################################################################################
# Application_2
print(70 * '#', '\n', 10 * '*', 'App_2: Text File Editor', 10 * '*')

def create_file(filename):
    with open(f"practise/{filename}", "w") as file: file.close()

def append_file(filename, txt):
    with open(f"practise/{filename}", "a") as file: file.write(txt); file.close()

def read_file(filename):
    with open(f"practise/{filename}", "r") as file: print(file.read()); file.close()

def srch_rplce(filename, old, new):
    with open(f"practise/{filename}", "r+") as file:
        lines = file.readlines()
        for line in lines:
            if old in line: lines[lines.index(line)] =  line[: line.index(old)] + new + line[line.index(old[-1])+1 :]
        file.truncate(0)
        file.writelines(lines)
        file.close()

def rm(filename):
    import os
    os.remove(f"practise/{filename}")

create_file('kareem.txt')
for x in range(50): append_file('kareem.txt', f"This line number ({str(x+1).zfill(2)})\n")
read_file('kareem.txt')
srch_rplce('kareem.txt', '23', '0000_0023')
read_file('kareem.txt')
rm('kareem.txt')



####################################################################################################
# Application_3 
# NOTE: This is a powerfull application
print(70 * '#', '\n', 10 * '*', 'App_3: Data Logger', 10 * '*')

def log_entry(filename, entry):     # This function appends a log to the file
    with open(f"practise/mydir/{filename}", "a") as file:
        file.write('\n' + entry)
        file.close()

def read_logs(filename):            # This function displays all logs
    with open(f"practise/mydir/{filename}", "r") as file:
        line = 0
        for log in file.readlines(): 
            line += 1
            print(f"Line({str(line).zfill(3)}): {log}")
        file.close()

def filter_logs(filename, keyword): # This function displays all logs which has this keyword
    with open(f"practise/mydir/{filename}", "r") as file:
        for log in file.readlines(): 
            if keyword in log: print(log)
        file.close()

def cls_logs(filename):             # This function clears the file
    with open(f"practise/mydir/{filename}", "w") as file: 
        file.truncate(0)
        file.close()

def export_logs(filename, format):  # This function export another log file with another format such as {CSV, JSON}
    filename, format = str(filename), str(format)
    if not format.lower() in ('csv', 'json'): print(f"{format} is an unsupported format. Only (CSV, JSON) are supported")
    else: 
        with open(f"practise/mydir/{filename}", "r") as file: 
            logs = file.readlines()     # list of logs. each log is a string
            file.close()
        # JSON Format
        if format.lower() == 'json': 
            import json
            for log in logs: 
                log_entries = log.split()
                msg = ''
                for item in log_entries[3:]:
                    msg += item + ' '
                logs[logs.index(log)] = {
                    'timestamp' : log_entries[0] + ' ' + log_entries[1], 
                    'level'     : log_entries[2], 
                    'message'   : msg
                }
            with open(f"practise/mydir/{filename.split('.')[0]}.{format.lower()}", "w") as jsonfile: 
                json.dump(logs, jsonfile, indent=4)
                jsonfile.close()
        # CSV Format
        elif format.lower() == 'csv': 
            for log in logs:
                log_entries = log.split()
                msg = ''
                for item in log_entries[3:]:
                    msg += item + ' '
                logs[logs.index(log)] = log_entries[0] + ' ' + log_entries[1] + ',' + log_entries[2] + ',' + msg + '\n' # Time stamp,level,message
            with open(f"practise/mydir/{filename.split('.')[0]}.{format.lower()}", "w") as csvfile: 
                csvfile.write("timestamp,level,message\n")
                csvfile.writelines(logs)
                csvfile.close()

def rm_log(filename, lognum):       # This function removes a log from the file
    with open(f"practise/mydir/{filename}", "a+") as file:
        file.seek(0)
        logs = file.readlines()
        if not lognum > len(logs):
            logs.pop(lognum-1)
            file.truncate(0)
            file.writelines(logs)
        else: print(f"Unexpected log number({lognum}). Total number of logs = {len(logs)}")


read_logs('output.log')
filter_logs('output.log', 'INFO')
filter_logs('output.log', 'WARNING')
filter_logs('output.log', 'ERROR')

export_logs('output.log', 'csv')
export_logs('output.log', 'json')
export_logs('output.log', 'txt')    # This is an unsupported format

log_entry('output.log', '2025-10-01 13:23:03 INFO Kareem is a good man')
export_logs('output.log', 'csv')
export_logs('output.log', 'json')

# log_entry()

# rm_log('output.log', 5)
read_logs('output.log')
export_logs('output.log', 'csv')
export_logs('output.log', 'json')
rm_log('output.log', 10)

