def lateRide(n):

    hours = str(n // 60)
    minutes = str(n % 60)
    time = hours + minutes

    return(sum(int(num) for num in time))

print(lateRide(808))