import pandas as pd


def greater():
    var1 = pd.DataFrame({"A": [14, 25, 33, 42], "B": [543, 62, 27, 18]})
    var1["C"] = var1["A"] + var1["B"]
    var1["Python"] = var1["A"] > 20
    print(var1)


def insert_fun():
    var1 = pd.DataFrame({"A": [14, 25, 33, 42], "B": [543, 62, 27, 18]})
    var1["C"] = var1["A"] + var1["B"]
    var1.insert(1, "python_f", var1["A"])


# print(greater())


# print(insert_fun())
# Create a CSV file
def New_csv():
    dic = {"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]}
    d = pd.DataFrame(dic)
    print(d)
    d.to_csv("new.csv", index=False, header=[1, 2, 3])


print(New_csv())
