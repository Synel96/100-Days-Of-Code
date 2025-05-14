
import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)



data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Blakc"],
    "Count" : [gray_squirrels_count, cinnamon_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")
print(df)

        

