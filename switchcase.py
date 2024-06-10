def print_day(day_number):
    switch = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    
    day_name = switch.get(day_number, "Invalid day")
    print(day_name)

def main():
    for day_number in range(1, 9):  
        print_day(day_number)

if __name__ == "__main__":
    main()
