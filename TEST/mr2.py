"""
=============================================================================
METAMORPHIC RELATION 2 (MR2): TRANSLATION / SHIFT INVARIANCE
File: mr2.py
Formula: manhattan_distance(A, B) == manhattan_distance(A + c, B + c)
=============================================================================
"""

import math

# Source Test Inputs (2D vectors as required)
T1 = [12, 34]
T2 = [5, 10]
T3 = [-3, 8]
T4 = [0, 0]
T5 = [100, 250]

# 5 Metamorphic Test Groups for MR2
MR2_MTGS = [
    {
        "name": "MTG 2.1",
        "source": (T1, T2),
        "shift_c": 10,
        "follow_up": ([x + 10 for x in T1], [y + 10 for y in T2]),
        "relation_str": "dist(T1, T2) == dist(T1+10, T2+10)",
    },
    {
        "name": "MTG 2.2",
        "source": (T1, T3),
        "shift_c": -25,
        "follow_up": ([x - 25 for x in T1], [y - 25 for y in T3]),
        "relation_str": "dist(T1, T3) == dist(T1-25, T3-25)",
    },
    {
        "name": "MTG 2.3",
        "source": (T2, T4),
        "shift_c": 100,
        "follow_up": ([x + 100 for x in T2], [y + 100 for y in T4]),
        "relation_str": "dist(T2, T4) == dist(T2+100, T4+100)",
    },
    {
        "name": "MTG 2.4",
        "source": (T3, T5),
        "shift_c": 3.5,
        "follow_up": ([x + 3.5 for x in T3], [y + 3.5 for y in T5]),
        "relation_str": "dist(T3, T5) == dist(T3+3.5, T5+3.5)",
    },
    {
        "name": "MTG 2.5",
        "source": (T4, T5),
        "shift_c": -50,
        "follow_up": ([x - 50 for x in T4], [y - 50 for y in T5]),
        "relation_str": "dist(T4, T5) == dist(T4-50, T5-50)",
    },
]


def evaluate_mr2_group(func, mtg):
    """
    Executes a single MTG for MR2 on the given function.
    Returns:
        (out_source, out_followup, is_killed, relation_eval_str)
    """
    pA, pB = mtg["source"]
    pA_f, pB_f = mtg["follow_up"]

    try:
        out_src = func(list(pA), list(pB))
        out_fol = func(list(pA_f), list(pB_f))
        satisfied = math.isclose(out_src, out_fol, rel_tol=1e-7, abs_tol=1e-7)
        op = "==" if satisfied else "=/="
        eval_str = f"{out_src:.1f} {op} {out_fol:.1f}"
        is_killed = not satisfied
        return out_src, out_fol, is_killed, eval_str
    except Exception as e:
        return "ERR", "ERR", True, "ERR =/= ERR"
