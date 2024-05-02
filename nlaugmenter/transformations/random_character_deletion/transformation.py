import numpy as np

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

def delete_random_characters(sentence: str, prob: float):
    if len(sentence) > 1:
        indices = np.random.choice([True, False], size=len(sentence), p=[prob, 1-prob])
        return ''.join(np.array(list(sentence))[~indices])
    return sentence

class RandomCharacterDeletion(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["All"]
    keywords = ["noise", "rule-based", "possible-meaning-alteration"]

    def __init__(self, seed=0, max_outputs=1, prob=0.1):
        super().__init__(seed=seed, max_outputs=max_outputs)
        self.prob = prob
    
    def generate(self, sentence: str):
        np.random.seed(self.seed)
        outputs = []
        for _ in range(self.max_outputs):
            perturbed_sentence = delete_random_characters(sentence, self.prob)
            outputs.append(perturbed_sentence)
        return outputs