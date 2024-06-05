# Removing some punctuation marks in a sentence

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This perturbation randomly removes punctuation marks from a sentence (with a probability `prob`). 

NB: Punctuations marks are defined here using the regular expression `r'[^\w\s]'`, meaning any character that is not a word character nor a whitespace character. Underscores (`_`) are exempt.

Example:
```python
>>> trans = RemovePunctuation(seed=0, max_outputs=5, prob=0.5)
>>> trans.generate('Hello, world!!!! This is a test sentence with punctuation: commas, periods, exclamation marks!...')
>>> ['Hello, world!!! This is a test sentence with punctuation: commas periods, exclamation marks!..',
 'Hello, world! This is a test sentence with punctuation: commas, periods, exclamation marks!..',
 'Hello world!!! This is a test sentence with punctuation commas periods, exclamation marks..',
 'Hello, world!!! This is a test sentence with punctuation commas, periods exclamation marks!.',
 'Hello world!! This is a test sentence with punctuation commas periods exclamation marks!']
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## Evaluation

The impact on the performance of RoBERTa (`textattack/roberta-base-imdb`) on the IMDB dataset (20% test split):

| Data perturbation level | Accuracy drop |
|---|---|
| p = 0.50 | 95.0 -> 95.0 (0) |
| p = 0.75 | 95.0 -> 95.0 (0) |
| p = 1.00 | 95.0 -> 95.0 (0) |

## What are the limitations of this transformation?

This transformation will not be challenging for models that are trained on informal text data (which already display a limited use of punctuation marks). 
