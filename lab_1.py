class SJurnal:

    def __init__(self, student, sbj):
        self.sbj = sbj
        self.student = student
    grade_list = [1, 5, 5, 4, 3, 2, 5]
    def grade(self, grade):
        self.grade_list.append(grade)

    def printer(self):
        print(self.student)
        print(self.sbj)
        print(self.grade_list)

    def final_grade(self):
        final_grad_ = sum(self.grade_list) / len(self.grade_list)
        print(final_grad_)
    
sjurnal = SJurnal('Петросян', 'ШедевроХимия')
sjurnal.printer()
sjurnal.final_grade()

    



    
