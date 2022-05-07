import math


def my_equasion(x):
    return math.sqrt(x)


def calculate_value(x):

    result = x

    
    try: 
        if x < 0:
            result = x*10
            return result
    finally:
        result = x*2

    return result
    
    


if __name__ == "__main__":

    # error = MyError("Ошибка!")

    # print(f"{error}")
       
    print(calculate_value(9))

    # y = my_equasion(9)




