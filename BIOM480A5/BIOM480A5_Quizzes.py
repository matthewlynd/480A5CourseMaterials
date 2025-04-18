import random
from IPython.display import clear_output
import time
def multiple_choice(optionsDict, questionTemplate, action, num2win):
    tryagain = True
    # clear text from output and print the next question.
    num_correct = 0

    while tryagain:
        clear_output(wait=True)

        answers = list(set(optionsDict.values()))
        var = random.choice(list(optionsDict.keys()))
        type_var = optionsDict[var]
        
        question = questionTemplate.replace('XXX', var)
        print(question)

        options = random.sample(answers, 5)
        options.append(type_var)
        random.shuffle(options)
        options = list(set(options))

        for i in range(len(options)):
            print(f"{i}: {options[i]}")
        
        answer = None
        while not answer:
            answer = input(f"Choose the correct answer (0-{len(options)-1}). If you want to quit, type 'q': ")
            if answer == 'q':
                print(f"You answered {num_correct} questions correctly. Goodbye!") 
                tryagain = False
                return
            if not answer.isdigit() or int(answer) not in range(len(options)):
                print(f"Please enter a number between 0 and {len(options)-1}.")
                answer = None
        if options[int(answer)] == type_var:
            num_correct += 1
            print(f"Yay - good job! You have {num_correct} correct answers. Get {num2win} correct answers to win the game.")
            if num_correct >= num2win:
                print('\nYou won the game!\n')
                print(action)
                print('\nPlease keep going if you want to practice more.')

        else:
            print(f"I'm sorry, the correct answer is {type_var}")

        time.sleep(1)
        tryagain = input("Do you want to try again? ([y]/n): ") != 'n'
    print("Goodbye!")

def multiple_choice_quiz(quizName):
    match quizName.lower():
        case "types":
            optionsDict = {'A = 1':'int', 'B = 2.0':'float', 'C = "3"':'string', 'D = True':'bool', 'E = [1,2,3]':'list',  'F = (1,2,3)':'tuple', 'G = {1,2,3}':'set', 'H = {"a":1,"b":2,"c":3}':'dict', 'I = None':'NoneType', 'J = 1+2j':'complex', 
                    'K = 1.3':'float', 'L = 5-2j':'complex', 'M = {1:2, 3:4}':'dict', "N = {'a','b','c'}":'set', 'O = "hello"':'string', "P = ['x','y','z']":'list', "Q = ('q','r','s')":'tuple', 'R = False':'bool', 'S = None':'NoneType'}
            question = "What is the type of the following variable: XXX ?"
            action = "You got 5 right - place your left hand on your head."
            num2win = 5
        case "slicing":
            question = "How would you index or slice the the list 'x' to get XXX ?"
            optionsDict = {'the first element':'x[0]', 
                        'the last element':'x[-1]', 
                        'a list with the first 3 elements':'x[:3]', 
                        'a list with the last 3 elements':'x[-3:]', 
                        'a list with the second to the fourth element':'x[1:4]', 
                        'a list with the second to the last element':'x[1:-1]', 
                        'a list with the first element and the last element':'[x[0], x[-1]]', 
                        'a list with the last element and the second to the last element':'x[-1], x[-2]', 
                        'a list with the first 3 elements and the last 3 elements':'[x[:3], x[-3:]]', 
                        'a list with every third element starting with the first element':'x[::3]',
                        'a list with every third element starting with the second element':'x[1::3]',
                        'a reversed list with every third element starting with the last element':'x[-1::-3]',
                        'a list of every string in the list that has the letter "a"':'[i for i in x if "a" in i]',
                        'a list of every string in the list that has the letter "a" in the second position':'[i for i in x if len(i)>1 and i[1]=="a"]'}
            action = "You got 8 right - touch your nose with your right hand."
            num2win = 8
        case "list_operations":
            question = "Which command would you use to perform the following operation on the lists x, y and z:\n XXX ?"
            optionsDict = {'concatenate the lists to form a longer list':'x + y + z',
                        'repeat the list x 5 times':'x*5',
                        'remove repeated elements from the list x':'list(set(x))',
                        'sort the list x':'sorted(x)',
                        'reverse the list x':'x[::-1]',
                        'add the element 5 to the end of the list x':'x.append(5)',
                        'remove the first element from the list x':'x.pop(0)',
                        'sum the elements of the list x':'sum(x)',
                        "find the first index of the element 'abc' in the list x":'x.index("abc")',
                        'count the number of times the element 5 appears in the list x':'x.count(5)',
                        'create a new list with the summed elements of the lists x and y':'[i+j for i,j in zip(x,y)]',
                        'create a tuple with the elements of the list x':'tuple(x)',
                        'create a set with the elements of the list x':'set(x)',
                        'create a dictionary with the elements of the list x':'dict(enumerate(x))',
                        'find the intersection of the lists x and y':'list(set(x) & set(y))',
                        'find the union of the lists x and y':'list(set(x) | set(y))',
                        'find the difference of the lists x and y':'list(set(x) - set(y))',
                        'find the symmetric difference of the lists x and y':'list(set(x) ^ set(y))',
                        'check if the element 5 is in the list x':'if 5 in x',
                        'check if the element 5 is not in the list x':'if 5 not in x',
                        'check if the list x is empty':'if not x',
                        'check if the list x is not empty':'if x',
                        'check if the list x is equal to the list y':'if x==y',
                        'check if the list x is not equal to the list y':'if x!=y',
                        'check if maxiumum element of the list x is greater than 5':'if max(x)>5',
                        'check if minimum element of the list x is less than 5':'if min(x)<5',
                        'check if all elements of the list x are greater than 5':'if all(i>5 for i in x)',
                        'check if any element of the list x is greater than 5':'if any(i>5 for i in x)',
                        'check if all elements of the list x are strings':'if all(isinstance(i, str) for i in x)',
                        'check if any element of the list x is a string':'if any(isinstance(i, str) for i in x)',
                        'check if all elements of the list x are unique':'if len(x)==len(set(x))'}  
            action = "You got 12 right - look up and smile."
            num2win = 12
            
        case "dictionary_operations":
            question = "Which command would you use to perform the following operation on the lists X, Y, and Z dictionaries a, b and c:\n XXX ?"  
            optionsDict = {'create a new dictionary called using X as the keys and Y as the values':'a = dict(zip(X,Y))',
                        'extract the value of the key "abc" from the dictionary a':'a["abc"]',
                        'add the key "abc" with the value 5 to the dictionary a':'a["abc"] = 5',
                        'remove the key "abc" from the dictionary a':'a.pop("abc")',
                        'remove all elements from the dictionary a':'a.clear()',
                        'create a subset of the dictionary a with the keys in the list X':'{k:a[k] for k in X}',
                        'create a subset of the dictionary a with the values in the list Y':'{k:v for k,v in a.items() if v in Y}',
                        'create a subset of the dictionary a with the keys that contain the letter "a"':'{k:v for k,v in a.items() if "a" in k}',
                        'create a subset of the dictionary a with the values that are greater than 5':'{k:v for k,v in a.items() if v>5}',
                        'get a list of all the keys in the dictionary a':'list(a.keys())',
                        'get a list of all the values in the dictionary a':'list(a.values())',
                        'get a list of all unique values in the dictionary a':'list(set(a.values()))',
                        'get a list of all key-value pairs in the dictionary a':'list(a.items())',
                        'check if the key "abc" is in the dictionary a':'if "abc" in a',
                        'check if the key "abc" is not in the dictionary a':'if "abc" not in a',
                        'check if the value 5 is in the dictionary a':'if 5 in a.values()',
                        'check if the value 5 is not in the dictionary a':'if 5 not in a.values()',
                        'check if the dictionary a is empty':'if not a',
                        'check if the dictionary a is not empty':'if a',
                        'check if the dictionary a is equal to the dictionary b':'if a==b',
                        'check if the dictionary a is not equal to the dictionary b':'if a!=b',
                        'check if the dictionary a has the key "abc"':'if "abc" in a.keys()',
                        'check how many key-value pairs are in the dictionary a':'len(a)'}
            num2win = 10            
            action = f"You got 10 right - cough three times."

                        
        case "string_operations":
            question = "Which command would you use to perform the following operation on the strings X and/or Y:\n XXX ?"
            optionsDict = {'get the first character of the string X':'X[0]',
                        'get the last character of the string X':'X[-1]',
                        'get the first 3 characters of the string X':'X[:3]',
                        'get the last 3 characters of the string X':'X[-3:]',
                        'split the string X into a list of words separaed by spaces':'X.split()',
                        'split the string X into a list of phrases separated by commas':'X.split(",")',
                        'split the string X into a list of characters':'list(X)',
                        'join the a list Y containing words into a single string separated by spaces':'" ".join(Z)',
                        'join the a list Y containing words into a single string separated by commas':'",".join(Z)',
                        'concatenate the strings X and Y':'X + Y',
                        'count the number of times the letter "a" appears in the string X':'X.count("a")',
                        'change the string X to uppercase':'X.upper()',
                        'change the string X to lowercase':'X.lower()',
                        'change an integer x to a string':'str(x)',
                        'change a string x to an integer':'int(x)',
                        'change a string x to a float':'float(x)',
                        'count how many times the letters "aa" appear in the string X':'sum(1 for i in range(len(X)-1) if X[i:i+2]=="aa")',
                        'replace the letter "a" with the letter "b" in the string X':'X.replace("a","b")',
                        'check if the string X is equal to the string Y':'if X==Y',
                        'check if the string X is not equal to the string Y':'if X!=Y',
                        'check if the string X is in the string Y':'if X in Y',
                        'check if the string X is not in the string Y':'if X not in Y',
                        'check if the string X is empty':'if not X',
                        'check if the string X is not empty':'if X',
                        'check if the string X is a palindrome':'if X==X[::-1]',
                        'flip the order of the words in the string X':'" ".join(X.split()[::-1])',
                        'get a list of all unique words in the string X':'list(set(X.split()))',
                        'get the length of the string X':'len(X)',
                        'get the length of the string X without counting spaces':'len(X.replace(" ",""))',
                        'create a random string of length 10':'"".join(random.choices(string.ascii_letters + string.digits, k=10))',
                        'create a random string of length 10 with only letters':'"".join(random.choices(string.ascii_letters, k=10))'}
            action = "You got 15 right - knock twice on the table."
            num2win = 15

        case 'math_operations':
            question = "Which command would you use to perform the following operation on the numbers X and Y:\n XXX ?"
            optionsDict = {'add the numbers X and Y':'X + Y',
                        'subtract the number Y from X':'X - Y',
                        'multiply the numbers X and Y':'X * Y',
                        'divide the number X by Y':'X / Y',
                        'raise the number X to the power of Y':'X ** Y',
                        'find the remainder of X divided by Y':'X % Y',
                        'find the integer division of X divided by Y':'X // Y',
                        'find the square root of X':'X ** 0.5',
                        'find the absolute value of X':'abs(X)',
                        'find the maximum of X and Y':'max(X,Y)',
                        'find the minimum of X and Y':'min(X,Y)',
                        'round the number X to the nearest integer':'round(X)',
                        'round the number X to the nearest tenth':'round(X,1)',
                        'round the number X to the nearest hundredth':'round(X,2)',
                        'round the number X to the nearest thousandth':'round(X,3)',
                        'check if the number X is equal to the number Y':'if X==Y',
                        'check if the number X is not equal to the number Y':'if X!=Y',
                        'check if the number X is greater than the number Y':'if X>Y',
                        'check if the number X is less than the number Y':'if X<Y',
                        'check if the number X is greater than or equal to the number Y':'if X>=Y',
                        'check if the number X is less than or equal to the number Y':'if X<=Y',
                        'check if the number X is positive':'if X>0',
                        'check if the number X is negative':'if X<0',
                        'check if the number X is even':'if X%2==0',
                        'check if the number X is odd':'if X%2!=0',
                        'check if the number X is a prime number':'if all(X%i!=0 for i in range(2,X))',
                        'check if the number X is a multiple of Y':'if X%Y==0',
                        'check if the number X is a power of Y':'if X == Y ** round(math.log(X, Y))'}
            action = f"You got 10 right - stand up and then sit down."
            num2win = 10
        case 'string_formatting':
            question = "Which command would you use to perform the following operation on the strings X and Y:\n XXX ?"
            optionsDict = {'concatenate the strings X and Y':'X + Y',
                        'concatenate the strings X and Y with a space in between':'X + " " + Y',
                        'complete a string to include the value of the variable X':'f"Value of X is {X}"',
                        'complete a string to include the value of the variable X with 2 decimal places':'f"Value of X is {X:.2f}"',
                        'complete a string to include the values and sum of the variables X and Y':'f"Values of X and Y are {X} and {Y} and their sum is {X+Y}"',
                        'create a string will all the numbers in the list X on a single line':'" ".join(map(str,X))',
                        'create a string will all the numbers in the list X on separate lines':'"\\n".join(map(str,X))',
                        'create a string with the numbers in the list X separated by commas':'",".join(map(str,X))',
                        'create a string with the numbers in the list X separated by tabs':'"\\t".join(map(str,X))',
                        'align the string X to the left in a field of width 10':'X.ljust(10)',
                        'align the string X to the right in a field of width 10':'X.rjust(10)',
                        'center the string X in a field of width 10':'X.center(10)',
                        'fill the string X with dashes to make it 10 characters long':'X.ljust(10,"-")',
                        'convert a string X to uppercase':'X.upper()',
                        'convert a string X to lowercase':'X.lower()',
                        'capitalize the first letter of the string X':'X.capitalize()',
                        'capitalize the first letter after a space in the string X':'" ".join(i.capitalize() for i in X.split())'}
            action = "You got 10 right - touch your left ear."
            num2win = 10

        case 'importing_and_using_modules':
            question = "Which command would you use to perform the following operation on the module X:\n XXX ?"
            optionsDict = {'import the module X':'import X',
                        'import the module X and give it the alias Y':'import X as Y',
                        'import a specific function Z from the module X':'from X import Z',
                        'import all functions from the module X':'from X import *',
                        'reload the module X':'import importlib; importlib.reload(X)',
                        'check the version of the module X':'X.__version__',
                        'check the documentation of the module X':'help(X)',
                        'list the functions in the module X':'dir(X)',
                        'list the functions in the module X that start with the letter "a"':'[i for i in dir(X) if i.startswith("a")]',
                        'list the functions in the module X that contain the letter "a"':'[i for i in dir(X) if "a" in i]',
                        'list the modules in the current environment':'!pip list',
                        'list the modules in the current environment that start with the letter "a"':'!pip list | grep "^a"',
                        'list the modules in the current environment that contain the letter "a"':'!pip list | grep "a"',
                        'check if the module X is installed':'!pip show X',
                        'install the module X':'!pip install X',
                        'uninstall the module X':'!pip uninstall X',
                        'update the module X':'!pip install --upgrade X',
                        'show the current working directory':'!pwd or %pwd or os.getcwd()',
                        'change the current working directory to X':'!cd X or %cd X or os.chdir(X)',
                        'list the files in the current working directory':'!ls or %ls or os.listdir()',
                        'create a new directory called X':'!mkdir X or os.mkdir(X)',
                        'show the search path for modules':'sys.path',
                        'add a directory to the search path for modules':'sys.path.append(X)',
                        'show the user environment variables':'os.environ',
                        'show the user home directory':'os.path.expanduser("~")'}
            action = "You got 8 right - touch your palm to your forehead."
            num2win = 8
        case 'file_operations':
            question = "Which command would you use to perform the following operation on the file X:\n XXX ?"
            optionsDict = {'open the file X in read mode':'open(X, "r")',
                        'open the file X in write mode':'open(X, "w")',
                        'open the file X in append mode':'open(X, "a")',
                        'open the file X in read and write mode':'open(X, "r+")',
                        'close the file X':'X.close()',
                        'read the entire contents of the file X':'X.read()',
                        'read the first line of the file X':'X.readline()',
                        'read all lines of the file X into a list':'X.readlines()',
                        'write the string Y to the file X':'X.write(Y)',
                        'write the list Y to the file X':'X.writelines(Y)',
                        'check if the file X is closed':'X.closed',
                        'check if the file X is readable':'X.readable()',
                        'check if the file X is writable':'X.writable()',
                        'check if the file X is seekable':'X.seekable()',
                        'check if the file X is at the end':'X.seek(0,2)',
                        'move the file X cursor to the beginning':'X.seek(0)',
                        'move the file X cursor to the end':'X.seek(0,2)',
                        'move the file X cursor to the 5th byte':'X.seek(5)',
                        'move the file X cursor to the 5th line':'X.seek(0); [X.readline() for i in range(5)]',
                        'move the file X cursor to the beginning of the 5th line':'X.seek(0); [X.readline() for i in range(4)]; X.readline()',
                        'move the file X cursor to the 5th byte of the 5th line':'X.seek(0); [X.readline() for i in range(4)]; X.readline().seek(5)',
                        'move the file X cursor to the end of the 5th line':'X.seek(0); [X.readline() for i in range(4)]; X.readline().seek(0,2)',
                        'move the file X cursor to the beginning of the 5th line':'X.seek(0); [X.readline() for i in range (4)]; X.readline().seek(0)',
                        'print the contents of the file X to the screen':'print(X.read())',
                        'print the first line of the file X to the screen':'print(X.readline())',
                        'open two files X and Y and create a new file Z with the contents of both':'with open(X) as f1, open(Y) as f2: with open(Z, "w") as f3: f3.write(f1.read() + f2.read())',
                        'open the file X and read the first 5 bytes':'with open(X) as f: f.read(5)'}
            action = "You got 10 right - touch your right ear."
            num2win = 10

        case 'pandas_operations':
            question = "Which command would you use to perform the following operation on the pandas dataframe X:\n XXX ?"
            optionsDict = {'create a new dataframe with the columns A and B from the dataframe X':'X[["A","B"]]',
                        'create a new dataframe with the rows 5 to 10 from the dataframe X':'X.iloc[5:11]',
                        'create a new dataframe with the columns A and B and the rows 5 to 10 from the dataframe X':'X[["A","B"]].iloc[5:11]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is greater than 5':'X[X["A"]>5][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is greater than 5 and less than 10':'X[(X["A"]>5) & (X["A"]<10)][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is greater than 5 or less than 10':'X[(X["A"]>5) | (X["A"]<10)][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is not 5':'X[X["A"]!=5][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is in the list Y':'X[X["A"].isin(Y)][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is not in the list Y':'X[~X["A"].isin(Y)][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is null':'X[X["A"].isnull()][["A","B"]]',
                        'create a new dataframe with the columns A and B and the rows where the value in column A is not null':'X[~X["A"].isnull()][["A","B"]]',
                        'show the first 5 rows of the dataframe X':'X.head()',
                        'write the dataframe X to a csv file called Y (e.g., "Y.csv")' : 'X.to_csv(Y)',
                        'print the column names of the dataframe X':'X.columns',
                        'get the number of rows in the dataframe X':'len(X)',
                        'get the number of columns in the dataframe X':'len(X.columns)',
                        'get the numbers of rows and columns in the dataframe X':'X.shape',
                        'find out what a function "function" in the dataframe X does':'help(X.function)',
                        'print out the last 5 rows of the dataframe X':'X.tail()',
                        'load a csv file called Y (e.g., "Y.csv") into a dataframe':'pd.read_csv(Y)',
                        'import the pandas library':'import pandas as pd',
                        'create a data frame from a numpy array Z with columns A and B':'pd.DataFrame(Z, columns=["A","B"])'}
            action = "You got 10 right - turn to face to the left."
            num2win = 10

        case _:
            print("Quiz not found")
            return
    multiple_choice(optionsDict, question, action, num2win)
