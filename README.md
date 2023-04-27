# tic_tac_toe_python
The game of Tic Tac Toe using Object Oriented Programming - Python 

```
class Board():
  ''' 
  rows, cols = (5, 5)
  arr = [[' ']*cols]*rows
  print(arr)
  '''

  def __init__(self):
    matrix = []
    for i in range(3):
      a = []
      for j in range(3):
        a.append(' ')
      matrix.append(a)
    # self.grid = [[' '] * 3] * 3
    self.grid = matrix
    self.nextPlayer = 'X'
    self.moves = 9

  def Update(self, x, y):
    # print('Inside Update.........')
    if x < 0 or x > 2 or y < 0 or y > 2:
      return None, 'Invalid grid position'
    if self.grid[x][y] != ' ':
      return None, f'position already occupied by {self.grid[x][y]}'

    # print(self)
    # print('Updating the grid......' + str(x) + " " + str(y))
    self.grid[x][y] = self.nextPlayer
    # print(self)

    self.moves = self.moves - 1
    if not self.win() and self.moves == 0:
      return 'draw', None

    if self.win():
      return 'win', None
    self.nextPlayer = 'X' if self.nextPlayer == 'O' else 'O'
    return None, None
    

  def win(self):
    char = self.nextPlayer
    # Loop through the rows and check if teh count of the 'X' or 'O' is three
    for i in range(len(self.grid)):
      count = 0
      for j in range(len(self.grid[0])):
        if self.grid[i][j] == char:
          count += 1
      if count == 3:
        print('Found a row')
        return True
    # Loop through the columns and check if teh count of the 'X' or 'O' is three
    for i in range(len(self.grid[0])):
      count = 0
      for j in range(len(self.grid)):
        if self.grid[j][i] == char:
          count += 1
      if count == 3:
        print('Found a col')
        return True
    # go through giagonal 1
    for i in range(len(self.grid)):
      count = 0
      for j in range(len(self.grid[0])):
        if i == j and self.grid[j][i] == char:
          count += 1
      if count == 3:
        print('Found a diagonal +')
        return True
    # go through diagonal 2
    for i in range(len(self.grid)):
      count = 0
      for j in range(len(self.grid[0]) - 1, -1, -1):
        if i == j and self.grid[j][i] == char:
          count += 1
      if count == 3:
        print('Found a diagonal -')
        return True
    # print('Game still on...')
    return False

  def __str__(self):
    output = ''
    for row in self.grid:
      for ch in row:
        output += ch
        output += ' '
      output += '\n     \n'

    return output


class Game():

  def __init__(self):
    self.board = Board()

  def main(self):
    while (1):
      self.GetInput()

  def GetInput(self):
    # print(self.board)
    self.DisplayOutPut('Turn For : ' + self.board.nextPlayer)
    x = input('Please enter the x grid position')
    y = input('Please enter the y grid position')

    return1, return2 = self.board.Update(int(x), int(y))
    print(self.board)
    if return1 is None:
      self.DisplayOutPut(return2)
    else:
      if return1 == 'win' or return1 == 'draw':
        self.DisplayOutPut(return1 + ' ' + self.board.nextPlayer)
        self.board.__init__()

  def DisplayOutPut(self, str):
    print(str)


# def ask_name():
#     name = input('Please input your name: ')
#     print(f"Hello {name}!")

# ask_name()

game = Game()
game.main()
```