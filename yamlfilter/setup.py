from setuptools import setup, find_packages
 
setup (
  name='servicefilter',
  packages=find_packages(),
  entry_points =
  """
  [pygments.filters]
  servicefilter = servicefilter.filter:ServiceFilter
  """,
)