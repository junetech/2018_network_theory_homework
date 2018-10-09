# Python Code Submission Guide

Created in 9th(Tue) Oct. 2018 by JuneTech

## Procedure

1. Make an empty file with filename of `HW*_studentnumber_lastname.py`.
   For example, `HW2_20162338_Hong.py`.
1. Paste this base code into your empty file:
    ```py
    #!python3
    '''
    Code for 2018 Network Theory HW#2-2
    '''
    import networkx as nx

    def solve(filename):
        ## Your
        ## lines
        ## of code
        ## that TA will
        ## use to check correctness
        return solution

    def main():
        filename = "network_theory_hw2_graph1.csv"
        print(solve(filename))

    if __name__ == '__main__':
        main()
    ```
1. Fill in the `solve(filename)` function by yourself.
1. Submit one `HW*_studentnumber_lastname.py file`.
   In case you feel you need, submit a report in any format you like.

## Do's

- Use `filename`, an input variable for your `solve` function, when you read files. Changing filename in the `main` function will easily let you test your code with other inputs.
- Whenever you need, make user-defined function you need, **in the same file**. Note that you do not submit multiple `.py` files. Do like as follows:
    ```py
    #!python3
    '''
    Code for 2018 Network Theory HW#2-2
    '''
    import networkx as nx

    def my_read_function(filename):
        ## You do something with filename
        return G

    def my_second_function(arg1, arg2):
        ## You do something
        ## either return some value
        ## or change the value of arguments
        return arg1 * arg2

    def my_another_function(arg1, arg2):
        ## You do something
        ## either return some value
        ## or change the value of arguments
        change(arg1)

    def my_last_function(arg1, arg2):
        ## You do something
        ## either return some value
        ## or change the value of arguments
        ## or both!
        change(arg2)
        return arg1 - arg2

    def solve(filename):
        ## Your lines of code
        ## that TA will
        ## use to check correctness
        a = ##
        b = ##
        G = my_read_function(filename)
        c = my_second_function(a, b)
        my_another_function(a, c)
        solution = my_last_function(b, c)
        return solution

    def main():
        filename = "network_theory_hw2_graph1.csv"
        print(solve(filename))

    if __name__ == '__main__':
        main()
    ```

## Tips

- Python cares capital letters. A LOT.
  - `True` is a boolean, while `true` is a string.
  - `int` specifies the type of variable, while `Int` does not.
- Write comments. It helps yourself a lot. It also helps TA.
  - Writing a docstring for function is like:
    ```py
    def my_last_function(arg1, arg2):
    '''
    Returns the distance between arg1 and arg2
    '''
    ```
  - Writing in-line comments is like:
    ```py
    def solve(filename):
    a = ##
    b = ##
    ## Calculating distance between a and b
    c = my_first_function(a, b)
    ## Setting initial labels
    my_another_function(a, c)
    ## Return dictionary of labels; if negative cycle, return list
    solution = my_last_function(b, c)
    return solution
    ```
- Install `pylint`. It helps you to reduce your time by red underlines.
  Some green underline warnings may be negligible, but not always.
- You may need to run your command line prompt with administrator mode(관리자 권한), depending on how you installed your Python.
