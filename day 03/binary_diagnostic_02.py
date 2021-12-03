lines = []

def binary_string_to_decimal(binary_list):
  result = 0

  for ele in binary_list:
    result = (result << 1) | int(ele)
  
  return result

# returns an array that contains the most common bit on the first position and the least common on the second position
# it returns [0, 0] when the number of zeros and ones are the same
def frequency(binary_list, index):
  zeros = 0
  ones = 0
  for ele in binary_list:
    if (ele[index] == '0'): zeros += 1
    elif (ele[index] == '1'): ones += 1
  
  if (zeros == ones): return [0, 0]
  elif (zeros > ones): return [0, 1]
  else: return [1, 0]

def filter_first_bit(binary_list, frequency_preference, index):
  filtered_list = []
  frequency_op = 0
  [most_common, least_common] = frequency(binary_list, index)

  if (frequency_preference == 'most_c'):
    if (most_common == least_common): frequency_op = 1
    else: frequency_op = most_common

  elif (frequency_preference == 'least_c'):
    if (most_common == least_common): frequency_op = 0
    else: frequency_op = least_common

  for ele in binary_list:
    if(int(ele[index]) == frequency_op):      
      filtered_list.append(ele)


  return filtered_list


with open('./input.txt', 'r') as f:
  lines = f.readlines()

#removing trailing '/n'
for i in range(len(lines)):
  lines[i] = lines[i].strip()

#filtering
oxigen_generator = lines
for i in range(len(lines[0])):
  oxigen_generator = filter_first_bit(oxigen_generator, 'most_c', i)

  if(len(oxigen_generator) == 1):     
    break

co2_scrubber = lines
for i in range(len(lines[0])):
  co2_scrubber = filter_first_bit(co2_scrubber, 'least_c', i)

  if(len(co2_scrubber) == 1):     
    break

oxigen_decimal = binary_string_to_decimal(oxigen_generator[0])
co2_decimal = binary_string_to_decimal(co2_scrubber[0])

print(oxigen_decimal * co2_decimal)