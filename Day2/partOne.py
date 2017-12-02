import sys

# Convert a value to an int
def conv(x): return int(x.strip())

diffSum = 0
# Read the input (tab separated lines of numbers)
for line in sys.stdin:
    if (line == '\n'):
      # This is horrible lol
      break
    s = line.split('\t')
    # Fix the last value, which has an \n attached, and convert all chars to ints
    s = list(map(conv, s))
    diffSum += max(s) - min(s)
    print(max(s) - min(s), diffSum)

print('The answer is:', diffSum)