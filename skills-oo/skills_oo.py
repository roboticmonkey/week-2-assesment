"""skills file """
#started 10:30-12:40

class Student(object):
    """student class, holds first, last name and address"""

    score = None

    def __init__(self, first_name, last_name, address):
        """initializes a student object"""
        
        self.first_name = first_name 
        self.last_name = last_name
        self.address = address


class Question(object):
    """creates a question object"""

    def __init__(self, question, answer):
        """initializes a question object"""

        self.q_n_a = {'question': question, 'answer': answer,}

   
    def ask_and_evaluate(self):
        """ prints question, asks for answer, returns True or False depending
            the answer"""

        print self.q_n_a['question']
        answer = raw_input("Enter answer: ")
        if answer == self.q_n_a['answer']:
            # print True
            return True
        else:
            # print False
            return False

class Exam(object):
    """creates Exam objects"""

    def __init__(self, name):
        """initializes a list for exam questions"""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """adds a question to the list of questions"""

        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """admisters the exam, asks all the questions. gives back a score."""
        score = 0

        #loops through the questions and tally score
        for each in self.questions:
            
            if each.ask_and_evaluate() == True:
                score += 1
            else:
                continue

        # print score
        return score

class Quiz(Exam):
    """Quiz is a subclass of Exam"""


    def administer(self):
        """admisters the quiz, asks all the questions. gives back a pass/fail."""
        
        score = 0
        num_of_questions = len(self.questions)

        #loops through the questions and tallys score
        for each in self.questions:
            
            if each.ask_and_evaluate() == True:
                score += 1
            else:
                continue
        # print "score is", score
        # print " no. of questions to pass", num_of_questions/2.0
        
        #determains if the student passed or failed the quiz
        if score >= (num_of_questions/2.0):

            # print "Pass"
            return True
        else:

            # print "Failed"
            return False

def take_test(exam, student):
    """administers and exam for a student and records their score."""
  
    student.score = exam.administer()

    return None

def example():
    """used to test class, methods and functions to make a working exam & quiz"""

    student = Student('aiden', 'ward', '123 main st.')

    # exam = Exam('midterm')
    
    # exam.add_question('what is the sun?', 'a star')
    # exam.add_question('what does ALF want to eat?', 'a cat')
    # exam.add_question('who knew?', 'i did')
    # take_test(exam, student)

    quiz = Quiz('quiz1')
    quiz.add_question('what is the sun?', 'a star')
    quiz.add_question('what does ALF want to eat?', 'a cat')
    quiz.add_question('who knew?', 'i did')


    take_test(quiz, student)

example()




