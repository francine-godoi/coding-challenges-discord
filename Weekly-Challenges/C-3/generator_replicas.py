def erange(*args):
    num_args = len(args)
    start = 0
    step = 1

    # associate args with their position in function
    if num_args == 3:
        start, stop, step = args
    elif num_args == 2:
        start, stop = args
    else:
        stop = args[0]
    
    # The 1st iteration throgh the loop will add the 'step', so it has to
    # be reduced beforehand so 'start' starts from the number it's supposed to
    start -= step

    if step > 0: # loop for positive 'step'
        while start + step < stop: # if adding a 'steo' makes 'start' go over 'stop' it stops the loop
            start += step
            yield(start)
    else:
        while start + step > stop: # loop for negative 'step'
            start += step
            yield(start)


def numerate(*args):
    num_args = len(args)
    start_index = 0

    # associate args with their position in function
    if num_args == 2:
        iterable, start_index = args
    else:
        iterable = args[0]   

    # iterate over the iterable and return the value with an index
    for value in iterable:
        yield start_index, value
        start_index += 1


if __name__=="__main__":

    iterable = []

    for i in erange(5):
        iterable.append("It worked!")

    for index, value in numerate(iterable, 1):
       print(f"{value} {index} time(s)!!")

