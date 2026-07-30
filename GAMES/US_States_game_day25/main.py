import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US States GAME")
#// to load a new image as turtle's image
image="blank_states_img.gif"         # the path to the image
screen.addshape(image)          #(just ....gif)
turtle.shape(image)    # now change the turtle shape to this image


data=pd.read_csv("50_states.csv")
all_state=data.state.to_list()
guessed_states=[]


while  len(guessed_states)<50 :
    answer_box=screen.textinput(title=f"Guess the states!,correct answer={len(guessed_states)}/50", prompt="what's the next state's name?").title()
    if answer_box=="Exit":
        missing_states=[state for state in all_state if state not in guessed_states ]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_box in all_state:
        guessed_states.append(answer_box)
        State_data=data[data.state==answer_box]    # just a row just !!!
        print(State_data)
        print(State_data.state.item())                 # from a row of a table a state column and .item as a string

        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(State_data.x.item(),State_data.y.item())      #x and y are the seri of table not a number  add . item for the number
        t.write(answer_box,align="center",font=("Arial",8,"normal"))

#screen.exitonclick()   is not necessary when we  have break
