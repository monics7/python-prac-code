student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}
print(student)
print(student['name'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))
student['phone'] = '555-555'
print(student)
student.update({'name': 'Jane', 'age': 26, 'phone': '666-666'})
print(student)
del student['age']
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)
