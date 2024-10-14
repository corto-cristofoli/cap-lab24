# MiniC interpreter and typer
LAB3, MIF08 / CAP / CS444 2022-23


# Authors

Corto Cristofoli

# Contents

The `TP03/MiniCInterpretVisitor.py` is the parser for evaluating the code. `TP03/MiniCTypingVisitor.py` is
parsing the type and all the errors.

# Howto

`make test-interpret TEST_FILES='TP03/tests/provided/examples/test_print_int.c'` for a single run

`make test` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make test TEST_FILES='TP03/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

# Test design 

The tests are separated between good and bad tests. I haven't the time to do a lot, so they only cover 47% of
the code.

# Design choices

I haven't done the for loop (not the time).

# Known bugs

I didn't see any bugs.
