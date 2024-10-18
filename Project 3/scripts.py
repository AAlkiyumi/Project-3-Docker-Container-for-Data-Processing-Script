import pathlib
import socket
import sys
from collections import Counter
import re

# Initial set up for path and files
output_path = pathlib.Path("/home/output").absolute()
data_path = pathlib.Path("/home/data").absolute()

# Redirect stdout to result file
orig_stdout = sys.stdout
final_file = open(f'{output_path}/result.txt', 'w')
sys.stdout = final_file 

# Keep track of all the count of words in text files
txt_num_word = {}
largest_file = ''
max_word = 0
total_num_word = 0

print("Everything that's currently in /home/data:")
data_files = list(data_path.glob('*.txt'))
for f in data_files:
    print(f'- {f.name}')

# Process IF.txt
print("Attempting to open IF.txt...")
try:
    with open(data_path / 'IF.txt', 'r') as f:
        data = f.read()
        print("Successfully opened IF.txt")
        words = data.split()
        curr_words = len(words)
        total_num_word += curr_words
        txt_num_word['IF.txt'] = curr_words
        
        if max_word < curr_words:
            largest_file = 'IF.txt'
            max_word = curr_words
            
        # Top 3 most frequent words
        word_counts = Counter(words)
        most_common_if = word_counts.most_common(3)
        print(f'Top 3 most frequent words in IF.txt:')
        for word, count in most_common_if:
            print(f'{word}: {count}')
except FileNotFoundError:
    print("IF.txt not found.")

# Process AlwaysRememberUsThisWay.txt
print("Attempting to open AlwaysRememberUsThisWay.txt...")
try:
    with open(data_path / 'AlwaysRememberUsThisWay.txt', 'r') as f:
        data = f.read()
        print("Successfully opened AlwaysRememberUsThisWay.txt")
        
        # Handle contractions
        data = re.sub(r"(?<!\w)(I'm|can't|don't|it's|you're|we're|they're|won't|wouldn't|shouldn't|couldn't|isn't|hasn't|hadn't|wasn't|aren't|I'll|you'll|he'll|she'll|it'll|we'll|they'll|I'll|you've|he's|she's|we've|they've|I'll|you're|you'd|you'd|you're|we'd|they'd|would|wouldn't|should|shouldn't|could|couldn't|is|isn't|has|hasn't|had|hadn't|was|wasn't|are|aren't|I'll|you're|we'll|you'll|they'll|I'll)\b", r' \1', data)
        
        words = data.split()
        curr_words = len(words)
        total_num_word += curr_words
        txt_num_word['AlwaysRememberUsThisWay.txt'] = curr_words
        
        if max_word < curr_words:
            largest_file = 'AlwaysRememberUsThisWay.txt'
            max_word = curr_words
            
        # Top 3 most frequent words
        word_counts = Counter(words)
        most_common_aw = word_counts.most_common(3)
        print(f'Top 3 most frequent words in AlwaysRememberUsThisWay.txt:')
        for word, count in most_common_aw:
            print(f'{word}: {count}')
except FileNotFoundError:
    print("AlwaysRememberUsThisWay.txt not found.")

# Summary output
for idx, val in txt_num_word.items():
    print(f'{idx} has {val} words')
    
print(f'Total number of words across all files: {total_num_word}')
print(f'Largest file: {largest_file} with {max_word} words')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
print(f'Hostname: {hostname}')
print(f'IP Address: {ip_address}')

# End writing progress
sys.stdout = orig_stdout
final_file.close()

# Print out final result
with open(f'{output_path}/result.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')