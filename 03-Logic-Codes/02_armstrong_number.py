def armstrong_check(num):
    order = len(str(num))
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return num == total

if __name__ == "__main__":
    number = 153
    if armstrong_check(number):
        print(f"{number} is an Armstrong Number!")
    else:
        print(f"{number} is NOT an Armstrong Number.")
