"""QUİZ UYGULAMASI."""

# Questions


class Questions:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0  # -> Hangi Soruyu seçeceğimiz. indexler 0 dan başladığı için soru1 gelir.

    def getquestion(self):
        return self.questions[self.questionIndex]

    def displayquestion(self):
        question = self.getquestion()
        print(f"soru {self.questionIndex + 1 } : {question.text} ")

        for q in question.choices:
            print("-" + q)
        answer = input("cevabiniz : ")
        self.guess(answer)

    def guess(self, answer):
        question = self.getquestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        self.loadquestion()

    def loadquestion(self):
        if len(self.questions) == self.questionIndex:
            self.showscore()

        else:
            self.displayprogress()
            self.displayquestion()

    def showscore(self):

        print("score :", self.score)

    def displayprogress(self):
        totalquestion = len(self.questions)
        questionnumber = self.questionIndex + 1

        if questionnumber > totalquestion:
            print("Quiz bitti.")

        else:
            print(f"question {questionnumber} of {totalquestion}".center(100, "*"))


q1 = Questions("soru1", ["cevap1", "cevap2", "cevap3"], "cevap1")
q2 = Questions("soru2", ["cevap1", "cevap2", "cevap3"], "cevap2")
q3 = Questions("soru3", ["cevap1", "cevap2", "cevap3"], "cevap3")


questions = [q1, q2, q3]


quiz = Quiz(questions)

quiz.loadquestion()
