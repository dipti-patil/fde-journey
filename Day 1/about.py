name = "Dipti Patil"
years_of_experience = 13.5
study_hrs_per_day= 3
job_ready = True

skills_to_learn=["python", "GenAI", "Agentic AI", "RAG"]

# Prints a neat summary using f-strings.
print("\n===== About Me =====")
print(f"Name: {name}")
print(f"Total Experience: {years_of_experience}")
print(f"Daily hrs for study:  {study_hrs_per_day}")
print(f"Skills to Learn: ", {', '.join(skills_to_learn)})


#Prints the type of each variable
print("\n===== Variable Types =====")
print (type(name))
print(type(years_of_experience))
print(type(study_hrs_per_day))
print(type(skills_to_learn))


# Calculate total study hours over 16 weeks
weeks = 16
total_days_in_week = 7

total_study_hours = study_hrs_per_day * total_days_in_week * weeks

print("\n===== Study Plan =====")
print(f"Total study hours over {weeks} weeks: {total_study_hours}")


# Asks the user with input() how many hours they studied today,
#  converts that to a number with float(), and prints how many hours remain in the 16-week budget, formatted with :.1f.

hours_studied_today = float(input("how many hrs you studied today: "))

remaining_hrs = total_study_hours - hours_studied_today
print(f"remaining hrs :{remaining_hrs}")