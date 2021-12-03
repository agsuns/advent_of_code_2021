lines = []

def binary_list_to_decimal(binary_list):
  result = 0

  for ele in binary_list:
    result = (result << 1) | ele
  
  return result

def frequency(binary_list, index):
  zeros = 0
  ones = 0
  for ele in binary_list:
    if (ele[index] == '0'): zeros += 1
    elif (ele[index] == '1'): ones += 1
  
  return [0, 1] if zeros > ones else [1, 0]

with open('./input.txt', 'r') as f:
  lines = f.readlines()

#removing trailing '/n'
for i in range(len(lines)):
  lines[i] = lines[i].strip()

binary_length = len(lines[0])
gama = [0] * binary_length
epsilon = [0] * binary_length

for i in range(binary_length):
  [most_common, least_common] = frequency(lines, i)
  gama[i] = most_common
  epsilon[i] = least_common

gama_decimal = binary_list_to_decimal(gama)
epsilon_decimal = binary_list_to_decimal(epsilon)

print(gama_decimal * epsilon_decimal)

