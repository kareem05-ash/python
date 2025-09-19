"""This a script calculates Area Steal (As) or Moment (M)"""

# choose operation function
def choose():
    '''Prompt the user for his choise {op1, op2}'''
    while True:
        try:
            print("Choose Operation!")
            print("To get Moment.M, press (1): ")
            print("To get Area Steal.As, press (2): ")
            print("To Quit From The Program, Write (exit)")
            choise = input(" = Your Choise: ").strip()
            if choise.lower() == 'exit':
                return choise
            else:
                if len(choise) != 1:
                    raise IndexError
                if not choise.isdecimal():
                    raise TypeError
                if not choise in ('1', '2'):
                    raise ValueError
                choise = int(choise)
        except IndexError:
            print(f"Input must NOT exceede one character")
        except ValueError:
            print("Choose 1, or 2 only")
        except TypeError:
            print("Only decimel numbers are allowed")
        except:
            print("Some error happened")
        else:
            return choise

# calculate area steal function
def calc_area_steal():
    '''This Function Calculates & Prints The Value Of The Area Steal'''
    J = 1       # Constant Value; To Be Modified
    FY = 1      # Constant Value; To Be Modified
    M = get_data('Moment', 'Units')
    thick = get_data('Thickness', 'mm')
    clear = get_data('Clearance', 'mm')
    As = ((M * 10**5)**0.5) / (FY * (thick - clear) * J)
    # As = (x, y)
    Y = [14, 16, 18]
    print('*' * 50)
    for y in Y:
        x = (As / ((22/7) * y**2)).__ceil__()
        print(f" >> As -> ({x}, {y})")
    print('*' * 50)

# calculate moment function
def calc_moment():
    '''This Funciton Calculates & Prints The Value Of The Moment'''
    J = 1       # Constant Value; To Be Modified
    FY = 1      # Constant Value; To Be Modified
    print(" - Enter Value Of The Area Steal as: (x, y)")
    x = get_data('x', 'Units')
    y = get_data('y', 'Units')
    As = x * ((22/7) * y**2)
    thick = get_data('Thickness', 'mm')
    clear = get_data('Clearance', 'mm')
    M = (As * FY * (thick - clear) * J)**2 * 10**-5
    print('*' * 50, f"\n >> The Value Of The Moment Is: {M:_.2f}\n{'*' * 50}")

# get data input from the user
def get_data(text, units) -> str:
    '''
    This funciton takes an input data from the user and validate it
    Parameters::
        text => the name of the data input
        units=> the units to take the input in
    return::
        var => the valid data in float format
    '''
    while True:
        var = input(f" - Enter {text} In {units}: ").strip()
        try:
            if '.' in var:
                var_list = var.split('.')
                if len(var_list) != 2:
                    raise SyntaxError
                if not var_list[0].isdecimal() or not var_list[1].isdecimal():
                    raise TypeError
            else:
                if not var.isdecimal():
                    raise TypeError
            var = float(var)
        except SyntaxError:
            print("Syntax Error. Try Again!")
        except TypeError:
            print("Type Error. Try Again!")
        except:
            print("Invalid Input. Try Again!")
        else:
            return var

# User Interface Loop
while True:
    user_choise = choose()
    if user_choise == 1:
        calc_moment()
    elif user_choise == 2:
        calc_area_steal()
    elif user_choise == 'exit':
        print("Goodbuy!")
        break
