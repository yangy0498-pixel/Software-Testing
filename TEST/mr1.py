"""
=============================================================================
METAMORPHIC RELATION 1 (MR1): SYMMETRY (COMMUTATIVITY)
File: mr1.py
Formula: manhattan_distance(A, B) == manhattan_distance(B, A)
=============================================================================
"""

import math

# Source Test Inputs (2D vectors as required)
T1 = [12, 34]
T2 = [5, 10]
T3 = [-3, 8]
T4 = [0, 0]
T5 = [100, 250]

# 5 Metamorphic Test Groups for MR1
MR1_MTGS = [
    {
        "name": "MTG 1.1",
        "source": (T1, T2),
        "follow_up": (T2, T1),
        "relation_str": "dist(T1, T2) == dist(T2, T1)",
    },
    {
        "name": "MTG 1.2",
        "source": (T1, T3),
        "follow_up": (T3, T1),
        "relation_str": "dist(T1, T3) == dist(T3, T1)",
    },
    {
        "name": "MTG 1.3",
        "source": (T2, T3),
        "follow_up": (T3, T2),
        "relation_str": "dist(T2, T3) == dist(T3, T2)",
    },
    {
        "name": "MTG 1.4",
        "source": (T1, T4),
        "follow_up": (T4, T1),
        "relation_str": "dist(T1, T4) == dist(T4, T1)",
    },
    {
        "name": "MTG 1.5",
        "source": (T3, T5),
        "follow_up": (T5, T3),
        "relation_str": "dist(T3, T5) == dist(T5, T3)",
    },
]


def evaluate_mr1_group(func, mtg):
    """
    Executes a single MTG for MR1 on the given function.
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
