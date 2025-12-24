
def Get_day(current_day, month_abv, starting_year):
    date = print(f"{current_day:02}/ {month_abv}/ {starting_year}")
    return date

def main():
    months_num: dict = {1:'Jan', 2:'Feb', 3:'mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    days_in_month: list[int] = [0,31,28,31,30,31,30,31,31,30,31,30,32] #list [0] = 0 for month num allignment
    running: bool = True
    months_in_year:int = 12  

    starting_year: int = int(input("Enter the year: "))
    starting_month: int = int(input("Enter the month: "))
    starting_day: int = int(input("Enter the day: "))
    days_amt: int = int(input("How many days do you want: "))

    days_diff: int = starting_day
    month_abv: int = months_num[starting_month]
    leap_year: int = starting_year % 4       #To find if the year is a leap year

    if (leap_year == 0):
        days_in_month[2] = 29         #leap year + 1 day to Febuary
    else:
        days_in_month[2] = 28           #non-leap year

    while(running):
        #puting month abv at start
        if (starting_day != 1):
            print(f"\n{month_abv}")
        elif (starting_day == 1):
            print(f"\n{month_abv}")

        #counting days                
        for days in range(days_amt+1):
            
            current_day = starting_day + days
            days_diff -= 1

            if ((current_day > days_in_month[starting_month]) and (starting_month < months_in_year)):
                starting_day = -days +1
                current_day = 1
                starting_month +=1 
                month_abv = months_num[starting_month]
                days_in_month[starting_month]  
                print(f" \n{month_abv}")                  

            Get_day(current_day,month_abv,starting_year)
            
            #changing year
            if (current_day>=31 and month_abv == 'Dec'):
                starting_year += 1
                starting_month = 0    
            #no more dates
            if (days_diff == 0):
                running = False
        
if __name__ == '__main__':
    main()  