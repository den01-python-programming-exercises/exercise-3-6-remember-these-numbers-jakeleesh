def main():
    #write your code below this line
    numbers = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            numbers.append(num)
    for number in numbers:
        print(number)

if __name__ == '__main__':
    main()
