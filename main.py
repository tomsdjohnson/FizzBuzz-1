# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### if this function here is not used it can be deleted
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def multiple_of(multiple, num, rules):
    return (multiple % num == 0) and rules.__contains__(str(num))


def insert_fezz(strings):
    for i in range(0, len(strings)):
        if strings[i][0] == 'B':
            strings.insert(i, "Fezz")
            return strings
    strings.append("Fezz")
    return strings


def fizzbuzz(limit, rules):
    print(rules)
    for i in range(1, limit + 1):
        strings = []
        if multiple_of(i, 3, rules):
            strings.append("Fizz")
        if multiple_of(i, 5, rules):
            strings.append("Buzz")
        if multiple_of(i, 7, rules):
            strings.append("Bang")
        if multiple_of(i, 11, rules):
            strings.append("Bong")
        if multiple_of(i, 13, rules):
            strings = insert_fezz(strings)
        if multiple_of(i, 17, rules):
            strings = list(reversed(strings))
            
        ### Added a space here for readability    
        if len(strings) == 0:
            print(i)
        else:
            print(''.join(strings))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to FizzBuzz!\n")
    limit_input = input("Please enter which number you would like to stop at: ")#
    if not limit_input.isdigit():
        print("Please enter an integer!")
    else:
        rules_input = input("Please enter the numbers of the rules you want to input (comma seperated): ")
        fizzbuzz(int(limit_input), rules_input.split(','))

        
