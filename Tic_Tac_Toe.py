'''
Build a working game of Tic Tac Toe from the command line.

1. A player can enter either X or O on a board. Display the (board). 
2. A player should enter grid[][] position into command line. Update and display the board. 
3. (Game) will identiy if game is won by any of the players it's a draw. 
4. Display option to replay. System will clear the board and display it. 

game will 

class Board 
  lastplayed -- (x or o) 
  grid [list[list]]

  Update(x,y) --> Invalid input, Who's turn it is, win or draw, who won 
  Update(x,y) (terminationCondition(can be winner or draw), warningMessage)
  ToString()
  

class Game 

  GetInput()
  DisplayOutput()
  

ORowsCount = [0] *3
OColsCount = [0] *3
XRowsCount = [0] *3
XColsCount = [0] *3
ODiagCount = 0
XDiagCount = 0
Update(x, y):
  ....
  if (player is O) :
    ORowsCount[x]++
      if ORowsCount[x] == 3 return win
    OColsCount[y]++
    
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/solutions/441422/java-python-c-0ms-short-and-simple-all-8-ways-to-win-in-one-array/comments/418232/ 
'''
# Python


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
