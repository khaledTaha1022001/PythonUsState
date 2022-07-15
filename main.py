import turtle
from turtle import Turtle
import time
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image) # to add image as a shape to use it in .shape method
turtle.shape(image)

# def get_mouse_click_ciir(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_ciir)
# turtle.mainloop() # keep our screen open , to click and screen is not exit

def add_on_screen(state_name,x,y):
    screentext= Turtle()
    screentext.hideturtle()
    screentext.penup()
    screentext.goto(x=x,y=y)
    screentext.write(state_name,font=("Arial", 8, "normal"))







correct_answer_counter=0

data = pandas.read_csv("50_states.csv")
state_list = []
for state in data["state"]:
    state_list.append(state)

all_states= len(state_list)

game_is_on= True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    if len(state_list)==0:
        game_is_on=False
    answer_state= screen.textinput(title=f"you guessed : {correct_answer_counter} / {all_states} ", prompt="what's another state's name?")
    if answer_state =="Exit":
        break
    for state in state_list:
        if state== answer_state:
            state_list.remove(state)
            correct_answer_counter+=1
            x=data[data["state"]==state]["x"].to_list()
            y = data[data["state"] == state]["y"].to_list()
            print(x[0])
            print(y[0])
            add_on_screen(state_name=state, x=x[0], y=y[0])


