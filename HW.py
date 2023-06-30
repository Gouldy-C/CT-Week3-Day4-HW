'''
Instructions: 
You have a text file named user_records.txt which contains information about users in the following format:

FirstName LastName, Age, Country

Your task is to use Python and regular expressions (regex) to extract and print the age and country of each user.

For example, if you have a line that reads "John Doe, 25, United States", your script should print "Age: 25, Country: United States".

Some lines might be improperly formatted and do not contain all the required information. If a line doesn't conform to the required format, your script should print "Invalid record".

Use “with open()' to open the file and 'readlines()' to read all the lines.

Make use of regex groups in your pattern. The 're.compile()' function will be helpful.

Your output should look something like this:

#Age: 25, Country: United States
#Age: 30, Country: Canada
#Invalid record
#Age: 45, Country: United Kingdom
#Invalid record

-Create a function that takes in the file name and the regex pattern as arguments and prints out the results.
-Add a count for the number of valid and invalid records.
'''
import re
correct = re.compile('[A-Za-z]+ [A-Za-z]+, [0-9]{1,3}, ([A-Za-z]+ [A-Za-z]+|[A-Za-z]+)$')
age_cou = re.compile('(, [0-9]{1,3})(, ([A-Za-z]+ [A-Za-z]+|[A-Za-z]+))$')

def age_country(file_name, cor_pat, ac_pat):
    with open(file_name) as f:
        data = f.readlines()
    
    correct_lst = [cor_pat.match(x) for x in data]
    invalid_count = 0
    valid_count = 0
    
    for i in correct_lst:
        if i == None:
            invalid_count += 1
            print('Invalid record')
        else:
            valid_count += 1
            a = ac_pat.findall(i[0])
            print(f'Age: {a[0][0].strip(", ")}, Country: {a[0][1].strip(", ")}')

    print(f'Valid line(s): {valid_count}, Invalid line(s): {invalid_count}')

age_country('Homework/user_records.txt', correct, age_cou)
