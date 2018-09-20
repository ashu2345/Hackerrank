class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self,firstName,lastName,idNumber,*scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def calculate(self):
        reqSum=0
        for n in self.scores[0]:
            reqSum+=n
        av = reqSum/len(self.scores[0])
        if 90<=av<=100:
            return 'O'
        elif 80<=av<90:
            return 'E'
        elif 70<=av<80:
            return 'A'
        elif 60<=av<70:
            return 'P'
        elif 50<=av<60:
            return 'D'
        elif av<40:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
