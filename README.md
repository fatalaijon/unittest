## Unit Testing Exercises

These exercises accompany the ISP unit testing presentation:
<https://cpske.github.io/ISP/testing/PythonUnitTesting.pdf>


### 1. MathTest of `sqrt` and `pow`

1. Create a class named `MathTest` in `math_test.py`.  Write these 2 test methods:
   * `test_sqrt`
      - test that square root of 25 is 5
      - test that square root of 0 is 0 (edge case)
      - test that square root of 9.0E+300 is 3.0E+150 (extreme case)
   * `test_pow`
      - write 2 tests (assertEqual) for `math.pow` (power function)

2. Run your tests on the command line.  They should all pass.

3. Commit this file to the repository.

### 2. Failing Tests

Write a test method that *fails* and a test method that *errors*.    
Both "failures" and "errors" occur regularly in unit testing.

1. Write `test_wrong_sqrt` - test for a value that is not correct, such as sqrt(100) is 20.

2. Write `test_sqrt_of_negative` - test if sqrt of a negative number returns a positive value (or returns an imaginary value).  This will cause a ValueError exception -- don't catch this exception, the purpose is to see how unittest handles it.

3. Run the tests.  The first test should "fail" and the second test should "error" (raises a ValueError).  
   - Notice how unittest displays "errors" and "failures" differently.

4. Commit your code to the repository.


### 3. Test for Exception

1. Modify `test_sqrt_of_negative` to expect a `ValueError` will be raised by math.sqrt.  Syntax for this is in the presentation (above).

2. Run the tests.  The revised test should pass (no 'error' results). The other test should still fail.

3. Commit this change to the repository.

### 4. Test with Limited Precision

The square root of 2 is approximately 1.4142135623730951.

1. Write a test that sqrt(2) is correct to **10 decimal places** using the test method:    
   `assertAlmostEqual(expected, actual, places=n)`

2. Run the tests.

3. Commit this change to the repo.

Note: another way to use assertAlmostEqual is:
```python
  assertAlmostEqual(expected, actual, delta=value)
```
This is more flexible since you can compute the delta value based on *relative error*.


### 5. Test Driven Development

In this last exercise, use *Test Driven Development* (TDD).  Write the unit tests **before** you write the code being tested.

The code under test is a function named `integrate` that does numerical integration using *Simpson's Rule* to approximate the value of integrals.

The syntax is: `integrate(fun, a, b, intervals=1)`     

where:

  `fun` is a real-valued function with a single real parameter, fun(x)    
  `a` is the left endpoint of the interval to integrate    
  `b` is the right endpoint of the interval to integrate    
  `intervals` (optional) is number of subintervals to use. 

Increasing the number of subintervals usually makes the result more accurate.

**DO NOT** write this function yet.  You must write the tests first (TDD).


**5.1** Write these test for `integrate`:

| # | Function  | What to test      |
|---|:----------|:------------------|
| 1 | constant function | integral of a constant value function is exactly correct |
| 2 | quadratic polynomial | integral of a quadratic function is correct |
| 3a | sine function      | integral of sin from 0 to pi is 2.0 with error less than 0.1 |
| 3b | sine function      | integral from 0 to pi with 20 subintervals is 2.0 with error less than 1.0e-6 |

Test Case #1 is given in the starter code.

For Test Case #2, the value computed by Simpson's rule may contain some very small round-off or precision error. A relative error of 1.0e-10 is acceptable. OK to use just one quadratic polynomial but you should test using more than one set of endpoints.

For Test Case #3 you must test that the exact and computed values are *almost* equal.

**5.2** Run the tests - they should all **fail**, of course.

**SUBMIT** Commit your code and push to Github.

**5.3** Write the code for integrate in file `integral.py`.

**5.4** Run the tests, again.  If any fail, revise your code and retest until they all pass. Also check your test code for possible errors.

**SUBMIT** Commit your code and push to Github.


### Simpson's Rule for Numerical Integration

[Simpson's Rule][Simpsons-Rule] is a formula for numerical integration that computes the exact integral value for any polynomial of degree 3 or less. For other functions it is approximate; the error is a constant times the 4th derivative of the function.  
The formula to numerically approximate the integral of f(x) from a to b is:

  h = (b - a)/2    
  integral = (f(a) + 4f(a+h) + f(b))(h/3)

To get a more accurate result, the interval [a,b] can be divided in `n` subintervals and Simpson's Rule applied to each subinterval.  The formula is:

n = number of subintervals    
h = (b - a)/(2n)   
integral = (h/3) [f(a) + 4f(a+h) + 2f(a+2h) + 4f(a+3h) + 2f(a+4h) + ... + f(b)] 


[Simpsons-Rule]: https://en.wikipedia.org/wiki/Simpson%27s_rule
