# Character Repetition

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This perturbation emulates some of the marks of expressiveness found in user-generated content (UGC) by repeating certain characters. 
*All* sentence-ending punctuation (.?!) are repeated, while letters are selected for repetition with a probability `prob_rep`. 
Digits, whitespace, and other punctuation and characters are not repeated.
The number of repetitions for a selected character is sampled from a Poisson distribution of parameter `n_rep`.

Example:
```python
>>> trans = CharacterRepetion(seed=0, max_outputs=5, prob_rep=0.5, n_rep=3)
>>> trans.generate("That's so cool!")
>>> ["That'ssssss so cool!!!!",
 "Thhhhat's so coool!",
 "TTTThhatt'sss sooo coool!!",
 "Thaaat's sssso coooooool!!!!!!!",
 "Thhhat's so coooooool!!!"]
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## Evaluation

The impact on the performance of RoBERTa (`textattack/roberta-base-imdb`) on the IMDB dataset (20% test split):

| Data perturbation level | Accuracy drop |
|---|---|
| prob_rep = 0.05 | 95.0 -> 92.0 (-3.0) |
| prob_rep = 0.10 | 95.0 -> 90.0 (-5.0) |
| prob_rep = 0.15 | 95.0 -> 84.0 (-11.0) |
| prob_rep = 0.20 | 95.0 -> 81.0 (-14.0) |

## Related work

This perturbation performs two of the phenomena of marks of expressiveness in UGC described by Seddah et al. (2012):
1. Punctuation transgression: the overuse of strong punctuation marks, and
2. Graphemic stretching: the repetition of certain letters in a word.

Citation:
```bibtex
@inproceedings{seddah-etal-2012-french,
    title = "The {F}rench {S}ocial {M}edia {B}ank: a Treebank of Noisy User Generated Content",
    author = "Seddah, Djam{\'e}  and
      Sagot, Benoit  and
      Candito, Marie  and
      Mouilleron, Virginie  and
      Combet, Vanessa",
    editor = "Kay, Martin  and
      Boitet, Christian",
    booktitle = "Proceedings of {COLING} 2012",
    month = dec,
    year = "2012",
    address = "Mumbai, India",
    publisher = "The COLING 2012 Organizing Committee",
    url = "https://aclanthology.org/C12-1149",
    pages = "2441--2458",
}
```

## What are the limitations of this transformation?

Repeating all full stops will affect those that mark abbreviations (e.g. `3 p.m.` -> `3 p....m...`), which people tend not to do.
