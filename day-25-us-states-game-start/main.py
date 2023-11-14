import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# #Find out the coordinate of each state
# def get_mouse_click_coor(x,y):
#    print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")
check_state = data.state.to_list()
# print(data)
guessed_states = []

while len(guessed_states) <50:
   name_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What is another state's name?").title()
   #print(name_state)

   # count = 0
   # while check_state == name_state:
   #    count = count+1

   if name_state == "Exit":
      missing_states=[]
      for state in check_state:
         if state not in guessed_states:
            missing_states.append(state)
      new_data = pd.DataFrame(missing_states)
      new_data.to_csv("state_to_learn.csv")
      break
   if name_state in check_state:
      guessed_states.append(name_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == name_state]
      t.goto(int(state_data.x), int(state_data.y))
      t.write(name_state)

# remaininf_state= pd.DataFrame
# remaining_state.to_csv() state_to_learn.csv
#screen.exitonclick()