The official evaluation script lives in this directory. We have provided sample output from the baseline model on the development data in ../baseline/. You may run the baseline as shown in the examples below. For the baseline, we use the pretrained `BertTokenizer` models from [huggingface](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer). 

Word-level Task Evaluation:

``
python evaluate.py --guess ../baseline/eng.word.dev.bert.tsv --gold ../data/eng.word.dev.tsv --category
``

```
category:       101
levenshtein:    1.56
precision:      51.59
recall: 48.8
f-measure:      50.16

category:       111
levenshtein:    3.28
precision:      34.86
recall: 27.45
f-measure:      30.71

category:       011
levenshtein:    3.35
precision:      32.77
recall: 27.16
f-measure:      29.7

category:       010
levenshtein:    2.76
precision:      25.31
recall: 33.91
f-measure:      28.99

category:       000
levenshtein:    2.16
precision:      2.42
recall: 6.63
f-measure:      3.55

category:       110
levenshtein:    3.31
precision:      24.95
recall: 26.21
f-measure:      25.56

category:       001
levenshtein:    1.66
precision:      43.76
recall: 49.5
f-measure:      46.45

category:       100
levenshtein:    2.79
precision:      12.49
recall: 19.58
f-measure:      15.25

category:       all
levenshtein:    2.72
precision:      20.86
recall: 28.28
f-measure:      24.01
```
