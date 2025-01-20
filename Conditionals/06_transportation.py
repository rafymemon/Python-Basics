distance = int(input("Enter the distance :"))
#distance_in_int = int(distance)

if distance < 3 :
    transport = "Walk"
elif distance <= 15 :
    transport = "bike"
elif distance >15 and distance <100:
    transport = "Car"
else :
    transport = "Plane"
    
print("According to your distance, you can use ",transport)