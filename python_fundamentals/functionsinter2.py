x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].
# print(x)
# print(x[0])
# print(x[1])
# print(x[1][0])
x[1][0] = 15
print(x)
# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
print(students)
students[0]['last_name'] = 'bryant'
print(students)
# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
# For z, how would you change the value 20 to 30?
z[0]['y'] = 30
print(z)

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(dict_name):
    for x in students:
        print(
            "first_name- {} ,last_name- {}".format(x['first_name'], x['last_name']))


iterateDictionary(students)
# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output


def iterateDictionary2(key, dict_name):
    for x in students:
        print(x['first_name'])


iterateDictionary2('first_name', students)

# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printDojoInfo():
    count = 0
    for x in dojo["locations"]:
        print(x)
        count += 1
    print(count, "locations")
    count = 0
    for y in dojo["instructors"]:
        print(y)
        count += 1
    print(count, "instructors")


printDojoInfo()

# for data in students:
#     print(data)
# for key in students[0].keys():
#     print(key)
# for val in students[0].values():
#     print(val)


# def iterateDictionary(students):
#     for i in range(len(students)):
#        # for j in students[i].items():
#             print(key, " - ", val)


# # ram - HardCoded solution
# for data in students:
#     print("first_name -", data['first_name'],
#           ", last_Name -", data['last_name'])

# # ram - without hardcoding using keys
# k = []
# for data in students:
#     for key in data.keys():
#         k.append(key)
#     print(k[0], "-", data[k[0]], ",", k[1], data[k[1]])
#     k.clear()

# # ram - without hardcoding using items
# k = []
# for data in students:
#     for key, val in data.items():
#         k.append(key + "-" + val)
#     print(k[0], ",", k[1])
#     k.clear()


# print(keys, data['first_name'],
#       ",", keys, "-", data['last_name'])

# for data in students:
#     for keys in data.keys():
#         print(keys)

# iterateDictionary(students)
# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in
# that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output


# def iterateDictionary2(key, dict_name):
#     for i in range(0, len(students), 1):
#         for key in students[i].keys():
#             print (value)
# for val in students[1].values():
#     print(val)

# iterateDictionary2('first_name', students)
