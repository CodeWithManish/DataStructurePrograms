def prime_list(num1, num2):
    list_ = []
    for number in range(num1, num2):
        count = 0
        for iterate in range(1, number):
            if number % iterate == 0:
                count += 1
        if count >= 2:
            continue
        if count < 2:
            list_.append(number)
    return list_


if __name__ == "__main__":
    arr = []
    num1 = 1
    num2 = 100
    while num2 < 1000:
        list2 = prime_list(num1, num2)
        arr.append(list2)
        num1 += 100
        num2 += 100

    print(arr)