"""Expected reciprocal rank under random tie-breaking (a metric that scores many candidates 0 is then not penalised
below a random order, as tie-averaged ranks would do)."""
import numpy as np


def exp_rr(scores, target):
    if isinstance(scores, dict):
        v = scores[target]; vals = np.fromiter(scores.values(), dtype=float)
    else:
        vals = np.asarray(scores, dtype=float); v = vals[target]
    better = int((vals > v).sum()); ties = int((vals == v).sum())
    return float(np.mean([1.0 / k for k in range(better + 1, better + ties + 1)]))


def avg_rank(scores, target):
    if isinstance(scores, dict):
        v = scores[target]; vals = np.fromiter(scores.values(), dtype=float)
    else:
        vals = np.asarray(scores, dtype=float); v = vals[target]
    return 1 + float((vals > v).sum()) + (float((vals == v).sum()) - 1) / 2
