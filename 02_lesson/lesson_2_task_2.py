def is_year_leap(years):
    return "True" if years % 4 == 0 else "False"


y = int(input("Год: "))
result = is_year_leap(y)
print(f"Год {y} - {result}")
