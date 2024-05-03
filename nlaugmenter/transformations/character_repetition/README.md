# Character Repetition

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This perturbation tries to emulate some of the expressiveness of user-generated content by repeating characters. 
*All* sentence-ending punctuation (.?!) are repeated, while letters are selected for repetition with a probability `p_rep`. 
Digits, whitespace, and other punctuation and characters are not repeated.
The number of repetitions for a selected character is sampled from a Poisson distribution of parameter `n_rep`.

Example:
```python
>>> trans = CharacterRepetion(seed=0, max_outputs=5, prob_rep=0.5, n_rep=3)
>>> trans.generate('That's so cool!')
>>> ['That'ssssss so cool!!!!',
 'Thhhhat's so coool!',
 'TTTThhatt'sss sooo coool!!',
 'Thaaat's sssso coooooool!!!!!!!',
 'Thhhat's so coooooool!!!']
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## Evaluation

The impact on the performance of RoBERTa (`textattack/roberta-base-imdb`) on the IMDB dataset (20% test split):

| Data perturbation level | Accuracy drop |
|---|---|
| p = 0.05 | 95.0 -> 94.0 (-1.0) |
| p = 0.10 | 95.0 -> 91.0 (-4.0) |
| p = 0.15 | 95.0 -> 87.0 (-8.0) |
| p = 0.20 | 95.0 -> 85.0 (-10.0) |

## What are the limitations of this transformation?

If the probability p is set too high, deleting characters can result in deleting whole words, which can alter the meaning of the sentence, e.g. negations.
