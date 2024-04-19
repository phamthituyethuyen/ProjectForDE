class Employee:
    def __init__(self,fist_name, Id_student):
        self.fist_name = fist_name
        self.Id_student = Id_student
        self.mail = fist_name + Id_student +"@gmail.com"
        
    def information(self):
        return '1.{} \n2.{} \n3.{}'.format(self.fist_name, self.Id_student,self.mail)
Employee1 = Employee("tuyethuyenpham", "21166127")
print(Employee1.mail)
print(Employee1.information())