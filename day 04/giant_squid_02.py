import re

matrix_n = 5
def string_to_array(string, separator, _type):
  number_array = string.split(separator)
  for i in range(len(number_array)):  
    if (_type == 'board'): number_array[i] = [int(number_array[i]), 0]
    else : number_array[i] = int(number_array[i])

  return number_array

def get_board(file_object):
  board = []
  temp = []

  for i in range(5):
    temp = file_object.readline()
    temp = temp.strip()
    temp = re.sub(' {2,}', ' ', temp)

    if (temp == ''): 
      return []
    
    board.append(string_to_array(temp, ' ', 'board'))
  
  file_object.readline()
  return board
#receives a board and then returns true for a winning board. otherwise, false
def check_winning_board(board):  
  #checking rows
  for i in range(matrix_n):
    counter = 0

    for j in range(matrix_n):
      if (board[i][j][1] == 1): counter += 1

    if (counter == matrix_n):
      return True

  #checking columns
  for j in range(matrix_n):
    counter = 0

    for i in range(matrix_n):
      if (board[i][j][1] == 1): counter += 1

    if (counter == matrix_n):
      return True

  return False

def mark_board(board, drawn_number):
  for row in board:
    for i in range(matrix_n):
      # print(f"element: [{row[i][0]}], drawn_number: [{drawn_number}]")
      if (row[i][0] == drawn_number):        
        row[i][1] = 1

def sum_unmarked(board):
  sum = 0
   
  for row in board:
    for i in range(matrix_n):
      if (row[i][1] == 0): sum += row[i][0]

  return sum

def print_board(board):
  for row in board:
    print(row)

def analyse(boards, drawn_numbers):
  for drawn_number in drawn_numbers:    
    for board in boards:
      mark_board(board, drawn_number)    
      if (check_winning_board(board)):
        if (len(boards) == 1):
          # print_board(board)
          print(f'result {sum_unmarked(board)},{drawn_number} = {sum_unmarked(board) * drawn_number}')
          return
        boards.remove(board)

        print(len(boards))

drawn_numbers = []
boards = []
with open('./input.txt', 'r') as f:
  #reading the drawn numbers first
  drawn_numbers = string_to_array(f.readline(), ',', 'drawn_numbers')
  f.readline()

  while True:
    temp = get_board(f)
    if (temp): boards.append(temp)
    else: break

analyse(boards, drawn_numbers)


