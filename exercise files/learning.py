file_path = 'D:\Python Projects\install\exercise files\learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        message = line.rstrip()
        message = message.replace('python', 'c')
        print(message)

# for line in lines:
#     print(line.strip())

# list_1 = file_object.readlines()
#  for lists in list_1:
#     print(lists.strip())
