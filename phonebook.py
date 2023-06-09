def phonebook():
    directory = {}

    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 3:
            print("quitting...")
            break

        elif command == 2:
            name = input("name: ")
            num = input("number: ")
            if name in directory:
                directory[name].append(num)
            else:
                directory[name] = [num]
            print("ok!")
            #print(directory)

        elif command == 1:
            name = input("name: ")
            if name in directory:
                for num in directory[name]:
                    print(num)
            else:
                print("no number")

if __name__ == "__main__":
    phonebook()
