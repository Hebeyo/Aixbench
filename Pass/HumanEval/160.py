def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    expression = ''
    for i in range(len(operator)):
        expression += str(operand[i])
        expression += operator[i]
    expression += str(operand[-1])
    return eval(expression)

def check(candidate):
    for item in range(31):
        assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
        assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert candidate(['//', '*'], [7, 3, 4]) == 8, 'This prints if this assert fails 1 (good for debugging!)'
        assert True, 'This prints if this assert fails 2 (also good for debugging!)'
'\nStandard answer: \n    expression = str(operand[0])\n    for oprt, oprn in zip(operator, operand[1:]):\n        expression+= oprt + str(oprn)\n    return eval(expression)\n'
check(do_algebra)