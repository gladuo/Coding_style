# coding=utf-8
from __future__ import division

# FILE = "./data.in"

# CNT = 0


def f1(tp, fp, tn, fn):
    if (tp + fp) == 0:
        return 0
    if (tp + fn) == 0:
        return 0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
        # global CNT
        # CNT += 1
        # print CNT
        return 0
    ans = 2 * precision * recall / (precision + recall)
    return ans


def ws_fscore(FILE):
    tp = tn = fp = fn = 0
    with open(FILE, "r") as f:
        for line in f.readlines():
            args = map(int, line.split("\t")[2:])
            real = args[0]
            expected = args[2]
            real_ln = args[1]
            if real_ln == 1:
                continue
            else:
                if expected == -1:
                    if real == 0:
                        tn += 1
                    elif real == 1:
                        tp += 1
                elif expected == 0:
                    if real == 0:
                        tn += 1
                    elif real == 1:
                        fp += 1
                else:
                    if real == 0:
                        fn += 1
                    elif real == 1:
                        tp += 1

    return f1(tp, fp, tn, fn)


def ln_fscore(FILE):
    tp = tn = fp = fn = 0
    with open(FILE, "r") as f:
        for line in f.readlines():
            args = map(int, line.split("\t")[2:])
            real = args[1]
            expected = args[3]

            if expected == -1:
                if real == 0:
                    tn += 1
                elif real == 1:
                    tp += 1
            elif expected == 0:
                if real == 0:
                    tn += 1
                elif real == 1:
                    fp += 1
            else:
                if real == 0:
                    fn += 1
                elif real == 1:
                    tp += 1

    return f1(tp, fp, tn, fn)


def in_fscore(FILE):
    max_ws = 0
    max_level = 0
    indent = 0
    with open(FILE, "r") as f:
        for line in f.readlines():
            args = map(int, line.split("\t")[2:])
            if args[0] != 1000000000:
                max_ws = max(max_ws, args[0])
            max_level = max(max_level, args[4])

    vote = [0] * (max_ws+1)
    for i in range(1, max_ws+1):
        with open(FILE, "r") as f:
            for line in f.readlines():
                args = map(int, line.split("\t")[2:])
                real_ws = args[0]
                real_ln = args[1]
                expected_ln = args[3]
                expected_level = args[4]
                if expected_ln == 1 and expected_ln == real_ln:
                    if i * expected_level == real_ws:
                        vote[i] += 1

    max_fit = 0
    for i in range(1, max_ws+1):
        if vote[i] > max_fit:
            max_fit = vote[i]
            indent = i

    rec_real = [0] * (max_level+2)
    rec_expected = [0] * (max_level+2)
    rec_fit = [0] * (max_level+2)
    with open(FILE, "r") as f:
        for line in f.readlines():
            args = map(int, line.split("\t")[2:])
            real_ws = args[0]
            real_ln = args[1]
            expected_ln = args[3]
            expected_level = args[4]

            if real_ln == 1 and real_ln == expected_ln:
                real_level = real_ws // indent
                if real_ws % indent == 0:
                    if real_level >= max_level + 1:
                        real_level = max_level + 1
                    rec_real[real_level] += 1
                    rec_expected[expected_level] += 1
                    if real_level == expected_level:
                        rec_fit[real_level] += 1
                else:
                    rec_real[max_level+1] += 1

        sum_tp = 0
        for i in range(0, max_level+1):
            sum_tp += rec_fit[i]

        ans = 0
        for i in range(0, max_level+2):
            tp = rec_fit[i]
            fp = rec_real[i] - tp
            fn = rec_expected[i] - tp
            if sum_tp == 0:
                break  # 此处break了
            ans += f1(tp, fp, 0, fn) * tp / sum_tp

        return ans


def cal(FILE):
    print "F1 score"
    print "White space:", ws_fscore(FILE)
    print "Next line:", ln_fscore(FILE)
    print "Indent:", in_fscore(FILE)


if __name__ == '__main__':
    cal(FILE='./data.in')
