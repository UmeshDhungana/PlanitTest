from collections import Counter

# List of people with attributes
people_list = [
               {'Name': 'Rajesh', 'Age': 27, 'Nationality': 'Nepal'},
               {'Name': 'Umesh', 'Age': 28, 'Nationality': 'Korea'},
               {'Name': 'Umesh', 'Age': 28, 'Nationality': 'Japan'},
               {'Name': 'Harry', 'Age': 21, 'Nationality': 'Japan'}
               ]

N = 25
uniqueNames = []
duplicateNames = []
ages = []
people_under_N_age = []
uniqueCountry = []

name_key_counts = Counter(p['Name'] for p in people_list)
country_key_counts = Counter(p['Nationality'] for p in people_list)
# print(name_key_counts)

for p in people_list:
    ages.append(p['Age'])
    if name_key_counts[p['Name']] == 1:
        uniqueNames.append(p)
    else:
        duplicateNames.append(p)

    if p['Age'] < N:
        people_under_N_age.append(p['Name'])

    if country_key_counts[p['Nationality']] == 1:
        uniqueCountry.append(p['Nationality'])

average_age = sum(ages)/len(people_list)

print('List of duplicates: ', duplicateNames)
print('Without Duplicates (unique list): ', uniqueNames)
print('Average Age: ', average_age)
print('People under certain (N) age: ', people_under_N_age)
print('List of Unique Countries: ', uniqueCountry)
