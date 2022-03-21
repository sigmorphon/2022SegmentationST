#!/usr/bin/env python
"""
Official Evaluation Script for the SIGMORPHON 2022 Morpheme Segmentation Shared Task.
Returns precision, recall, f-measure, and mean Levenhstein distance.
Author: Khuyagbaatar Batsuren
Last Update: 03/14/2022
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


def print_numbers(precision, recall, distance, f_measure, cat="all"):
    print("\ncategory:\t" + cat)
    print("levenshtein:\t" + str(distance) + "\nprecision:\t" + str(precision))
    print("recall:\t" + str(recall) + "\nf-measure:\t" + str(f_measure))


def read_tsv(path, category):
    # tsv without header
    col_names = ["word", "segments"]
    if category:
        col_names.append("category")
    data = {name: [] for name in col_names}
    with open(path) as f:
        for line in f:
            fields = line.strip().split("\t")
            for name, field in zip(col_names, fields):
                if name == "segments":
                    field = field.replace(' @@', '|')
                data[name].append(field)
    return data


def n_correct(gold_segments, guess_segments):
    gold_seg_set = set(gold_segments.split("|"))
    return sum(guess_seg in gold_seg_set for guess_seg in guess_segments.split("|"))


def compute_stats(dists, overlaps, gold_lens, pred_lens):
    mean_dist = sum(dists) / len(dists)
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
    gold_data = read_tsv(args.gold, args.category)
    guess_data = read_tsv(args.guess, False)  # you only need the "segments" column

    # todo: make sure the data is well-formed

    # levenshtein distance can be computed separately for each (gold, guess)
    # pair
    dists = [distance(gold, guess)
             for gold, guess
             in zip(gold_data["segments"], guess_data["segments"])]

    # the values needed for P/R can also be broken down per-example
    n_overlaps = [n_correct(gold, guess)
                  for gold, guess
                  in zip(gold_data["segments"], guess_data["segments"])]
    gold_lens = [len(gold.split("|")) for gold in gold_data["segments"]]
    pred_lens = [len(guess.split("|")) for guess in guess_data["segments"]]
    overall_stats = compute_stats(dists, n_overlaps, gold_lens, pred_lens)
    print_numbers(**overall_stats)

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
                pred_lens_by_cat[cat]
            )
            print_numbers(**cat_stats, cat=cat)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='SIGMORPHON 2022 Morpheme Segmentation Shared Task Evaluation')
    parser.add_argument("--gold", help="Gold standard", required=True, type=str)
    parser.add_argument("--guess", help="Model output", required=True, type=str)
    parser.add_argument("--category", help="Morphological category", action="store_true")
    opt = parser.parse_args()
    main(opt)
