import turtle
import pandas
screen = turtle.Screen()    
screen.title("American States Game")
#Fotoğraf yüklenebilir
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#####Mouse'la yer bulma kodu
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_number=0
data = pandas.read_csv("50_states.csv")
answer_data = []
while state_number < 50:

    answer = screen.textinput(title=f"{state_number}/50 Correct", prompt="What's another states name?").title()
    if answer == "Exit":
        break
    if answer in data.state.values and answer not in answer_data:
        answer_data.append(answer)
        state_data = data[data.state == answer]
#state.data.x int'e çevrilmeden konulursa hata veriyor çünkü index ve x valuları beraber olduğundan
        x = int(state_data.x)
        y = int(state_data.y)
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x,y)
        marker.write(answer)
        state_number+=1

with open("missed_states.csv","w") as missed:
    for state in data.state:
        if state not in answer_data:
            missed.write(f"{state}\n")
