# Create a new file and write content to it
new_file = 'example.txt'
with open(new_file, 'w') as file:
    file.write('This is some content written to a new file.')

# Append more text to an existing file
existing_file = 'existing.txt'
with open(existing_file, 'a') as file:
    file.write('\nThis text is appended to an existing file.')

# Read the content from a text file
read_file = 'example.txt'
with open(read_file, 'r') as file:
    content = file.read()
    print('File Content:', content)

# Open text files with various encodings
utf8_file = 'example_utf8.txt'
with open(utf8_file, 'r', encoding='utf-8') as file:
    utf8_content = file.read()
    print('UTF-8 File Content:', utf8_content)

latin1_file = 'example_latin1.txt'
with open(latin1_file, 'r', encoding='latin-1') as file:
    latin1_content = file.read()
    print('Latin-1 File Content:', latin1_content)

# Close the opened file
file.close()