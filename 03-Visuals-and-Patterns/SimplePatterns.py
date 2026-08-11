# Full Pyramid
print("1. Full Pyramid Pattern with Python")
print()
def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)
print()

print("2. Inverted Full Pyramid")
print()
def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print("")

inverted_full_pyramid(5)
print()

print("3. Hollow Pyramid")
print()
def hollow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_pyramid(5)
print()

print("4. Half and Inverted Half Pyramids")
print()
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

half_pyramid(5)

def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

inverted_half_pyramid(5)

