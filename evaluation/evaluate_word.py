#!/usr/bin/env python
"""
Official Evaluation Script for the SIGMORPHON 2022 Morpheme Segmentation Shared Task.
Returns precision, recall, f-measure, and mean Levenhstein distance.
Author: Khuyagbaatar Batsuren
Last Update: 03/14/2022
"""

import numpy as np
import codecs

def distance(str1, str2):
    """Simple Levenshtein implementation for evalm."""
    m = np.zeros([len(str2) + 1, len(str1) + 1], dtype=int)
    for x in range(1, len(str2) + 1):
        m[x, 0] = m[x - 1, 0] + 1
    for y in range(1, len(str1) + 1):
        m[0, y] = m[0, y - 1] + 1
    for x in range(1, len(str2) + 1):
        for y in range(1, len(str1) + 1):
            if str1[y-1] == str2[x-1]:
                dg = 0
            else:
                dg = 1
            m[x, y] = min(m[x - 1, y] + 1, m[x, y - 1] + 1, m[x - 1, y - 1] + dg)
    return m[len(str2), len(str1)]

def read(fname, flag):
    """ read file name """
    D = {}
    C = {}
    with codecs.open(fname, 'rb', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if flag:
              lemma, segments, tag = line.split("\t")
              C[lemma] = tag
            else:
              lemma, segments = line.split("\t")[0:2]
            D[lemma] = segments.replace(' @@','|')
    return D, C

def printNumbers(T):
  answers, D_cat = T[0], T[1]
  cat_set = set(D_cat)
  for cat in cat_set:
    print("\ncategory:\t" +cat)
    print ("levenshtein:\t"+str(answers[cat]['distance'])+"\nprecision:\t"+str(answers[cat]['precision']))
    print ("recall:\t"+str(answers[cat]['recall'])+"\nf-measure:\t"+str(answers[cat]['fmeasure']))

def eval_form(gold, guess, category):
    """ compute average accuracy and edit distance for word-level task """
    correct, dist, total = {}, {}, {}
    tp, fp, total_m, total_g = {}, {}, {}, {}
    answers = {}
    if len(category) < 1:
      category['']='all'
    for cat in category.values():
      tp[cat] = .0
      dist[cat] = .0
      total_m[cat] = .0
      total_g[cat] = .0
      total[cat] = .0
    for lemma, str1 in gold.items():
      str2 = u"" # empty string if no guess
      cat = "all"
      if lemma in category:
        cat = category[lemma]
      if (cat in total) is False:
        total[cat] = .0
      if lemma in guess:
        str2 = guess[lemma]
        gold_set = set(str1.split('|'))
        guess_list = str2.split('|')
        if (cat in total_g) is False:
          total_g[cat] = .0
        if (cat in total_m) is False:
          total_m[cat] = .0
        total_g[cat] += len(str2.split('|'))
        total_m[cat] += len(str1.split('|'))
        
      for b in guess_list:
          if b in gold_set:
            if (cat in tp) is False:
              tp[cat]=.0
            tp[cat] += 1
      dist[cat] += distance(str1, str2)
      total[cat] += 1

    for cat in total.keys():
      answers[cat] = {}
      answers[cat]['distance'] =round(dist[cat]/total[cat],2)
      answers[cat]['precision'] = round((tp[cat]/total_g[cat])*100,2)
      answers[cat]['recall'] = round((tp[cat]/total_m[cat])*100,2)
      answers[cat]['fmeasure'] = round((2*answers[cat]['precision']*answers[cat]['recall']) / (answers[cat]['precision']+answers[cat]['recall']),2)
    return (answers, total.keys())



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='SIGMORPHON 2022 Morpheme Segmentation Shared Task Evaluation')
    parser.add_argument("--gold", help="Gold standard", required=True, type=str)
    parser.add_argument("--guess", help="Model output", required=True, type=str)
    parser.add_argument("--category", help="Morphological category", action="store_true")
    args = parser.parse_args()    

    D_gold, D_cat = read(args.gold, args.category)
    D_guess = read(args.guess, False)[0]
    if args.category:
      printNumbers(eval_form(D_gold, D_guess,D_cat))
    printNumbers(eval_form(D_gold, D_guess,{}))
