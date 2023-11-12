class Gradebook:
    disciplines_list = ["Математика", "Физика", "Литература", "История", "Химия"]
    possible_grades = ["отлично", "хорошо", "удовл.", "неудовл.", "н/я"]

    def __init__(self, discipline, group):
        if discipline not in Gradebook.disciplines_list:
            raise ValueError(f"Доступные дисциплины: {', '.join(Gradebook.disciplines_list)}")
        self.discipline = discipline
        self.group = group
        self.grades = {}

    def __str__(self):
        title = f"Ведомость по предмету '{self.discipline}', группа {self.group}"
        separator = "-" * len(title)
        results = "\n".join(f"{last_name}: {grade}" for last_name, grade in self.grades.items())
        return f"{title}\n{separator}\n{results}\n{separator}"

    def put(self, last_name, grade):
        if grade not in Gradebook.possible_grades:
            raise ValueError(f"Доступные оценки: {', '.join(Gradebook.possible_grades)}")
        self.grades[last_name] = grade

    def get(self, last_name):
        return self.grades.get(last_name, None)

    def change(self, last_name, new_grade):
        if new_grade not in Gradebook.possible_grades:
            raise ValueError(f"Доступные оценки: {', '.join(Gradebook.possible_grades)}")
        if last_name not in self.grades:
            raise ValueError(f"Студента с фамилией {last_name} нет в ведомости.")
        self.grades[last_name] = new_grade

    def delete(self, last_name):
        if last_name not in self.grades:
            raise ValueError(f"Студента с фамилией {last_name} нет в ведомости.")
        del self.grades[last_name]

    def result(self):
        grades_count = {grade: 0 for grade in Gradebook.possible_grades}
        for grade in self.grades.values():
            grades_count[grade] += 1
        return tuple(grades_count.values())

    def count(self):
        return len(self.grades)

    def names(self):
        return list(self.grades.keys())


if __name__ == "__main__":
    gradebook = Gradebook("Математика", "ДПИ22-2")

    gradebook.put("Иванов", "отлично")
    gradebook.put("Петров", "хорошо")
    gradebook.put("Сидоров", "удовл.")
    gradebook.put("Кузнецов", "неудовл.")

    print(gradebook)
    print()

    print("Оценка студента с фамилией Петров:", gradebook.get("Петров"))

    gradebook.change("Иванов", "удовл.")
    print(gradebook)
    print()

    gradebook.delete("Сидоров")
    print(gradebook)
    print()

    gradebook.put("Сидоров", "удовл.")
    print(gradebook)
    print()

    print("Оценки в ведомости:", gradebook.result())
    print("Количество студентов:", gradebook.count())
    print(f"Студенты:", ', '.join(gradebook.names()))
