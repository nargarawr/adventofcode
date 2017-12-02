# Get the input
captcha = input('Input the captcha:\n')

# Convert to a list of chars
c = list(str(captcha))

# Get what half of the list will be
half = int(len(c)/2)
sum = 0

# Loop through the list, if the current value is equal to the value (n/2) elements in the future (accounting for wrapping), add this value to the sum
for i, val in enumerate(c):
  index = half + i
  
  # Wrap here
  if index >= len(c):
    index = index - len(c)

  if val == c[index]:
      sum += int(val)
  
print('Your answer is:', sum)