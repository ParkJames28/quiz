array1 = ["juan","pedro","torko"]
array2 = [
    ["kamote","bombay","suka"],
    ["tae","igit","tobol"],
    ["gorlock","lodi","petpeeve"]
]

def single_dimentional_array(array):
    for monkey in array:
        print(monkey)

def two_dimensional_array(array):
    for smegul in array:
        for baboy in smegul:
            print (baboy)

data1 = input("Which array you wanna display? single dimensional array or two dimensional array? ")

if data1 == "single dimensional array":
    single_dimentional_array(array1)
elif data1 == "two dimensional array":
    two_dimensional_array(array2)
