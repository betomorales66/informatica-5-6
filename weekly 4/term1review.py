from datetime import datetime

def main():
    day = datetime.now().weekday()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print(days[day])
    if day < 4:
        print("it's a weekday 🥱")
        remaining = 5 - day
        print(remaining, "days until the weeknd")

    elif day == 4:
        print("it's friday 🥵")
        print("just a day left until the weeknd")

    else:
        print("it's weekend")

    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month = datetime.now().now().month
    print("it's", months[month-1])
    
    print("these are the summer months:")
    print(months[5])
    print(months[6])
    print(months[7])



if __name__=="__main__":
    main()
