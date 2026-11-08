"""
=============================================================================
METAMORPHIC TESTING & MUTATION TESTING EXECUTION SUITE
Main Runner: test.py
Integrates:
  - mr1.py (Metamorphic Relation 1: Symmetry)
  - mr2.py (Metamorphic Relation 2: Shift Invariance)
Measures Computed: ONLY E-measure and P-measure
=============================================================================
"""

import csv
import importlib.util
import math
import os
import sys

# Ensure current directory is on Python path so we can import mr1 and mr2
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
if TEST_DIR not in sys.path:
    sys.path.insert(0, TEST_DIR)

import mr1
import mr2

BASE_DIR = os.path.dirname(TEST_DIR)
SUT_PATH = os.path.join(BASE_DIR, "SUT", "manhattan_distance.py")
MUTANTS_DIR = os.path.join(BASE_DIR, "MUTANTS")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def load_module(file_path: str, module_name: str):
    """Dynamically load a python file as a module."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def eval_func_pair(func, pA, pB):
    """Execute function and return numeric result or 'ERR'."""
    try:
        return func(list(pA), list(pB))
    except Exception:
        return "ERR"


def format_rel(out_src, out_fol):
    """Format comparison as '31.0 == 31.0' or '31.0 =/= -31.0' or 'ERR =/= ERR'."""
    if isinstance(out_src, str) or isinstance(out_fol, str):
        return "ERR =/= ERR", True
    satisfied = math.isclose(out_src, out_fol, rel_tol=1e-7, abs_tol=1e-7)
    op = "==" if satisfied else "=/="
    killed = not satisfied

    def fmt(x):
        if x == int(x):
            return str(int(x))
        return f"{x:.1f}"

    return f"{fmt(out_src)} {op} {fmt(out_fol)}", killed


def run_lecture_slide_table():
    """
    Executes and formats results according to the exact slide table format:
    [Group | Source (ts) | Follow-up (tf) | SUT Output | M1  M2 ... M30]
    """
    sut_mod = load_module(SUT_PATH, "sut")
    sut_func = sut_mod.manhattan_distance

    # Load all 30 mutants
    mutant_funcs = {}
    for i in range(1, 31):
        m_file = os.path.join(MUTANTS_DIR, f"mutant{i}.py")
        mod = load_module(m_file, f"mutant{i}")
        mutant_funcs[i] = mod.manhattan_distance

    for mr_num, mr_title, mtgs, eval_func in [
        (1, "MR1: Symmetry (Commutativity) — dist(A, B) == dist(B, A)", mr1.MR1_MTGS, mr1.evaluate_mr1_group),
        (2, "MR2: Shift Invariance — dist(A, B) == dist(A+c, B+c)", mr2.MR2_MTGS, mr2.evaluate_mr2_group),
    ]:
        print("\n" + "=" * 140)
        print(f"METAMORPHIC RELATION {mr_num} EXECUTION TABLE (SUT & MUTANTS)")
        print(f"{mr_title}")
        print("=" * 140)

        # Header
        header = f"{'Group':<9} | {'Source (ts)':<24} | {'Follow-up (tf)':<24} | {'SUT Output':<15} | " + " ".join([f"M{i:<2}" for i in range(1, 31)])
        print(header)
        print("-" * len(header))

        for mtg in mtgs:
            # SUT evaluation
            _, _, sut_killed, sut_eval = eval_func(sut_func, mtg)
            src_str = str(mtg['source'][0])
            fol_str = str(mtg['follow_up'][0])

            # Evaluate each mutant
            m_cells = []
            for i in range(1, 31):
                _, _, m_killed, m_eval = eval_func(mutant_funcs[i], mtg)
                # Display 'X' if killed (=/=), '.' if survived (==)
                cell = "X" if m_killed else "."
                m_cells.append(f"{cell:<3}")

            row = f"{mtg['name']:<9} | {src_str:<24} | {fol_str:<24} | {sut_eval:<15} | " + " ".join(m_cells)
            print(row)

    print("\n[Legend: 'X' = Mutant KILLED (violates MR =/=), '.' = Mutant SURVIVED (satisfies MR ==)]")


def write_detailed_csvs():
    """Write complete source/follow-up comparisons for all mutants to Excel-friendly CSVs."""
    sut_mod = load_module(SUT_PATH, "sut")
    sut_func = sut_mod.manhattan_distance

    mutant_funcs = {}
    for i in range(1, 31):
        m_file = os.path.join(MUTANTS_DIR, f"mutant{i}.py")
        mod = load_module(m_file, f"mutant{i}")
        mutant_funcs[i] = mod.manhattan_distance

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    test_suites = [
        ("mr1", "MR1: Symmetry", mr1.MR1_MTGS),
        ("mr2", "MR2: Shift Invariance", mr2.MR2_MTGS),
    ]
    headers = [
        "MTG", "Metamorphic Relation", "Source Point A", "Source Point B",
        "Follow-up Point A", "Follow-up Point B", "Shift c",
        "SUT Comparison",
    ] + [f"M{i} Comparison" for i in range(1, 31)]

    for relation_id, relation_name, mtgs in test_suites:
        output_path = os.path.join(OUTPUT_DIR, f"{relation_id}_results.csv")
        with open(output_path, "w", newline="", encoding="utf-8-sig") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            for mtg in mtgs:
                pA, pB = mtg["source"]
                pA_f, pB_f = mtg["follow_up"]
                sut_source = eval_func_pair(sut_func, pA, pB)
                sut_followup = eval_func_pair(sut_func, pA_f, pB_f)
                sut_comparison, _ = format_rel(sut_source, sut_followup)
                row = [
                    mtg["name"], relation_name, list(pA), list(pB),
                    list(pA_f), list(pB_f), mtg.get("shift_c", ""),
                    sut_comparison,
                ]
                for mutant_id in range(1, 31):
                    mutant_func = mutant_funcs[mutant_id]
                    source_output = eval_func_pair(mutant_func, pA, pB)
                    followup_output = eval_func_pair(mutant_func, pA_f, pB_f)
                    comparison, _ = format_rel(source_output, followup_output)
                    row.append(comparison)
                writer.writerow(row)
        print(f"Detailed {relation_id.upper()} results: {output_path}")


def run_full_evaluation():
    """Computes ONLY E-measure and P-measure across MR1, MR2, and combined."""
    sut_mod = load_module(SUT_PATH, "sut")
    sut_func = sut_mod.manhattan_distance

    mutant_funcs = {}
    for i in range(1, 31):
        m_file = os.path.join(MUTANTS_DIR, f"mutant{i}.py")
        mod = load_module(m_file, f"mutant{i}")
        mutant_funcs[i] = mod.manhattan_distance

    total_mutants = 30
    mr1_kills = {mtg["name"]: [] for mtg in mr1.MR1_MTGS}
    mr2_kills = {mtg["name"]: [] for mtg in mr2.MR2_MTGS}

    mr1_killed_set = set()
    mr2_killed_set = set()

    for i in range(1, total_mutants + 1):
        m_func = mutant_funcs[i]

        # MR1
        for mtg in mr1.MR1_MTGS:
            _, _, killed, _ = mr1.evaluate_mr1_group(m_func, mtg)
            if killed:
                mr1_kills[mtg["name"]].append(i)
                mr1_killed_set.add(i)

        # MR2
        for mtg in mr2.MR2_MTGS:
            _, _, killed, _ = mr2.evaluate_mr2_group(m_func, mtg)
            if killed:
                mr2_kills[mtg["name"]].append(i)
                mr2_killed_set.add(i)

    overall_killed_set = mr1_killed_set | mr2_killed_set

    # E-MEASURE (Effectiveness)
    e_mr1 = len(mr1_killed_set) / total_mutants
    e_mr2 = len(mr2_killed_set) / total_mutants
    e_overall = len(overall_killed_set) / total_mutants

    # P-MEASURE (Probability)
    p_rate_mr1 = sum(1 for kills in mr1_kills.values() if kills) / len(mr1.MR1_MTGS)
    p_rate_mr2 = sum(1 for kills in mr2_kills.values() if kills) / len(mr2.MR2_MTGS)
    p_avg_mr1 = sum(len(kills) for kills in mr1_kills.values()) / (len(mr1.MR1_MTGS) * total_mutants)
    p_avg_mr2 = sum(len(kills) for kills in mr2_kills.values()) / (len(mr2.MR2_MTGS) * total_mutants)

    print("\n" + "=" * 80)
    print("FINAL EVALUATION METRICS (ONLY E-MEASURE & P-MEASURE)")
    print("=" * 80)
    print(f"Total Non-Equivalent Mutants: {total_mutants}")
    print("\n1. E-MEASURE (Effectiveness = Mutants Killed / Total Mutants):")
    print(f"   * E(MR1 - Symmetry):          {len(mr1_killed_set)}/{total_mutants} = {e_mr1:.4f} ({e_mr1*100:.2f}%)")
    print(f"   * E(MR2 - Shift Invariance):  {len(mr2_killed_set)}/{total_mutants} = {e_mr2:.4f} ({e_mr2*100:.2f}%)")
    print(f"   * Combined E-measure:         {len(overall_killed_set)}/{total_mutants} = {e_overall:.4f} ({e_overall*100:.2f}%)")

    print("\n2. P-MEASURE (Probability):")
    print(f"   * P_rate(MR1 - MTGs with >=1 kill): 5/5 = {p_rate_mr1:.4f} ({p_rate_mr1*100:.2f}%)")
    print(f"   * P_rate(MR2 - MTGs with >=1 kill): 5/5 = {p_rate_mr2:.4f} ({p_rate_mr2*100:.2f}%)")
    print(f"   * P_avg(MR1 - Mean detection prob): {p_avg_mr1:.4f} ({p_avg_mr1*100:.2f}%)")
    print(f"   * P_avg(MR2 - Mean detection prob): {p_avg_mr2:.4f} ({p_avg_mr2*100:.2f}%)")
    print("=" * 80)


if __name__ == "__main__":
    run_lecture_slide_table()
    write_detailed_csvs()
    run_full_evaluation()
