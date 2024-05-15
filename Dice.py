import random
import matplotlib.pyplot as plt
from pyscript import display
from pyweb import pydom


def mainFunc(*args, **kwargs):
    dice = [1,2,3,4,5,6]
    # tryAmount = int(input("시도 횟수 : "))
    # sumAmount = int(input("합 개수 : "))
    # weight = list(map(float, input( "1~6의 가중치 띄어쓰기로 구분(0~1, 합해서 1) : ").split(" ")))
    tryAmount = int(pydom["#tryAmount"][0].value)
    sumAmount = int(pydom["#sumAmount"][0].value)
    weight = list(map(int, str(pydom["#weight"][0].value).split(" ")))
    resultRange = [[x, 0] for x in range(sumAmount, sumAmount*6 + 1)]
    # print(resultRange)

    for _ in range(tryAmount):
        diceSum = 0
        for i in range(sumAmount):
            diceSum += random.choices(dice, weight)[0]
        for j in resultRange:
            if j[0] == diceSum:
                j[1] += 1
        

    x = []
    y = []
    for h in resultRange:
        x.append(h[0])
        y.append(h[1])
        
    plt.xlabel("sum of dice")
    plt.ylabel("how many times")    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True)
    ax.bar(x, y, color="y") 
    display(fig, target="display", append=True)
    
def clearFunc(*args, **kwargs):
    plt.close("all")
    display("",target="display", append=False)
    
    