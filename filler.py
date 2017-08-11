import turtle, random

colors = ["red","Green Yellow","black","Deep Sky Blue","Dark Violet", "yellow"]
colors_two = []
colors_updated = ["Orange Red", "Lawn Green", "Dark Slate Gray", "Dodger Blue", "Purple", "Gold"]
user_entered_color = ["red", "green", "black", "blue", "purple", "yellow"]
cubes = []
user_chunk = []
computer_chunk = []
score = 0
score_two = 0
user_choice = ""
computer_choice = ""

# Creates user 1 and user 2's board
for x in range(64):
  user_chunk.append(-1)
  computer_chunk.append(-1)

# Creates the board and filters out doubled blocks
for x in xrange(64):
  cubes.append(random.choice(colors))
  if cubes[x] == cubes[x - 1]:
    for i in xrange(len(colors)):
      if cubes[x] != colors[i]: #Filters out color that is a copy
        colors_two.append(colors[i])
    cubes.pop()
    cubes.append(random.choice(colors_two))
    del colors_two[:]
  if x >= 8:
    if cubes[x] == cubes[x - 8]:
      for i in xrange(len(colors)):
        if cubes[x] != colors[i]:
          colors_two.append(colors[i])
      cubes.pop()
      cubes.append(random.choice(colors_two))
      del colors_two[:]

  if cubes[x] == cubes[x - 1]: # Double filter due to it missing a few duplicates (Sloppy but YOLO)
    for i in xrange(len(colors)):
      if cubes[x] != colors[i]:
        colors_two.append(colors[i])
    cubes.pop()
    cubes.append(random.choice(colors_two))
    del colors_two[:]
  if x >= 8:
    if cubes[x] == cubes[x - 8]:
      for i in xrange(len(colors)):
        if cubes[x] != colors[i]:
          colors_two.append(colors[i])
      cubes.pop()
      cubes.append(random.choice(colors_two))
      del colors_two[:]

def filler_board():

  turtle.pensize(3)
  turtle.tracer(0, 0)
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(-122, -122)

  for i in range(4):
    turtle.color("grey")
    turtle.pendown()
    turtle.forward(265)
    turtle.left(90)

  # Draws board
  count = 0
  for j in range(-120, 120, 33):
    for i in range(-120, 120, 33):
        turtle.color(cubes[count])
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()
        count += 1

        # Draw a small rectangle
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()
  turtle.update()

def choices():

  count = 0

  turtle.color("Ghost White")
  turtle.penup()
  turtle.goto(-140, -185)
  turtle.pendown()
  turtle.begin_fill() #Creates blue rectangle for player one's score
  for k in range(2):
      turtle.forward(300)
      turtle.left(90)
      turtle.forward(45)
      turtle.left(90)
  turtle.end_fill()

  for x in range(6):
    turtle.penup()
    turtle.goto(-130 + count, -180)
    count += 50
    turtle.pendown()
    turtle.color(colors[x])

    if (cubes[0] == colors[x] or cubes[0] == colors_updated[x]) or (cubes[63] == colors[x] or cubes[63] == colors_updated[x]): # Shrinks the color that the player cannot select
      turtle.color(colors[x])
      turtle.begin_fill()
      for k in range(4):
        turtle.forward(20)
        turtle.left(90)
      turtle.end_fill()

    else:
      turtle.begin_fill()
      for k in range(4):
          turtle.forward(30)
          turtle.left(90)
      turtle.end_fill()
  turtle.update()

def user_moves():

  global score
  global user_choice
  user_choice = raw_input("Player 1 - Choose a color: (red, green, black, blue, purple, yellow)")
  user_chunk[0] = 1

  if user_choice != computer_choice:
    for x in xrange(len(cubes)):
      for i in xrange(len(user_entered_color)):
        if user_choice == user_entered_color[i]:
          for z in xrange(len(user_chunk)):
            if user_chunk[z] == 1:
              cubes[z] = colors_updated[i]
              if cubes[z + 1] == colors[i]: # Checks the block to the right of the cube
                user_chunk[z + 1] = 1
              if z <= 55 and cubes[z + 8] == colors[i]: # Checks the block above the cube
                user_chunk[z + 8] = 1
              if z >= 8 and cubes[z - 8] == colors[i]: # Checks the block below the cube
                user_chunk[z - 8] = 1
                cubes[z - 8] = colors_updated[i]
      break
  else:
    print "You cannot enter the same color as the other player."

  score = user_chunk.count(1)

def computer_moves():

  global score_two
  global computer_choice
  computer_choice = raw_input("Player 2 - Choose a color: (red, green, black, blue, purple, yellow)")
  computer_chunk[63] = 1

  if computer_choice != user_choice:
    for x in reversed(cubes):
      for i in xrange(len(user_entered_color)):
        if computer_choice == user_entered_color[i]:
          for z in xrange(63, 0, -1):
            if computer_chunk[z] == 1:
              cubes[z] = colors_updated[i]
              if cubes[z - 1] == colors[i]: # Checks the block to the left of the cube
                computer_chunk[z - 1] = 1
              if cubes[z - 8] == colors[i]: # Checks the block below the cube
                computer_chunk[z - 8] = 1
              if z <= 55 and cubes[z + 8] == colors[i]: # Checks the block above the cube
                user_chunk[z + 8] = 1
                cubes[z + 8] = colors_updated[i]
  else:
    print "You cannot enter the same color as the other player."

  score_two = computer_chunk.count(1)

def scoreboard():

  turtle.penup()
  turtle.goto(-160, 150)
  turtle.pendown()
  turtle.color("Deep Sky Blue")

  turtle.begin_fill() #Creates blue rectangle for player one's score
  for k in range(2):
      turtle.forward(33)
      turtle.left(90)
      turtle.forward(23)
      turtle.left(90)
  turtle.end_fill()

  turtle.goto(-159, 152) # Writes player 1's score
  turtle.color("black")
  if score <= 9:
    turtle.write("0" + str(score), font=("Arial", 20, "bold"))
  else:
    turtle.write(str(score), font=("Arial", 20, "bold"))
  turtle.penup()
  turtle.goto(146, 150)
  turtle.color("Lawn Green")

  turtle.begin_fill() #Creates green rectangle for player two's score
  for k in range(2):
      turtle.forward(35)
      turtle.left(90)
      turtle.forward(25)
      turtle.left(90)
  turtle.end_fill()

  turtle.goto(149, 153) # Writes player 2's score
  turtle.color("black")
  if score_two <= 9:
    turtle.write("0" + str(score_two), font=("Arial", 20, "bold"))
  else:
    turtle.write(str(score_two), font=("Arial", 20, "bold"))

def main():

  switch_move = "user" # Sloppy way of switching from player 1 to player 2

  while score + score_two < 64:
    if switch_move == "user":
      filler_board()
      scoreboard()
      choices()
      user_moves()
      switch_move = "computer"
    if score + score_two < 64: # Makes sure that player 2's move doesnt happen once the board is full
      if switch_move == "computer":
        filler_board()
        scoreboard()
        choices()
        computer_moves()
        switch_move = "user"
  filler_board()
  choices()

  if score > score_two: # Prints out the winner
    print "Player 1 wins!"
  elif score < score_two:
    print "Player 2 wins!"
  else:
    print "Tie!"

main()
