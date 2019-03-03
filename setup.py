#!/usr/bin/env python


from setuptools import setup


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lines = (line.strip() for line in open(filename))
    return [
        line.split("#")[0].strip()
        for line in lines
        # skip comment lines and pip directives
        if line and not line.startswith("#") and not line.startswith("-")
    ]


reqs = parse_requirements("requirements/base.txt")

setup(
    name="format-nols-code",
    description="Pre-commit formatting hooks for NOLS code.",
    long_description=open("README.md").read(),
    version="0.0.0",  # dummy version (version is really github tag)
    author="NOLS devs",
    author_email="developer@nols.edu",
    url="https://github.com/NationalOutdoorLeadershipSchool/format-code",
    scripts=["format_python_code"],
    install_requires=reqs,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
