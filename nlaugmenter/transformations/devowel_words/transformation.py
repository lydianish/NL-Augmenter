import numpy as np

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

def is_vowel(c: str):
    return c.lower() in ['a', 'e', 'i', 'o', 'u']

def delete_vowels_from_words(sentence: str, prob: float):
    words = sentence.split()
    new_words = []
    for word in words:
        vowel_mask = np.array([is_vowel(c) for c in word])
        if np.random.rand() < prob:
            vowel_mask[0] = False # Do not delete the first vowel
            new_words.append(''.join(np.array(list(word))[~vowel_mask]))
        else:
            new_words.append(word)
    return ' '.join(new_words)

class DevowelWords(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["en"]
    keywords = ["morphological", "rule-based", "unnaturally-written"]

    def __init__(self, seed=0, max_outputs=1, prob=1):
        super().__init__(seed=seed, max_outputs=max_outputs)
        self.prob = prob
        
    def generate(self, sentence: str):
        np.random.seed(self.seed)
        outputs = []
        for _ in range(self.max_outputs):
            perturbed_sentence = delete_vowels_from_words(sentence, self.prob)
            outputs.append(perturbed_sentence)
        return outputs
