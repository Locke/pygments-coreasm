from setuptools import setup, find_packages
 
setup (
  name='coreasmlexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  coreasmlexer = coreasmlexer.lexer:CoreASMLexer
  """,
)

