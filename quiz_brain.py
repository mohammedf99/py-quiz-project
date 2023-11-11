class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        
    def has_next_questions(self):
        return self.q_number < len(self.q_list)
        
    def next_question(self):
        current_question = self.q_list[self.q_number]
        input(f"Q.{self.q_number + 1}: {current_question.text} (True/False): ")