import re

def validate_equation(equation: str) -> bool:
  """
  validate_equation(equation: str) -> bool
  Validates an equation string.

  equation: The equation string to validate.

  Returns: True if the equation is valid, False otherwise.
  """

  equation = equation.strip().lower()
  regexp = re.compile('[a-wy-zA-WY-Z]*[!|@|#|$|%|&|~]*')
  matches = regexp.findall(equation)
  for match in matches:
    if match != '' or equation.find('xx') != -1 or len(equation) < 1:
      return False
  return True


def compile_equation(equation: str) -> str:
  """
  compile_equation(equation: str) -> str
  Compiles an equation string.
  
  equation: The equation string to compile.

  Returns: The compiled equation string.
  """

  if validate_equation(equation):
    equation = equation.strip().lower().replace(' ', '').replace('^', '**')
    multiply = re.compile('[0-9]x')
    multiplies = multiply.findall(equation)
    for mult in multiplies:
      equation = equation.replace(mult, f'{mult[0]}*x')
    return equation
  else:
    raise SyntaxError

def get_equation_result(equation: str, x: float) -> float:
  """
  get_equation_result(equation: str, x: float) -> float
  Returns the result of an equation string (float('inf') in case of Division By Zero).

  equation: The equation string to evaluate.
  x: The x value to evaluate the equation at.

  Returns: The result of the equation.
  """

  equation = compile_equation(equation)
  try:
    value = eval(equation.replace('x', f'({x})'))
  except ZeroDivisionError:
    return float('inf')
  return float(value)
