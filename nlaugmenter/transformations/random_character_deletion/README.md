# Random Character Deletion

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This perturbation randomly deletes characters from a string of length > 1 with a probability `prob`.

Example:
```python
>>> trans = RandomCharacterDeletion(seed=0, max_outputs=5, prob=0.1)
>>> trans.generate('See you tomorrow.')
>>> ['See you tomorow.',
 'See you tomorow.',
 'Se you tomorrow.',
 'See you omorrow.',
 'See you tomorrow']
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## Evaluation

The impact on the performance of RoBERTa (`textattack/roberta-base-imdb`) on the IMDB dataset (20% test split):

| Data perturbation level | Accuracy drop |
|---|---|
| prob = 0.05 | 95.0 -> 94.0 (-1.0) |
| prob = 0.10 | 95.0 -> 91.0 (-4.0) |
| prob = 0.15 | 95.0 -> 87.0 (-8.0) |
| prob = 0.20 | 95.0 -> 85.0 (-10.0) |

## What are the limitations of this transformation?

If the probability p is set too high, deleting characters can result in deleting whole words, which can alter the meaning of the sentence, e.g. negations.
