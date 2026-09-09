def main():

    answer = "" #initialize
    followup = ""

    while answer != "Si!": #condition
        answer = input("ya merito? ").strip().title() #update
        if answer == "Si":
            followup = input("really? ").strip().title()
        if followup == "Si!":
            break

    print("ya llegamos!")






if __name__=="__main__":
    main()
