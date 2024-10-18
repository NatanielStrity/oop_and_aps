class SJurnal:

    def __init__(self, student, sbj):
        self.sbj = sbj
        self.student = student
    grade_list = [3, 3, 3, 3, 3, 4, 5]


    def grade(self, grade):
        self.grade_list.append(grade)
    

    def printer(self):
        print(self.student)
        print(self.sbj)
        print(self.grade_list)


    def final_grade(self):
       final_grade = sum(self.grade_list)/len(self.grade_list)
       print(final_grade)

sj = SJurnal('Петя', 'Химия')
sj.printer()
sj.final_grade()
