"""
controller.py by Henry Phan
Functions for Financial calculator
"""

#functions
def get_answer(principle: int, period: int, duration: int, compound: int,) -> str:
    """ calculates and outputs answer """
    if period > 0:
        financial = principle * (1 + period / compound) ** (compound * duration)
    elif period < 0:
        financial = principle * (1 - period / compound) ** (compound * duration)
    results = f"You will have {financial} by the end of {duration} years."
    return results