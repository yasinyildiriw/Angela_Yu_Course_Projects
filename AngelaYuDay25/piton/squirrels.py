import pandas
data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
with open("number_of_squirrels.csv","w") as file:
    file.write(f"Gray Squirrels {gray_squirrels}\nCinnamon Squirrels {cinnamon_squirrels}\nBlack"
    f" Squirrels {black_squirrels}")