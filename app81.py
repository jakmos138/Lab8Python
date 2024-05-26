import re

# The line to be separated
line = '0,278,The Shawshank Redemption,"Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",1994-09-23,162.501,8.704,26105,,'

# Regular expression pattern to capture groups and omit quotes
pattern = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')

# Find all matches using the pattern
matches = pattern.findall(line)

# Strip spaces and quotes from matches
matches = [match.strip(' "') for match in matches]

# Print the separated groups
for match in matches:
    print(match)
