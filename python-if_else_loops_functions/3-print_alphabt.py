#!/usr/bin/python3
# Using a single loop to iterate over ASCII lowercase letters
for i in range(ord('a'), ord('z')+1):
    # Exclude 'q' and 'e'
    if chr(i) not in ['q', 'e']:
        print(chr(i), end='')
