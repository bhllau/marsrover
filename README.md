# Solution to Mars Rover Problem in Python 3.7


## Summary

This repository is a solution to the Mars Rover problem (described in
[./TASK.md](TASK.md)) written in Python 3.7.


## Project structure

    .
    ├── .gitignore
    ├── .pylintrc
    ├── Dockerfile
    ├── README.md
    ├── bin
    │   ├── play
    │   ├── run_lint
    │   ├── run_tests
    │   └── run_typecheck
    ├── project
    │   ├── __init__.py
    │   ├── main.py
    │   └── tests
    │       ├── __init__.py
    │       └── main_tests.py
    └── req.txt


## Quickstart


### With Docker

1. Build docker image:

        $ docker build -t mars-rover-solution .

2. Run the image:

        $ docker run -it --rm mars-rover-solution
        >>> Linting project code...

        ------------------------------------
        Your code has been rated at 10.00/10


        >>> Running type check...
        Success: no issues found in 4 source files

        >>> Running unit tests and integration tests...
        ..............
        ----------------------------------------------------------------------
        Ran 14 tests in 0.004s

        OK
        Name                         Stmts   Miss  Cover
        ------------------------------------------------
        project/__init__.py              0      0   100%
        project/main.py                 55      2    96%
        project/tests/__init__.py        0      0   100%
        project/tests/main_test.py      53      0   100%
        ------------------------------------------------
        TOTAL                          108      2    98%

        >>> Start program in interactive mode (you can input now)...
        > 5 5
        > 1 1 N M
        < 1 2 N
        > 2 2 S MM
        < 2 0 S
        > 2 2 E LMLMM
        < 0 3 W
        (EOF)

        >>> Bye!


### Without Docker

1. Life is easier if we use same version of Python:

        $ python --version
        3.7.8


2. Install the requirements:

        $ pip install -r ./req.txt


3. The executables are provided under `./bin`:

   - To lint (for pretty and conforming codes):

        $ ./bin/run_lint
        --------------------------------------------------------------------
        Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

   - To type check (types annotations):

        $ ./bin/run_typecheck
        Success: no issues found in 4 source files

   - To run unit tests:

        $ ./bin/run_tests
        ..............
        ----------------------------------------------------------------------
        Ran 14 tests in 0.001s

        OK

   - To run the program (stdin/stdout):

        $ ./bin/play
        > 5 5
        > 1 1 N M
        < 1 2 N
        > 2 2 S MM
        < 2 0 S
        (EOF)

