# Changing text to all caps or all lowercase letters

Author name: Lydia Nishimwe \
Author email: lydia.nishimwe@inria.fr \
Author Affiliation: [ALMAnaCH lab, Inria](https://files.inria.fr/almanach/index-en.html)

## What type of transformation is this?

This transformation takes a sentence and changes all its characters to either upper case or lower case.

Example:
```python
>>> trans = AllCapsOrLowercase(seed=0, max_outputs=5)
>>> trans.generate('See you tomorrow.')
>>> ['SEE YOU TOMORROW.',
 'SEE YOU TOMORROW.',
 'see you tomorrow.',
 'see you tomorrow.',
 'SEE YOU TOMORROW.']
```

## What tasks does it intend to benefit?

This perturbation would benefit all tasks which have a sentence/paragraph/document as input like text classification,
text generation, etc. 

## What are the limitations of this transformation?

This perturbation is useful for testing the robustness of NLP models trained with tokenizers that are case-sensitive. It is however rendered useless in cases where the tokenizers are case-insensitive, or where the text preprocessing pipeline includes lowercasing.
