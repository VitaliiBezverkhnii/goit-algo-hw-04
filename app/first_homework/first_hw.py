from pathlib import Path


def total_salary(path):
    total_salary = 0
    average_salary = 0
    try:
        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = get_total_salary(lines)
            average_salary = get_average_salary(total_salary, len(lines))
    except FileNotFoundError as e:
        print(e)
    finally:
        return total_salary, average_salary

def get_total_salary(lines):
    total_salary = 0
    for line in lines:
        salary = line.split(",")[1]
        try:
            total_salary += float(salary)
        except ValueError as e:
            print(e)
            return 0
    return total_salary

def get_average_salary(total_salary, count_employes):
    return total_salary / count_employes

total, average = total_salary("first_homework/data/employee_data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
