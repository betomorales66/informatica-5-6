def main():

    fruits = ["apple", "banana", "cherry"]
    print("pinapple" not in fruits)

    fruit = "apple"
    print("b" in fruit)

    tasks = []
    while True:
        print(f"you have {len(tasks)} tasks to do")
        print(tasks)

        new_task = input("enter task: ").capitalize().strip()

        if new_task == "Exit":
            break
        elif new_task not in tasks:
            tasks.append(new_task)
        elif new_task in tasks:
            del_confirm = input(f"did you completed {new_task}? (y/n): ")
            if del_confirm == "y":
                tasks.remove(new_tasks)
            elif del_confirm == "n":
                continue




if __name__=="__main__":
    main()

