file_path = 'D:\Python Projects\install\exercise files\monica.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
