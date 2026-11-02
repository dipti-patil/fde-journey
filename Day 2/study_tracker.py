# total_hours(daily: list[float]) -> float: total of a list of daily hours, using a loop, not sum().
def total_hrs(daily:list[float]) -> float:
    total = 0
    for hrs in daily:
        total += hrs
    return total


# best_day(daily: list[float]) -> int: the day number (starting at 1) with the most hours, without max()
def best_day(daily: list[float]) -> int:
    best_hrs = daily[0]
    best_day_num = 1
    for  day_num, hrs in enumerate(daily[1:], start=2):
        if hrs > best_hrs:
            best_hrs = hrs
            best_day_num = day_num
    return best_day_num

#  status(avg: float) -> str: returns "ahead" if avg ≥ 5.5, "on track" if avg ≥ 4.5, otherwise "behind". Use early returns

def status(avg:float) -> str:
    if avg >=5.5:
        return "ahead"
    if avg >=4.5:
        return "on track"
    return "behind"

# ask_hours() -> float: uses a while loop to keep asking until the user enters a number between 0 and 12 inclusive. For now it is fine if typing a word crashes it; Day 4 fixes that.
def ask_hrs() -> float:
    while True:
        hrs = float(input("enter the hrs you studdied today:"))

        if 0 <= hrs <= 12:
            return hrs


# At the bottom, collect 7 days of hours by calling ask_hours() in a loop, and print a summary: total, average (1 decimal place), best day and status.
daily_hrs=[]

for day in range(1,8):
    print(f"Day {day}:")
    hrs = ask_hrs()
    daily_hrs.append(hrs)


# Calculate results

total = total_hrs(daily_hrs)
average = total / 7
best = best_day(daily_hrs)
progress = status(average)

print("\n========== Weekly Study Summary ==========")
print(f"Daily hours: {daily_hrs}")
print(f"Total hours: {total:.1f}")
print(f"Average hours: {average:.1f}")
print(f"Best day: Day {best}")
print(f"Status: {progress}")
print("==========================================")