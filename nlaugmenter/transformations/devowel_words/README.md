# Devowelling some words in a sentence

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This perturbation randomly selects words from a sentence (with a probability p) and devowels them by removing all their vowels (a, e, i ,o, u), except for one that's at the beginning of the word, e.g. `alright` -> `alrght`.

Example:
```python
>>> trans = DevowelWords(seed=0, max_outputs=5, prob=0.5)
>>> trans.generate('This is a sentence in which some words have been devowelled.')
>>> ['This is a sentence in which sm words have bn devowelled.',
 'This is a sntnc in whch some words have been devowelled.',
 'Ths is a sentence in which some wrds hv been dvwlld.',
 'This is a sentence in which some wrds hv been dvwlld.',
 'This is a sntnc in whch some wrds have bn dvwlld.']
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## Evaluation

The impact on the performance of RoBERTa (`textattack/roberta-base-imdb`) on the IMDB dataset (20% test split):

| Data perturbation level | Accuracy drop |
|---|---|
| p = 0.25 | 95.0 -> 94.0 (-1.0) |
| p = 0.50 | 95.0 -> 90.0 (-5.0) |
| p = 0.75 | 95.0 -> 78.0 (-17.0) |
| p = 1.00 | 95.0 -> 58.0 (-37.0) |

## What are the limitations of this transformation?

Removing all the vowels of a word except for the first one is a simple approach. In practice, people might use a more sophisticated way to devowel, for example:
- not devowelling a word that has mostly vowels because it will become unintelligible (e.g. `India` -> `nd`)
- only removing some of the vowels to avoid having a sequence of too many consonants (e.g. `international` -> `internatnl` instead of `intrntnl`).
