
def reverse_by_deque(string1):
    container = []

    for i in string1:
        container.append(i)

    out_string = ""
    for i in range(len(string1)):
        out_string += container[-1]
        container.pop()
    return out_string


if __name__ == "__main__":
    input_string = input("Enter string to be checked: ")
    rev_string = reverse_by_deque(input_string)
    if rev_string == input_string:
        print("Palindrome")
    else:
        print("Not Palindrome")
