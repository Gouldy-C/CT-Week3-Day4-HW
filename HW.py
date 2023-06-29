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


def age_country(file_name):
    with open(file_name) as f:
        data = f.readlines()

    correct = re.compile(
        '[A-Za-z]+ [A-Za-z]+, [0-9]{1,3}, ([A-Za-z]+ [A-Za-z]+|[A-Za-z]+)$')
    age = re.compile(', [0-9]{1,3}')
    country = re.compile(', ([A-Za-z]+ [A-Za-z]+|[A-Za-z]+)$')

    correct_lst = [correct.match(x) for x in data]

    for i in correct_lst:
        if i == None:
            print('Invalid record')
        else:
            a = age.search(i[0])
            c = country.search(i[0])
            print(f'Age: {a[0].strip(", ")}, Country: {c[0].strip(", ")}')


age_country('Homework/user_records.txt')
