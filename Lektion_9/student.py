class Student():
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade

    def calcAverage(self):
        totalgrades = 0
        for i in self.grade:
            if "b" in i:
                totalgrades += 1
            if "c" in i:
                totalgrades += 2
            if "d" in i:
                totalgrades += 3
            if "e" in i:
                totalgrades += 4
            if "f" in i:
                totalgrades += 5

        grades = ["a", "b", "c", "d", "e", "f"]
        print(self.grade)
        print()
        avg = totalgrades / len(self.grade)
        print ("Average grade is", grades[round(avg)])

student1 = Student("Peter", ["a", "b", "d", "f", "c", "a", "b", "c"])
student1.calcAverage()