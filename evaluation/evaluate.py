#!/usr/bin/env python
"""
Official Evaluation Script for the SIGMORPHON 2022 Morpheme Segmentation Shared Task.
Returns precision, recall, f-measure, and mean Levenhstein distance.
"""

from collections import defaultdict
import numpy as np


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


def print_numbers(stats_dict, cat="all"):
    print("\n")
    print("category:", cat)
    for stat_name, stat in sorted(stats_dict.items()):
        print("\t".join([stat_name, "{:.2f}".format(stat)]))


def read_tsv(path, level, category):
    # tsv without header
    col_names = ["word", "segments"]
    if category:
        col_names.append("category")
    data = {name: [] for name in col_names}
    first = True
    n = 0
    with open(path, encoding='utf-8') as f:
        for line in f:
            n+=1
            fields = line.rstrip("\n").split("\t")
            for name, field in zip(col_names, fields):
                if level == 'word':
                    if name == "segments":
                        field = field.replace(' @@', '|')
                        field = field.replace(' ', '|')
                    data[name].append(field)
                else:
                    if name == "segments":
                        field = field.replace(' @@', '|')
                    data[name].extend(field.split(' '))
            if first == True:
                if len(data['word']) != len(data['segments']):
                    print(line)
                    first = False
    return data, n

def n_correct(gold_segments, guess_segments):
    a = gold_segments.split("|")
    b = guess_segments.split("|")
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]

def compute_stats(dists, overlaps, gold_lens, pred_lens, n):
    mean_dist = sum(dists) / n
    total_overlaps = sum(overlaps)
    precision = 100 * total_overlaps / sum(pred_lens)
    recall = 100 * total_overlaps / sum(gold_lens)
    f_measure = 2 * precision * recall / (precision + recall)
    return {"distance": mean_dist, "precision": precision, "recall": recall, "f_measure": f_measure}


def stratify(sequence, labels):
    assert len(sequence) == len(labels)
    by_label = defaultdict(list)
    for label, value in zip(labels, sequence):
        by_label[label].append(value)
    return by_label


def main(args):
    gold_data = read_tsv(args.gold, args.level, args.category)[0]
    guess_data , n = read_tsv(args.guess, args.level, False)  # only second column is needed
    assert len(gold_data["segments"]) == len(guess_data["segments"]), \
        "gold and guess tsvs do not have the same number of entries"

    # levenshtein distance can be computed separately for each pair
    dists = [distance(gold, guess)
             for gold, guess
             in zip(gold_data["segments"], guess_data["segments"])]

    # the values needed for P/R can also be broken down per-example
    n_overlaps = [n_correct(gold, guess)
                  for gold, guess
                  in zip(gold_data["segments"], guess_data["segments"])]
    gold_lens = [len(gold.split("|")) for gold in gold_data["segments"]]
    pred_lens = [len(guess.split("|")) for guess in guess_data["segments"]]

    if args.category:
        categories = gold_data["category"]
        # stratify by category
        dists_by_cat = stratify(dists, categories)
        overlaps_by_cat = stratify(n_overlaps, categories)
        gold_lens_by_cat = stratify(gold_lens, categories)
        pred_lens_by_cat = stratify(pred_lens, categories)

        for cat in sorted(dists_by_cat):
            cat_stats = compute_stats(
                dists_by_cat[cat],
                overlaps_by_cat[cat],
                gold_lens_by_cat[cat],
                pred_lens_by_cat[cat],
                len(dists_by_cat[cat])
            )
            print_numbers(cat_stats, cat=cat)

    overall_stats = compute_stats(dists, n_overlaps, gold_lens, pred_lens, n)
    print_numbers(overall_stats)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='SIGMORPHON 2022 Morpheme Segmentation Shared Task Evaluation')
    parser.add_argument("--gold", help="Gold standard", required=True, type=str)
    parser.add_argument("--guess", help="Model output", required=True, type=str)
    parser.add_argument("--level", help="Task level: word or sentence", required=True, choices=['word', 'sentence'], type = str)
    parser.add_argument("--category", help="Morphological category", action="store_true")
    opt = parser.parse_args()
    main(opt)
