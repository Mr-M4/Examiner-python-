class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average_score(self):
        total_score = sum(self.scores)
        average_score = total_score / len(self.scores)
        return average_score


class Examiner:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_class_average(self):
        total_scores = 0
        total_students = len(self.students)

        for student in self.students:
            total_scores += sum(student.scores)

        class_average = total_scores / (total_students * len(student.scores))
        return class_average

    def generate_report(self):
        print("Student Report:")
        print("=================")
        for student in self.students:
            average_score = student.calculate_average_score()
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Average Score: {average_score}")
            print("=================")

        class_average = self.calculate_class_average()
        print("Class Average Score:", class_average)


def main():
    examiner = Examiner()

    # Create student objects and add them to the examiner
    student1 = Student("1001", "John Smith")
    student1.add_score(85)
    student1.add_score(92)
    student1.add_score(78)
    examiner.add_student(student1)

    student2 = Student("1002", "Jane Doe")
    student2.add_score(90)
    student2.add_score(88)
    student2.add_score(94)
    examiner.add_student(student2)

    # Generate report
    examiner.generate_report()


if __name__ == "__main__":
    main()
