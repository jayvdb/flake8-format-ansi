# flake8-format-ansi
ANSI error format plugin for flake8

`pep8` and `flake8` support a custom error format using `--format=..`.  This flake8 plugin allows ANSI escape codes to be used in the custom error format.
e.g.

    \e[31mERROR:\e[0m %(path)s:%(row)d:%(col)d: \e[31m%(code)s\e[0m %(text)s

This can be placed into the `[flake8]` section of the configuration file.
e.g.

    [flake8]
    format = \e[31mERROR:\e[0m %(path)s:%(row)d:%(col)d: \e[31m%(code)s\e[0m %(text)s

However note that will cause ANSI escape codes to be shown in CMD.EXE.  See https://github.com/adoxa/ansicon for a way to add ANSI support to CMD.EXE on some MS Windows version.
