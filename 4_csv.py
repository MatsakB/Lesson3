import csv
profile = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]
with open('profile.csv', 'w', encoding = 'utf -8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimeter = ';')
    writer.writeheader()
    for user in profile:
        writer.writerow(user)