import re
import numpy as np

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

def remove_punctuation_with_probability(text, prob=0.5):
    # Define the regular expression pattern to match all punctuation characters
    pattern = r'[^\w\s]'
    # Use re.finditer to get an iterator over all punctuation matches
    matches = re.finditer(pattern, text)
    
    # Convert the text to a list of characters for easier manipulation
    text_list = list(text)
    
    for match in matches:
        # With probability p, replace the punctuation with an empty string
        if np.random.random() < prob:
            start = match.start()
            text_list[start] = ''  # Remove the punctuation character
    
    # Join the list back into a string
    cleaned_text = ''.join(text_list)
    return cleaned_text

class RemovePunctuation(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["en"]
    keywords = ["rule-based", "unnaturally-written"]

    def __init__(self, seed=0, max_outputs=1, prob=1):
        super().__init__(seed=seed, max_outputs=max_outputs)
        self.prob = prob
        print(f"RemovePunctuation initialized with seed {seed}, max_outputs {max_outputs}, prob {prob}")
        
    def generate(self, sentence: str):
        np.random.seed(self.seed)
        outputs = []
        for _ in range(self.max_outputs):
            perturbed_sentence = remove_punctuation_with_probability(sentence, prob=self.prob)
            outputs.append(perturbed_sentence)
        return outputs