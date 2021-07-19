from interfaces.SentenceOperation import SentenceOperation
from tasks.TaskTypes import TaskType
from initialize import spacy_nlp
import spacy
import jellyfish


class PhoneticMatchFilter(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    languages = ["en"]

    def __init__(self, keywords=None, algorithm: str = 'soundex'):
        super().__init__()
        self.keywords = keywords if keywords else ["hatstand", "jacket", "umbrella", "pineapple"]
        try:
            self.algo = getattr(jellyfish, algorithm)
        except AttributeError:
            raise NotImplementedError("Jellyfish does not implement `{}`".format(algorithm))
        self.nlp = spacy_nlp if spacy_nlp else spacy.load("en_core_web_sm")

    def filter(self, sentence: str = None) -> bool:
        tokenized = self.nlp(sentence, disable=["parser", "tagger", "ner", "lemmatizer"])
        phonetic = [self.algo(token.text) for token in tokenized]
        matchers = [self.algo(kw) for kw in self.keywords]
        contains_soundalikes = set(phonetic).intersection(set(matchers))
        return bool(contains_soundalikes)
