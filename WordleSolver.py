#Link this to the file with every 5 letter word in the dictionary
def filter_words_by_length(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Print the filtered words
            for word in words:
                print(word)

                
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'FiveLetterWords.txt'
word_length = 5

filter_words_by_length(file_path)
