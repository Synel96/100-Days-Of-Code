import turtle
import pandas

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()



screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50 :

   answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

   if answer_state == "Exit":
      missing_states = []
      for state in all_states :
         if state not in guessed_states:
            missing_states.append(state)
      new_data = pandas.DataFrame(missing_states)
      new_data.to_csv("States to Learn.csv")
      turtle.bye()
      break
   if answer_state in all_states:
      guessed_states.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(state_data.x.item() , state_data.y.item())
      t.write(answer_state)





def get_mouse_click_coor(x,y):
   print([x, y])

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()


