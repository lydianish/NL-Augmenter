import random

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

class RandomCharacterDeletion(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["All"]

    def __init__(self, seed=0, max_outputs=1, prob=0.1):
        super().__init__(seed=seed, max_outputs=max_outputs)
        self.prob = prob
    
    def select_n_indices(self, n, n_max):
        indices = set()
        while len(indices) < n:
            indices.add(random.randint(0, n_max-1))
        return indices

    def generate(self, sentence: str):
        random.seed(self.seed)
        outputs = []
        chars_to_delete = int(len(sentence) * self.prob)
        for _ in range(self.max_outputs):
            indices = self.select_n_indices(chars_to_delete, len(sentence))
            perturbed_sentence = [ char for i, char in enumerate(sentence) if i not in indices ]
            outputs.append(''.join(perturbed_sentence))
        return outputs