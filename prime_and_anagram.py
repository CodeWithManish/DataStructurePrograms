
def prime_number(num1, num2):
    list1 = []
    for i in range(num1, num2):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 2:
            continue
        if count < 2:
            list1.append(i)
    return list1


def anagram(num1, num2):
    list1 = []
    prime = prime_number(num1, num2)

    for i in range(len(prime)):
        for j in range(i+1, len(prime)):
            if sorted(str(prime[i])) == sorted(str(prime[j])):
                list1.append(prime[i])
                list1.append(prime[j])
    return list1


if __name__ == "__main__":
    arr = []
    num1 = 1
    num2 = 100
    while num2 < 1000:
        out_list = anagram(num1, num2)
        arr.append(out_list)
        num1 += 100
        num2 += 100

    print(arr)