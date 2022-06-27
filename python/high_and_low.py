def high_and_low(numbers):
    min = 1000
    max = -1000
    
    numbers = numbers.split(' ')
    intNum = [int(i) for i in numbers]
    
    for i in intNum:
        if i < min:
            min = i
        if i > max:
            max = i
    return f"{max} {min}"
