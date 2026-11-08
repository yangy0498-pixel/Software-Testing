"""
Mutant 10: AOR_Multiply_By_Two
Operator: AOR (Arithmetic Operator Replacement)
Description: Multiplied distance by 2.0
Hypothesized Killing Metamorphic Relation: MR2
"""

def manhattan_distance(point_a: list, point_b: list) -> float:
    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")
    return float(sum(abs(a - b) for a, b in zip(point_a, point_b)) * 2.0)


def _validate_point(point: list[float]) -> None:
    if point:
        if isinstance(point, list):
            for item in point:
                if not isinstance(item, (int, float)):
                    msg = f"Expected a list of numbers as input, found {type(item).__name__}"
                    raise TypeError(msg)
        else:
            msg = f"Expected a list of numbers as input, found {type(point).__name__}"
            raise TypeError(msg)
    else:
        raise ValueError("Missing an input")
