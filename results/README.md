# Preliminary results

Please report or open issue if you find any errors from the numbers below. Also it is not final results, and we are still working on completing morphological categories results on the word-level task. 

## Team details

| # | Name     | Authors                                                                      | University Affiliation(s)                                  |
|---|----------|------------------------------------------------------------------------------|------------------------------------------------------------|
| 1 | AUUH     | Aku Rouhe, Stig-Arne Grönroos,   Sami Virpioja, Mathias Creutz, Mikko Kurimo | Aalto University  / University of Helsinki                 |
| 2 | CLUZH    | Silvan Wehrli, Simon Clematide, Peter Makarov                                | University of Zurich                                       |
| 3 | DeepSPIN | Ben Peters, André Martins                                                    | Instituto de Telecomunicações / Instituto Superior Técnico |
| 4 | GU       | Lauren Levine                                                                | Georgetown University                                      |
| 5 | JB132    | Jan Bodnár                                                                   | Charles University                                         |
| 6 | NUM DI   | Tsolmon Zundui, Chinbat Avaajargal                                           | National University of Mongolia                            |
| 7 | Tü Seg   | Leander Girrbach                                                             | University of Tübingen                                     |

## Part1: Word-level task results
This table reports the f-measure performances of all submitted systems.
|   System   |  ces  |  eng  |  fra  |  ita  |  lat  |  rus  |  mon  |  hun  |  spa  | macro avg. |
|:----------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:----------:|
| AUUH_A     | 93.65 | 92.32 |     - |     - |     - |     - | 98.19 |     - |     - |      94.72 |
| AUUH_B     | 93.85 | 93.20 |     - |     - |     - |     - | 98.31 |     - |     - |      95.12 |
| AUUH_E     | 90.71 | 87.10 | 90.78 | 92.39 | 98.71 | 94.33 | 96.06 |     - |     - |      92.87 |
| AUUH_F     | 90.28 | 86.40 | 90.81 | 92.56 | 98.85 | 93.68 | 95.32 | 98.34 | 97.25 |      93.72 |
| BERT       | 20.42 | 23.06 | 12.66 |  9.08 |  8.84 | 13.81 | 14.58 | 24.00 | 16.57 |      15.89 |
| CLUZH      | 93.81 | 92.70 | 94.80 | 96.93 | 99.37 | 98.62 | 98.12 | 98.54 | 98.74 |      **96.85** |
| DeepSPIN-1 | 93.42 | 92.29 | 91.66 | 96.01 | 99.37 | 98.75 | 98.03 | 98.56 | 98.79 |      96.32 |
| DeepSPIN-2 | **93.88** | 93.39 | 95.29 | **97.47** | 99.36 | 99.30 | 98.00 | 98.68 | 99.02 |      97.15 |
| DeepSPIN-3 | 93.84 | **93.63** | **95.73** | 97.43 | **99.38** | **99.35** | **98.51** | **98.72** | **99.04** |      **97.29** |
| GU-1       |     - |     - | 83.44 | 88.69 |     - |     - |     - |     - |     - |      86.07 |
| GU-2       |     - |     - | 83.38 | 87.49 |     - |     - |     - |     - | 95.95 |      88.94 |
| JB132      | 64.65 | 65.43 | 46.20 | 33.44 | 91.39 | 50.55 | 57.82 | 72.64 | 43.39 |      58.39 |
| NUM DI     | 16.15 | 83.56 |     - | 89.55 |     - |     - | 85.59 | 95.91 |     - |      74.15 |
| Tü Seg     | 93.38 | 90.51 | 93.76 | 95.73 | 99.37 | 98.21 | 97.02 | 98.59 | 97.93 |      **96.06** |

![Overall f-score in part1](overall-word-f1-test.png)

Note: We are still working on completing morphological categories results on the word-level task. 

## Part2: Sentence-level task results

| Language  | F-measure | Submission |
|-----------|-----------|------------|
| Czech     |     91.99 |    CLUZH-3 |
| English   |     96.31 |     AUUH_B |
| Mongolian |     82.88 |    CLUZH-3 |

Czech
| system   |   precision |   recall |   f-measure |   distance |
|:---------|------------:|---------:|------------:|-----------:|
| AUUH_A   |       89.70 |    87.53 |       88.60 |       4.97 |
| AUUH_B   |       91.89 |    89.00 |       90.42 |       3.96 |
| AUUH_C   |       50.60 |    69.19 |       58.45 |      71.37 |
| AUUH_D   |       45.07 |    67.82 |       54.15 |      80.67 |
| AUUH_E   |       57.39 |    67.22 |       61.92 |      55.92 |
| AUUH_F   |       62.36 |    43.82 |       51.47 |      61.84 |
| BERT     |       38.47 |    31.45 |       34.61 |      17.88 |
| CLUZH-1  |       92.03 |    90.69 |       91.35 |       1.93 |
| CLUZH-2  |       92.41 |    91.13 |       91.76 |       1.87 |
| CLUZH-3  |       92.63 |    91.35 |       **91.99** |       1.80 |
| Tü Seg   |       89.52 |    88.42 |       88.97 |       2.50 |

![Czech](ces-sentence-test.png)

English
| system   |   precision |   recall |   f-measure |   distance |
|:---------|------------:|---------:|------------:|-----------:|
| AUUH_A   |       96.66 |    95.78 |       96.22 |       1.86 |
| AUUH_B   |       96.82 |    95.79 |       **96.31** |       1.39 |
| AUUH_C   |       84.77 |    71.67 |       77.67 |      19.13 |
| AUUH_D   |       93.29 |    83.41 |       88.07 |      10.58 |
| AUUH_E   |       95.23 |    76.82 |       85.04 |      12.36 |
| AUUH_F   |       91.50 |    74.84 |       82.34 |      13.30 |
| BERT     |       62.02 |    65.13 |       63.53 |       5.54 |
| CLUZH-1  |       89.74 |    89.20 |       89.47 |       9.86 |
| CLUZH-2  |       89.71 |    89.22 |       89.47 |       9.79 |
| CLUZH-3  |       89.83 |    89.25 |       89.54 |       9.84 |
| Tü Seg   |       87.83 |    89.58 |       88.69 |       1.78 |

![English](eng-sentence-test.png)


Mongolian
| system   |   precision |   recall |   f-measure |   distance |
|:---------|------------:|---------:|------------:|-----------:|
| AUUH_A   |       83.49 |    80.94 |       82.19 |       5.42 |
| AUUH_B   |       83.74 |    81.46 |       82.59 |       5.16 |
| AUUH_C   |       79.07 |    73.45 |       76.15 |      17.33 |
| AUUH_D   |       77.99 |    74.15 |       76.02 |      17.88 |
| AUUH_E   |       73.34 |    72.01 |       72.67 |      24.88 |
| AUUH_F   |       75.5  |    59.22 |       66.38 |      33.91 |
| BERT     |       19.82 |    29.2  |       23.62 |      29.19 |
| CLUZH-1  |       82.98 |    81.48 |       82.22 |       5.28 |
| CLUZH-2  |       83.29 |    81.83 |       82.55 |       5.19 |
| CLUZH-3  |       83.71 |    82.07 |       **82.88** |   5.1  |
| Tü Seg   |       69.59 |    67.55 |       68.55 |       9.85 |

![Mongolian](mon-sentence-test.png)
