def calculator():
    mileage_goal = int(input("How many miles do you want to run this week?\n"))
    mileage_so_far = float(input("How many miles have you run so far?\n"))
    days_left = int(input("How many days of the week are left?\n"))
    long_run = mileage_goal / 4.0
    if long_run - int(long_run) >= .5:
        long_run = int(long_run) + 1
    else:
        long_run = int(long_run)
        
    regular_run = (mileage_goal - long_run - mileage_so_far) / (days_left - 1)
    shorter_regular_run = int(regular_run)
    longer_regular_run = shorter_regular_run
    if regular_run % int(regular_run) != 0:
        longer_regular_run = int(regular_run) + 1
    print(round((regular_run % int(regular_run)) * (days_left - 1)))
    days_of_longer_regular_run = round((regular_run % int(regular_run)) * (days_left - 1))    
    
    
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(days_left - days_of_longer_regular_run - 1):
        print("run", shorter_regular_run, "miles on", days_of_the_week[i + 7 - days_left])
    for j in range(days_of_longer_regular_run):
        print("run", longer_regular_run, "miles on", days_of_the_week[j + 7 - days_left - days_of_longer_regular_run])
    print("run", long_run, "miles on", "Sunday")
    
    print(days_of_longer_regular_run)
    print("hi")


if __name__ == '__main__':
    calculator()
