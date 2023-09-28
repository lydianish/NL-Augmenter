import json
import os
import random

from nlaugmenter.interfaces.SentenceOperation import SentenceOperation
from nlaugmenter.tasks.TaskTypes import TaskType

"""
Base Class for implementing the different input transformations a generation should be robust against.
"""


def generate_sentence(sentence, spell_errors, prob_of_typo, seed):
    output = []
    random.seed(seed)
    for word in sentence.split():
        if (
            word.lower() in list(spell_errors.keys())
            and random.choice(range(0, 100)) <= prob_of_typo
        ):
            output.append(random.choice(spell_errors[word.lower()]))
        else:
            output.append(word)
    output = " ".join(output)
    return output


def generate_sentences(text, prob=0.1, seed=0, max_outputs=1):
    spell_errors = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "spell_errors.json"
    )
    with open(spell_errors, "r") as fp:
        spell_errors = json.load(fp)

    prob_of_typo = int(prob * 100)

    perturbed_texts = []
    for idx in range(max_outputs):
        new_text = generate_sentence(
            text, spell_errors, prob_of_typo, seed + idx
        )
        perturbed_texts.append(new_text)
    return perturbed_texts


class SpellingTransformation(SentenceOperation):
    tasks = [
        TaskType.TEXT_CLASSIFICATION,
        TaskType.TEXT_TO_TEXT_GENERATION,
        TaskType.TEXT_TAGGING,
    ]
    languages = ["en"]

    def __init__(self, prob=0.2, seed=0, max_outputs=3):
        super().__init__(seed, max_outputs=max_outputs)
        self.prob = prob

    def generate(self, sentence: str):
        perturbed_texts = generate_sentences(
            text=sentence,
            prob=self.prob,
            seed=self.seed,
            max_outputs=self.max_outputs,
        )
        return perturbed_texts
