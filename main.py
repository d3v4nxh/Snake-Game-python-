from tkinter import *
import random

score = 0
direction = 'down'


class Attribute:
    def __init__(self):
        global score, direction
        self.game_width = 1000
        self.game_height = 800
        self.speed = 100
        self.space_size = 50
        self.body = 3
        self.snake_color = 'cyan'
        self.foodcolor = 'red'
        self.bg_color = 'black'

        self.root = Tk()
        self.root.title('Snake Game')
        self.root.resizable(False, False)

        self.lblscr = Label(self.root, text=f'Score: {score}', font=('Terminal', 30))
        self.lblscr.pack()

        self.cnvs = Canvas(self.root, bg=self.bg_color, height=self.game_height, width=self.game_width)
        self.cnvs.pack()

        self.rstbtn = Button(text='Reset', command=self.reset)
        self.rstbtn.pack()

        self.set_Snake()
        self.set_Food()

        self.root.bind('<Left>', self.change_Dir_left)
        self.root.bind('<Right>', self.change_Dir_right)
        self.root.bind('<Up>', self.change_Dir_up)
        self.root.bind('<Down>', self.change_Dir_down)

        self.next_Turn()
        self.root.mainloop()

    def set_Snake(self):
        self.body_size = self.body
        self.coordinates = []
        self.squares = []

        for i in range(0, self.body):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.cnvs.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color,
                                                tag='snake')
            self.squares.append(square)

    def set_Food(self):
        x = random.randint(0, (self.game_width // self.space_size) - 1) * self.space_size
        y = random.randint(0, (self.game_height // self.space_size) - 1) * self.space_size
        self.food_coordinates = [x, y]
        self.cnvs.create_oval(x, y, x + self.space_size, y + self.space_size, fill=self.foodcolor, tag='food')

    def next_Turn(self):
        x, y = self.coordinates[0]
        if direction == 'up':
            y -= self.space_size
        elif direction == 'down':
            y += self.space_size
        elif direction == 'left':
            x -= self.space_size
        elif direction == 'right':
            x += self.space_size

        self.coordinates.insert(0, (x, y))

        square = self.cnvs.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color)

        self.squares.insert(0, square)

        if x == self.food_coordinates[0] and y == self.food_coordinates[1]:
            global score
            score += 1
            self.lblscr['text'] = f'Score: {score}'
            self.cnvs.delete('food')
            self.set_Food()
        else:
            del self.coordinates[-1]
            self.cnvs.delete(self.squares[-1])
            del self.squares[-1]

        if self.check_Collision():
            self.game_Over()
        else:
            self.root.after(self.speed, self.next_Turn)

    def change_Dir_left(self, event):
        global direction
        if direction != 'right':
            direction = 'left'

    def change_Dir_right(self, event):
        global direction
        if direction != 'left':
            direction = 'right'

    def change_Dir_up(self, event):
        global direction
        if direction != 'down':
            direction = 'up'

    def change_Dir_down(self, event):
        global direction
        if direction != 'up':
            direction = 'down'

    def check_Collision(self):
        x, y = self.coordinates[0]
        if x < 0 or x >= self.game_width:
            return True
        elif y < 0 or y >= self.game_height:
            return True

        for body in self.coordinates[1:]:
            if x == body[0] and y == body[1]:
                return True

        return False

    def game_Over(self):
        self.cnvs.delete(ALL)
        self.cnvs.create_text(self.cnvs.winfo_width() / 2, self.cnvs.winfo_height() / 2, font=('terminal', 20),
                              text='Game Over', fill='red', tag='over')

    def reset(self):
        global score, direction
        score = 0
        direction = 'down'
        self.lblscr.config(text=f'Score: {score}')
        self.cnvs.delete(ALL)
        self.set_Snake()
        self.set_Food()
        self.next_Turn()

a1 = Attribute()
        



