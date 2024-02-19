
def fcn_factorial(n):
    valor=1
    for i in range(n):
        valor*=(i+1)
    return valor

if __name__=="__main__":
    print(fcn_factorial(5))