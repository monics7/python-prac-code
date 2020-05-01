guest_name = ''
while guest_name != 'quit':
    guest_name = input("Enter guest name:")
    file_path = 'd:\Python Projects\install\exercise files\guest.txt'
    with open(file_path, 'a') as file_object:
        if guest_name != 'quit':
            file_object.write("\n"+guest_name)
