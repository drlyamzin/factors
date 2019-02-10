Factor operations
===

This package implements a Factor() class and operations associated with it. 

Use case examples

Create an instance of Factor(), with variable names:

factor = Factor()

Create an instance of Factor without variable names, add variable names in a separate step:

factor = Factor()
factor.set_factor_names()

Add cardinalities of variables:

factor.set_cardinalities()

Once cardinalities are set, the assignments of the factor are calculated automatically.

Set factor values:

factor.set_values()