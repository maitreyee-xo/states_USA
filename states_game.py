import turtle
import pandas

sc = turtle.Screen()
sc.title("States of the USA")
sc.setup(width=1.0, height=1.0)
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
list_of_state = states["state"]
list_of_states = list_of_state.to_list()
guessed_states = []
FONT = ("Arial", 24, "bold")
while len(guessed_states) < 50:
    answer_state = sc.textinput(title="Guess here!", prompt="Input your guesses here ")

    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_cor = states[states.state == answer_state]
        x_cordinate = float(x_cor["x"])
        y_cor = states[states.state == answer_state]
        y_cordinate = float(y_cor["y"])
        t.goto(x_cordinate, y_cordinate)
        t.write(answer_state)

    if answer_state == "Exit":
        t2 = turtle.Turtle()
        t2.hideturtle()
        t2.penup()
        t2.goto(0, 0)
        t2.write(F"GAME OVER. YOU GOT {len(guessed_states)} STATES RIGHT", align= "center", font =FONT)

    exit(0)

