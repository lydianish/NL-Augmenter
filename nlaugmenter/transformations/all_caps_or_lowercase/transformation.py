import random

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

class AllCapsOrLowercase(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["en"]

    def __init__(self, seed=0, max_outputs=1):
        super().__init__(seed=seed, max_outputs=max_outputs)
    
    def generate(self, sentence: str):
        random.seed(self.seed)
        outputs = []
        for _ in range(self.max_outputs):
            if random.random() > 0.5:
                outputs.append(sentence.upper())
            else:
                outputs.append(sentence.lower())
        return outputs