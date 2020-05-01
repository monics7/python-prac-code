def count_words(filename):
    # count the approximate number of words in a file
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # msg = "Sorry,the file "+file_name+" doesn't exist."
        # print(msg)
        pass
    else:
        # Count number of words in text file
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words")
file_names = ['alice.txt','monica.txt','john.txt','parbi.txt']
for file_name in file_names:
    count_words(file_name)
