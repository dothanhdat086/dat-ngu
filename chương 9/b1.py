x=int(input())
def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1
print("in ra ",sign(x))