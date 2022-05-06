# SIGMORPHON 2022 Shared Task on Morpheme Segmentation

Morphemes (prefixes, suffixes, root words) are linguistic descriptions, defined as the smallest meaningful unit of words. Our proposed shared task is morpheme
segmentation that converts a text into a sequence of morphemes. In order to prepare a dataset for this task, we integrated all basic types of morphological
databases (including [UniMorph](https://github.com/unimorph) (Kirov et al., 2018b; McCarthy et al., 2020) – inflectional morphology; [MorphyNet](https://github.com/kbatsuren/MorphyNet) (Batsuren et al., 2021) – derivational morphology; Universal Dependencies (Nivre et al., 2017) and ten editions of Wiktionary – compound morphology and root words). In the future, we expect the NLP community will
benefit a lot by innovating subword-based tokenization with this task. This shared task has two parts:

+ ***Part 1***: [Word-level morpheme segmentation](https://github.com/sigmorphon/2022SegmentationST#)
+ ***Part 2***: [Sentence-level morpheme segmentation](https://github.com/sigmorphon/2022SegmentationST#)

Please join our [Google Group](https://groups.google.com/forum/#!forum/sigmorphon-morpheme-segmentation/join) to stay up to date.
Click here to [register for the task](https://forms.gle/J3vsp11n338XbpYD6)!

Please open the issues if you have any questions.

Two subtasks will be scored separately. Participant teams may submit as many systems as they want to as many subtasks as they want.

## Part 1: Word-level Morpheme Segmentation
At the word level, participants will be asked to segment a given word into a sequence of morphemes. Input words contains all types of word forms: root words, derived words, inflected words, and compound words.

### Data
Training and development data are UTF-8-encoded tab-separated values files. Each example occupies a single line and consists of input word, the corresponding morpheme sequence, and the corresponding morphological category. The following shows three lines of English data:
    
    inaccuracies  in @@accurate @@cy @@s  110
    dictionary  dictionary  000
    screwdriver screw @@drive @@er  011

<i> Note: The third column as the morphological category is an optional feature that can only be used to oversample or undersample training data.</i>

First example is a derived word with prefix (in-) and suffixes (-cy and -s), and second example is a root word. Third example is a compound word. In the test datasets, we will provide only first column of data as input words. 

### Languages
Development languages are:
1.  `ces`: Czech
2.  `eng`: English
3.  `fra`: French
4.  `hun`: Hungarian
5.  `spa`: Spanish
6.  `ita`: Italian
7.  `lat`: Latin
8.  `rus`: Russian

Surprise language is:

9. `mon`: Mongolian

### Data Statistics
| word class | English | Spanish | Hungarian | French | Italian | Russian | Czech | Latin | Mongolian |
|:-----:|---------|---------|-----------|--------|---------|---------|-------|-------|-------|
|  100  |  126544 |  502229 |    410662 | 105192 |  253455 |  221760 |     - |   831991 |  7266 |
|  010  |  203102 |   18449 |     24923 |  67983 |   41092 |   72970 |     - |   0 |  2201 |
|  101  |   13790 |     458 |    101189 |    478 |     317 |    1909 |     - |   0 |  35 |
|  000  |  101938 |   15843 |      6952 |  13619 |   21037 |    2921 |     - |   50338 |  1604 |
|  011  |    5381 |      82 |      1654 |    506 |     140 |     328 |     - |   0 |  0 |
|  110  |  106570 |  346862 |    323119 | 126196 |  237104 |  481409 |     - |   0 |  7855 |
|  001  |   16990 |     248 |      3320 |   1684 |     431 |     259 |     - |   0 |  5 |
|  111  |    3059 |     343 |     54279 |    186 |     158 |    2658 |     - |   0 |  0 |
| total words |  577374 |  884514 |    926098 | 382797 |  553734 |  784214 | 38682 |   882329 |  18966 |

### Word category description
For some of the development languages, we are providing the word categories so that participant can deal with imbalanced situation of morphological categories. 

| word class | Description                      | English example (input ==> output)     |
|------------|----------------------------------|----------------------------------------|
| 100        | Inflection only                  | played ==> play @@ed                   |
| 010        | Derivation only                  | player ==> play @@er                   |
| 101        | Inflection and Compound          | wheelbands ==> wheel @@band @@s        |
| 000        | Root words                       | progress ==> progress                  |
| 011        | Derivation and Compound          | tankbuster ==> tank @@bust @@er        |
| 110        | Inflection and Derivation        | urbanizes ==> urban @@ize @@s          |
| 001        | Compound only                    | hotpot ==> hot @@pot                   |
| 111        | Inflection, Derivation, Compound | trackworkers ==> track @@work @@er @@s |

### Baseline results

The following table shows the word-level task results of pretrained `BertTokenizer` on English. This pretrained model was employed from [HuggingFace](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer). 

| word class | inflection | derivation | compound |   R   |   P   |   F1  | lev. distance |
|:----------:|:----------:|:----------:|:--------:|:-----:|:-----:|:-----:|:-------------:|
|     001    |     no     |     no     |    yes   | 64.11 | 46.60 | 53.97 |      1.42     |
|     101    |     yes    |     no     |    yes   | 50.12 | 51.57 | 50.83 |      1.51     |
|     011    |     no     |     yes    |    yes   | 38.93 | 36.85 | 37.86 |      2.96     |
|     111    |     yes    |     yes    |    yes   | 28.30 | 34.81 | 31.22 |      3.22     |
|     010    |     no     |     yes    |    no    | 33.90 | 25.29 | 28.97 |      2.75     |
|     110    |     yes    |     yes    |    no    | 26.17 | 24.92 | 25.53 |      3.31     |
|     100    |     yes    |     no     |    no    | 19.14 | 12.16 | 14.87 |      2.73     |
|     000    |     no     |     no     |    no    |  5.55 |  2.02 |  2.96 |      2.11     |
|    total   |      -     |      -     |     -    | 28.79 | 20.99 | 24.28 |      2.69     |

## Part 2: Sentence-level Morpheme Segmentation
At the sentence level, participating systems are expected to predict a sequence of morphemes for a given sentence.
The following shows two lines of English data:

    Six weeks of basic training . Six week @@s of base @@ic train @@ing .
    Fistfights , please . Fist @@fight @@s , please .

The following shows two lines of Mongolian data:

    Гэрт эмээ хоол хийв . Гэр @@т эмээ хоол хийх @@в .
    Би өдөр эмээ уусан . Би өдөр эм @@ээ уух @@сан .

In above example, `эмээ` is a hononym of two different words, first means a `grandmother` and second is `medicine`. Depending on the context, the second homonym word is inflectional form of `medicine` and it is segmentable.

### Languages
Development languages are:
1.  `ces`: Czech
2.  `eng`: English
3.  `mon`: Mongolian

### Data Statistics

|           | train | dev  | test |
|-----------|-------|------|------|
| Czech     | 1000  | 500  | 500  |
| English   | 11007 | 1783 | 1846 |
| Mongolian | 1000  | 500  | 600  |

### Baseline results
| Language  | Precison | Recall | F-measure | Lev. distance |
|-----------|:--------:|:------:|:---------:|:-------------:|
| Czech     |   36.76  |  30.35 |   33.25   |     21.01     |
| English   |   63.68  |  65.77 |   64.71   |      5.50     |
| Mongolian |   20.00  |  29.95 |   23.99   |     28.86     |

## Evaluation

We will provide python evaluation scripts, reporting the following evaluation measures:

- Precision - fraction of correctly predicted morphemes on all predicted morphemes
- Recall - ratio of correctly predicted morphemes on all gold morphemes 
- F-measure - the harmonic mean of the precision and recall
- Edit distance - average Levenshtein distance between the predicted output and the gold instance.

## Submission

Please submit your team's results to khuyagbaatar.b@gmail.com CCing your teammates by May 13rd, 2022. Each submission should be a .tar.gz or .zip file.

## Timeline

### Development Phase

- February 23, 2022: Training splits for development languages are released at https://github.com/sigmorphon/2022SegmentationST/tree/v0.2
- February 28, 2022: Development splits for development languages are released at https://github.com/sigmorphon/2022SegmentationST/tree/v0.2
- March 15, 2022: Evaluation tool of word-level task (English baseline results included) is released at https://github.com/sigmorphon/2022SegmentationST/tree/v0.2
- March 22, 2022: Evaluation tool of sentence-level task is released at [`/evaluation`](https://github.com/sigmorphon/2022SegmentationST/tree/main/evaluation)
- March 29, 2022: Full baseline results are released at [`/baseline`](https://github.com/sigmorphon/2022SegmentationST/tree/main/baseline)

### Generalization Phase

- ~~April 8~~ April 18, 2022: Training and development splits for surprise languages released [`/data/surprise`](https://github.com/sigmorphon/2022SegmentationST/tree/main/data/surprise)

### Evaluation Phase

- ~~April 15~~ April 29, 2022: Test splits for development and surprise languages are released at [`/data`](https://github.com/sigmorphon/2022SegmentationST/tree/main/data)
- ~~April 29~~ May 13, 2022: Participants' submissions due.

### Write-up Phase

- ~~May 13~~ May 27, 2022: Participants' draft system description papers due.
- ~~May 20~~ June 3, 2022: Participants' camera-ready system description papers due.

## Organizers

- Khuyagbaatar Batsuren (National University of Mongolia)
- Gábor Bella (University of Trento)
- Aryaman Arora (Georgetown University)
- Viktor Martinović (University of Vienna)
- Kyle Gorman (Graduate center, City University Of New York)
- Zdeněk Žabokrtský (Charles University)
- Amarsanaa Ganbold (National University of Mongolia)
- Šárka Dohnalová (Charles University)
- Magda Ševčíková (Charles University)
- Kateřina Pelegrinová (University of Ostrava)
- Fausto Giunchiglia (University of Trento)
- Ryan Cotterell (ETH Zürich)
- Ekaterina Vylomova (University of Melbourne)

## License
The data is released under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/legalcode) inherited from Wiktionary itself.

## References

Kirov, C., Cotterell, R., Sylak-Glassman, J., Walther, G., Vylomova, E., Xia, P., Faruqui, M., Mielke, S., McCarthy, A., Kübler, S., Yarowsky, D., Eisner, J., and Hulden, M. (2018). [UniMorph 2.0: Universal Morphology](https://arxiv.org/abs/1810.11101). Proceedings of LREC 2018.

McCarthy, A.D., Kirov, C., Grella, M., Nidhi, A., Xia, P., Gorman, K., Vylomova, E., Mielke, S.J., Nicolai, G., Silfverberg, M. and Arkhangelskij, T., (2020). [UniMorph 3.0: Universal Morphology.](https://aclanthology.org/2020.lrec-1.483/). Proceedings of LREC 2020.

Batsuren, K., Bella, G. and Giunchiglia, F., (2021). [MorphyNet: a Large Multilingual Database of Derivational and Inflectional Morphology.](https://aclanthology.org/2021.sigmorphon-1.5/) In Proceedings of SIGMORPHON 2021 (pp. 39-48).

Nivre, J., Agić, Ž., Ahrenberg, L., Antonsen, L., Aranzabe, M.J., Asahara, M., Ateyah, L., Attia, M., Atutxa, A., Augustinus, L. and Badmaeva, E., (2017). [Universal Dependencies 2.1.](https://hal.inria.fr/hal-01682188?gathStatIcon=true)

