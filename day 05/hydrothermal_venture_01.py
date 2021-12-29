import re

#coord[0] = column
#coord[1] = row
def ver_hor(coord1, coord2): 
  return (coord1[0] == coord2[0] or coord1[1] == coord2[1])

def print_hydro(hydro): 
  for i in range(len(hydro)):
    print(hydro[i])

def mark_down(hydrothermal, coord1, coord2):  
  vertical = coord1[1] == coord2[1]
  lesser = 0
  greater = 0
    
  if (vertical):     
    lesser = coord1[0] if coord1[0] < coord2[0] else coord2[0]
    greater = coord1[0] if coord1[0] > coord2[0] else coord2[0]

    for i in range(lesser, greater + 1):                  
        hydrothermal[coord1[1]][i] += 1        
    
  else:
    lesser = coord1[1] if coord1[1] < coord2[1] else coord2[1]
    greater = coord1[1] if coord1[1] > coord2[1] else coord2[1]

    # print(lesser, greater) 
    for i in range(lesser, greater + 1):
      hydrothermal[i][coord1[0]] += 1

def counter(hydrothermal):
  counter = 0

  for i in range(len(hydrothermal)):
    for j in range(len(hydrothermal[i])):
      if (hydrothermal[i][j] > 1): counter += 1

  return counter

matrix_n = 1000
hydrothermal = []
for i in range(matrix_n):
  hydrothermal.append([])
  for j in range(matrix_n):
    hydrothermal[i].append(0)

with open('./input.txt', 'r') as f:
  #reading the drawn numbers first
  
  while True:
    coord1 = []
    coord2 = []
    line = f.readline()
    
    if (not line): break

    result = re.search(r"^(\d+),(\d+) -> (\d+),(\d+)$", line)    
    coord1.extend([int(result.group(1)), int(result.group(2))])
    coord2.extend([int(result.group(3)), int(result.group(4))])

    
    if (ver_hor(coord1, coord2)):      
      mark_down(hydrothermal, coord1, coord2)      

  print(counter(hydrothermal))