def main():
    n = input("Hello, whats ur name?:").capitalize()
    print(f"Hello {n} this app is designed to track ur gym routine")
    gym = (input("What day is it?: (This will give you a routine):")).capitalize()
    yes1 = ""
    if gym == "Monday":
        start=input("Type start to.... well start:").lower().strip()

        print("Okay, on Monday we focus on Chest & Arms")

        print("First, flat dumbbell or barbell bench press: 4 sets x 8–10 reps")
        yes1 = ""
        while yes1 != "done":
            yes1 = input("Type done to proceed:").lower().strip()
        print("Second, incline dumbbell press: 3 sets x 10–12 reps")
        yes1 = ""
        while yes1 != "done":
            yes1 = input("Type done to proceed:").lower().strip()
        print("Third, cable crossovers or dumbbell chest flyes: 3 sets x 12 reps")
        yes1 = ""
        while yes1 != "done":
            yes1=input("Type done to procede:")
        print("Forth, standing alternating dumbbell bicep curls: 3 sets x 10–12 reps")
        yes1 = ""
        while yes1 != "done":
            yes1 = input("Type done to proceed:").lower().strip()
        print("Last but not least, rope cable triceps pushdowns: 3 sets x 12 reps")
        print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Tuesday":
        start=input("Type start to.... well start:").lower().strip()

        print("Okay, on Tuesday we focus on Back & Core")

        print("First, lat pulldowns or pull-ups: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, seated cable rows: 4 sets x 10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, single-arm dumbbell rows: 3 sets x 10–12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth: hanging knee raises (or captain's chair raises): 3 sets x 12–15 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least: forearm plank: 3 sets x 45–60 seconds")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Wednesday":
        start=input("Type start to.... well start:").lower().strip()

        print("Okay, on Wednesday we focus on Legs & Glutes")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("First, barbell back squats or leg press: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, romanian deadlifts: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, walking lunges or Bulgarian split squats: 3 sets x 10–12 reps per leg")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth, lying or seated leg curls: 3 sets x 12–15 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least, standing calf raises: 4 sets x 15 reps ")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Thursday":
        start=input("Type start to.... well start:").lower().strip()
        print("Okay, on Thursday we focus on Shoulders & Arms")

        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("First, seated dumbbell shoulder press: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, seated dumbbell shoulder press: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, cable face pulls or rear delt flyes: 3 sets x 12–15 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth, Hammer curls: 3 sets x 10–12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least, Overhead dumbbell triceps extension: 3 sets x 12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Friday":
        print("Okay, on Friday we focus on Back & Chest")
        start=input("Type start to.... well start:").lower().strip()

        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("First, incline dumbbell bench press: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, chest-supported machine or dumbbell row: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, cable chest flyes: 3 sets x 12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth, close-grip lat pulldowns: 3 sets x 10–12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least, push-ups (bodyweight or deficit): 3 sets to failure")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Saturday":
        start=input("Type start to.... well start:").lower().strip()
        print("Okay, on Saturday we focus on Lower Body & Core")

        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("First, barbell or dumbbell hip thrusts: 4 sets x 8–10 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, goblet squats: 3 sets x 10–12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, seated leg extensions: 3 sets x 12–15 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth, cable woodchoppers or Russian twists: 3 sets x 15 reps per side")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least, Ab wheel rollouts or deadbugs: 3 sets x 12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    if gym == "Sunday":
        start=input("Type start to.... well start:").lower().strip()

        print("Okay, on Sunday we focus on Cardio & Full Body Conditioning")
        religion=input("Before we start, whats ur religion?:").capitalize()
        if religion == "Mormon":
            print("Sinner")
            exit()

        print("Alr, u can exercise today")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("First, incline treadmill walk or rowing machine: 20 minutes steady pace")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Second, kettlebell swings or dumbbell swings: 4 sets x 15 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Third, box jumps or step-ups: 3 sets x 12 reps")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
            print("Fourth, mountain climbers: 3 sets x 30 seconds")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("Last but not least, farmer's dumbbell walks: 3 sets x 40 meters")
        yes1 = input("Type done to proceed:").lower().strip()
        if yes1 == "done":
             print("All set! Thank you for using our app, we would apreciatte it if you leave us a review")
        r=float(input("Give us ur honest review from 1-5:"))
        if r >= 4.5:
            print("Yeah, thought so")
        elif r >= 4:
            print("good enough")
        elif r >= 3:
            print("Good ig 🙄")
        elif r >= 2:
            print("Wtv 🫩")
        else:
            print("C´mon man")
    else:
        print("Type an actual day")




if __name__ =="__main__":
    main()
