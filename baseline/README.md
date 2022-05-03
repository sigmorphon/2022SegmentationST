# Baseline results

## Word-level task

| # | Language  | precision | recall | f-measure | lev. distance        |
|:-:|-----------|:---------:|:------:|:---------:|:--------------------:|
| 1 | English   |   20.99   |  28.79 |   24.28   |         2.69         |
| 2 | Hungarian |   20.88   |  27.81 |   23.85   |         3.54         |
| 3 | Czech     |   22.10   |  19.72 |   20.84   |         2.94         |
| 4 | Spanish   |   15.76   |  17.91 |   16.76   |         5.20         |
| 5 | Russian   |   13.23   |  14.13 |   13.67   |         7.62         |
| 6 | French    |   11.08   |  14.00 |   12.37   |         4.32         |
| 7 | Italian   |    8.12   |  10.54 |    9.18   |         5.35         |
| 8 | Latin     |    6.76   |  13.17 |    8.94   |         4.14         |

### Categorical details by language

Russian - Multilingual BERT Tokenizer (cased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    6.77   |  16.10 |    9.53   |   1.38   |
|    001   |     no     |     no     |    yes   |   12.00   |  23.08 |   15.79   |   2.92   |
|    010   |     no     |     yes    |    no    |   14.39   |  21.71 |   17.31   |   4.62   |
|    011   |     no     |     yes    |    yes   |   14.74   |  18.25 |   16.31   |   7.12   |
|    100   |     yes    |     no     |    no    |    6.85   |  10.19 |    8.19   |   5.85   |
|    101   |     yes    |     no     |    yes   |   10.68   |  15.99 |   12.80   |   6.06   |
|    110   |     yes    |     yes    |    no    |   15.89   |  14.55 |   15.19   |   8.94   |
|    111   |     yes    |     yes    |    yes   |    7.70   |  7.63  |    7.66   |   9.61   |
|    all   |      -     |      -     |     -    |   13.23   |  14.13 |   13.67   |   7.62   |

Italian - Multilingual BERT Tokenizer (cased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    2.70   |  6.97  |    3.89   |   1.59   |
|    001   |     no     |     no     |    yes   |   14.67   |  23.40 |   18.03   |   3.11   |
|    010   |     no     |     yes    |    no    |   14.11   |  19.16 |   16.25   |   3.77   |
|    011   |     no     |     yes    |    yes   |   10.53   |  13.95 |   12.00   |   5.79   |
|    100   |     yes    |     no     |    no    |    3.32   |  5.49  |    4.14   |   4.87   |
|    101   |     yes    |     no     |    yes   |   11.76   |  13.19 |   12.44   |   4.47   |
|    110   |     yes    |     yes    |    no    |   11.37   |  11.97 |   11.66   |   6.56   |
|    111   |     yes    |     yes    |    yes   |   11.11   |  10.64 |   10.87   |   7.09   |
|    all   |      -     |      -     |     -    |    8.12   |  10.54 |    9.18   |   5.35   |

Hungarian - Multilingual BERT Tokenizer (cased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    2.61   |  7.36  |    3.85   |   1.83   |
|    001   |     no     |     no     |    yes   |    9.89   |  20.37 |   13.31   |   2.78   |
|    010   |     no     |     yes    |    no    |   22.96   |  31.70 |   26.63   |   2.84   |
|    011   |     no     |     yes    |    yes   |   19.01   |  25.56 |   21.80   |   3.60   |
|    100   |     yes    |     no     |    no    |   16.75   |  27.17 |   20.72   |   2.97   |
|    101   |     yes    |     no     |    yes   |   17.76   |  27.27 |   21.51   |   3.92   |
|    110   |     yes    |     yes    |    no    |   25.53   |  28.36 |   26.87   |   3.88   |
|    111   |     yes    |     yes    |    yes   |   23.93   |  27.89 |   25.76   |   4.66   |
|    all   |      -     |      -     |     -    |   20.88   |  27.81 |   23.85   |   3.54   |

French - Multilingual BERT Tokenizer (cased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    6.55   |  16.23 |    9.33   |   1.48   |
|    001   |     no     |     no     |    yes   |   30.63   |  57.44 |   39.96   |   2.85   |
|    010   |     no     |     yes    |    no    |   12.60   |  18.44 |   14.97   |   3.81   |
|    011   |     no     |     yes    |    yes   |   16.31   |  22.22 |   18.81   |   5.45   |
|    100   |     yes    |     no     |    no    |    6.08   |  9.33  |    7.36   |   3.85   |
|    101   |     yes    |     no     |    yes   |   15.06   |  16.45 |   15.72   |   5.06   |
|    110   |     yes    |     yes    |    no    |   14.15   |  14.32 |   14.23   |   5.30   |
|    111   |     yes    |     yes    |    yes   |    6.67   |  5.68  |    6.13   |   8.37   |
|    all   |      -     |      -     |     -    |   11.08   |  14.00 |   12.37   |   4.32   |

Spanish - Multilingual BERT Tokenizer (cased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    5.19   |  12.82 |    7.39   |   1.47   |
|    001   |     no     |     no     |    yes   |    9.89   |  15.52 |   12.08   |   2.76   |
|    010   |     no     |     yes    |    no    |   16.02   |  21.29 |   18.28   |   3.37   |
|    011   |     no     |     yes    |    yes   |    5.26   |  5.26  |    5.26   |   4.83   |
|    100   |     yes    |     no     |    no    |   11.52   |  15.79 |   13.32   |   4.62   |
|    101   |     yes    |     no     |    yes   |   10.57   |  11.82 |   11.16   |   5.59   |
|    110   |     yes    |     yes    |    no    |   20.21   |  19.29 |   19.74   |   6.11   |
|    111   |     yes    |     yes    |    yes   |   28.92   |  28.57 |   28.74   |     7    |
|    all   |      -     |      -     |     -    |   15.76   |  17.91 |   16.76   |    5.2   |

English - BERT Tokenizer (uncased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    2.02   |  5.55  |    2.96   |   2.11   |
|    001   |     no     |     no     |    yes   |   46.60   |  64.11 |   53.97   |   1.42   |
|    010   |     no     |     yes    |    no    |   25.29   |  33.90 |   28.97   |   2.75   |
|    011   |     no     |     yes    |    yes   |   36.85   |  38.93 |   37.86   |   2.96   |
|    100   |     yes    |     no     |    no    |   12.16   |  19.14 |   14.87   |   2.73   |
|    101   |     yes    |     no     |    yes   |   51.57   |  50.12 |   50.83   |   1.51   |
|    110   |     yes    |     yes    |    no    |   24.92   |  26.17 |   25.53   |   3.31   |
|    111   |     yes    |     yes    |    yes   |   34.81   |  28.30 |   31.22   |   3.22   |
|    all   |      -     |      -     |     -    |   20.99   |  28.79 |   24.28   |   2.69   |

Mongolian - BERT Tokenizer (uncased)

| category | inflection | derivation | compound | precision | recall | f_measure | distance |
|:--------:|:----------:|:----------:|:--------:|:---------:|:------:|:---------:|:--------:|
|    000   |     no     |     no     |    no    |    1.26   |  3.75  |    1.89   |   2.14   |
|    001   |     no     |     no     |    yes   |    -      |  -     |    -      |   -      |
|    010   |     no     |     yes    |    no    |    4.86   |  9.62  |    6.46   |   4.45   |
|    011   |     no     |     yes    |    yes   |    -      |  -     |    -      |   -      |
|    100   |     yes    |     no     |    no    |    6.22   | 12.52  |    8.31   |   3.50   |
|    101   |     yes    |     no     |    yes   |    0.00   |  0.00  |    0.00   |   5.33   |
|    110   |     yes    |     yes    |    no    |    6.45   | 10.18  |    7.90   |   5.94   |
|    111   |     yes    |     yes    |    yes   |    -      |  -     |    -      |   -      |
|    all   |      -     |      -     |     -    |    5.89   | 10.59  |    7.57   |   4.51   |

## Sentence-level task

| Language  | Precison | Recall | F-measure | Lev. distance |
|-----------|:--------:|:------:|:---------:|:-------------:|
| Czech     |   36.76  |  30.35 |   33.25   |     21.01     |
| English   |   63.68  |  65.77 |   64.71   |      5.50     |
| Mongolian |   20.00  |  29.95 |   23.99   |     28.86     |

