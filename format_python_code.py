#!/usr/bin/env python3


import shlex
import subprocess
import sys


PASS = 0
FAIL = 1


def main():
    """This calls three python packages which each contribute something to overall Python
    code formatting.

    They can conflict in sometimes upredictable fashion. When they do, they each
    modify the file on every pass, resulting in valid but uncommitable changes. The
    solution is to wrap them all together into one hook so pre-commit treats them
    atomically and is unaware of any transient file modifications.
    """
    files = sys.argv[1:]  # this assumes argv is a pre-filtered list of python files

    package_settings = {
        "black": "--line-length 100",
        "docformatter": "--wrap-summaries 90 --wrap-descriptions 85 --in-place",
        "isort": (
            "--atomic --line-width 100 --combine-star --combine-as "
            "--multi-line 3 --trailing-comma --lines-after-imports 2"
        ),
    }

    return_value = PASS
    stderr = ""
    for package, string_settings in package_settings.items():
        list_settings = shlex.split(string_settings)
        result = subprocess.run([package, *list_settings, *files], capture_output=True)
        return_value |= result.returncode
        if result.returncode:
            stderr += "\n" + result.stderr.decode("utf-8")

    if return_value:
        print(stderr)

    return return_value


if __name__ == "__main__":
    sys.exit(main())
