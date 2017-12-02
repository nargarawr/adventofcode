import sys

# Convert a value to an int
def conv(x): return int(x.strip())

sum = 0
# Read the input (tab separated lines of numbers)
for line in sys.stdin:
    if (line == '\n'):
      # This is horrible lol
      break
    s = line.split('\t')
    # Fix the last value, which has an \n attached, and convert all chars to ints
    s = list(map(conv, s))
    
    # This is also pretty horrible
    for v1 in s: 
      for v2 in s: 
        if ((v1 != v2) and (v1 % v2 == 0)):
          print(v1/v2)
          sum += v1/v2
          break

print('The answer is:', int(sum))