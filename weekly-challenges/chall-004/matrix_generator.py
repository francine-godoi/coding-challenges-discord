import random 

def TwoDList():
    twoD_list=[]
    _list=[]
    _len = random.randint(1,20)

    for x in range(random.randint(1,10)):
        for y in range(_len):
            _list.append(int(random.randint(0,99)/10 if random.randint(1,4)!=4 else 0))

        twoD_list.append(_list)
        _list=[]

    return twoD_list