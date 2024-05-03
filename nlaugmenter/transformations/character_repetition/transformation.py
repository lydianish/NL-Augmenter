import numpy as np

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

def repeat_characters(sentence: str, prob_rep: float, n_rep: float):
    chars = [ [c] for c in sentence ]
    for i, c in enumerate(sentence):
        if c in ['.', '?', '!'] or (c.isalpha() and np.random.rand() < prob_rep):
            chars[i] *= np.random.poisson(n_rep)
    return ''.join([ ''.join(c_list) for c_list in chars ])

class CharacterRepetition(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["en"]
    keywords = ["noise", "rule-based", "unnaturally-written"]

    def __init__(self, seed=0, max_outputs=1, prob_rep=0.05, n_rep=3):
        super().__init__(seed=seed, max_outputs=max_outputs)
        self.prob_rep = prob_rep
        self.n_rep = n_rep
    
    def generate(self, sentence: str):
        np.random.seed(self.seed)
        outputs = []
        for _ in range(self.max_outputs):
            perturbed_sentence = repeat_characters(sentence, self.prob_rep, self.n_rep)
            outputs.append(perturbed_sentence)
        return outputs
