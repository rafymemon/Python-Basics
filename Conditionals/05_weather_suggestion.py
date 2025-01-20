
weather = input("Enter the weather forcast of your area :")


if weather == "Sunny" :
    activity = "Going for a walk in a sunny weather is better for your health ."
    #print("Going for a walk in a sunny weather is better for your health .")
elif weather == "Rainy" :
    activity = "Rainy weather is the best time for reading a book."
   # print("Rainy weather is the best time for reading a book.")
elif weather == "Snowy" :
    activity = "Show your art on the snow in a snowy weather."
    #print("Show your art on the snow in a snowy weather.")
elif weather == "Cloudy" :
   activity = "Enjoy the clouds and listen to music"
   # print("Enjoy the clouds and listen to music")
else :
    activity = "It is better to stay at home and watch netflix and chill rather than going out."


print(activity)