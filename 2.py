# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0
def count_a_text(file_name):
    try:
        f = open(file_name)
        text = f.read()
        f.close()
        newtext = []
        for letter in text:
            if letter == 'a' or letter == 'A':
                newtext += letter
        return len(newtext)
    except IOError:
        return 0
