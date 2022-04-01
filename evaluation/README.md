The official evaluation script lives in this directory. We have provided sample output from the baseline model on the development data in ../baseline/. You may run the baseline as shown in the examples below. For the baseline, we use the pretrained `BertTokenizer` models from [huggingface](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer). 

Word-level Task Evaluation:

``
python evaluate.py --level word --guess ../baseline/eng.word.dev.bert.tsv --gold ../data/eng.word.dev.tsv --category
``

```
category: 000
distance        2.11
f_measure       2.96
precision       2.02
recall  5.55


category: 001
distance        1.42
f_measure       53.97
precision       46.60
recall  64.11


category: 010
distance        2.75
f_measure       28.97
precision       25.29
recall  33.90


category: 011
distance        2.96
f_measure       37.86
precision       36.85
recall  38.93


category: 100
distance        2.73
f_measure       14.87
precision       12.16
recall  19.14


category: 101
distance        1.51
f_measure       50.83
precision       51.57
recall  50.12


category: 110
distance        3.31
f_measure       25.53
precision       24.92
recall  26.17


category: 111
distance        3.22
f_measure       31.22
precision       34.81
recall  28.30


category: all
distance        2.69
f_measure       24.28
precision       20.99
recall  28.79
```

Sentence-level Task Evaluation:

``
python evaluate.py --level sentence --guess ../baseline/eng.sentence.dev.bert.tsv --gold ../data/eng.sentence.dev.tsv
``

```
category: all
distance        5.81
f_measure       63.70
precision       63.05
recall  64.37
```

```
python evaluate_word.py --level sentence --guess ../baseline/mon.sentence.dev.bert.tsv --gold ../data/mon.sentence.dev.tsv

category: all
distance        28.88
f_measure       23.49
precision       19.58
recall  29.33

evaluate_word.py --level sentence --guess ../baseline/ces.sentence.dev.bert.tsv --gold ../data/ces.sentence.dev.tsv


category: all
distance        21.01
f_measure       32.89
precision       36.36
recall  30.02
```
