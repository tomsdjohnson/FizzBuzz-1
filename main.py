# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def multiple_of(multiple, num):
    return multiple % num == 0


def insert_fezz(strings):
    for i in range(0, len(strings)):
        if strings[i][0] == 'B':
            strings.insert(i, "Fezz")
            return strings
    strings.append("Fezz")
    return strings


def fizzbuzz(limit):
    for i in range(1, limit + 1):
        strings = []
        if multiple_of(i, 3):
            strings.append("Fizz")
        if multiple_of(i, 5):
            strings.append("Buzz")
        if multiple_of(i, 7):
            strings.append("Bang")
        if multiple_of(i, 11):
            strings.append("Bong")
        if multiple_of(i, 13):
            strings = insert_fezz(strings)
        if multiple_of(i, 17):
            strings = list(reversed(strings))
        if len(strings) == 0:
            print(i)
        else:
            print(''.join(strings))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to FizzBuzz!\n")
    limit = input("Please enter which number you would like to stop at: ")
    if limit.isdigit():
        fizzbuzz(int(limit))
    else:
        print("Please enter an integer!")


