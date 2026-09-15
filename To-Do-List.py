def main():

    task = []
    while True:
        print(F"you have {len(task)} tasks to do.")
        print(task)
        command = input("what do you want to do? (add, complete, or end): ").lower()
        if command == "add":
            new_task = input("enter a new task: ")
            task.append(new_task)
        elif command == "complete":
            new_task = input("you have completed: ")
            task.remove(new_task)
        elif command == "end":
            break
            task.pop(new_task)
        else:
            print("que te pasa mijo that was not very mexican")















if __name__=="__main__":
    main()
