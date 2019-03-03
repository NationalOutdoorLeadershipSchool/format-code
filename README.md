# format-code
Pre-commit formatting hooks for NOLS code.


## Installation

- Install pre-commit:

```bash
pip install pre-commit
```

- Create or copy a **.pre-commit-config.yaml** file to the root project directory. It might very well be in your repo already. Look at **example_pre-commit-config.yaml** for the general case.


- Install the existing config (or the one you just created):

```bash
pre-commit install
```

That's it! You have now installed pre-commit hooks into your project.

## Usage

The [pre-commit documentation](https://pre-commit.com/) is a good place to start.

Pre-commit generally just works in the background when you commit or push changes to git.

You can run it manually on staged files:

```bash
pre-commit run 
```

or all files:

```bash
pre-commit run --all-files 
```

## Gotchas

**TL;DR:** Pre-commit can refuse your commits a lot. Always stage before committing, pay attention to what it is telling you. When in doubt, stage and commit again.

At first pre-commit will take some getting used to and you'll probably become more aware of the git commit flow than you used to be. First thing to know is that **PRE-COMMIT IS A VALIDATOR: if any of the hooks modify even one file it fails validation and will abort the commit**, even if all the hooks function properly.

This might require you to adjust your approach depending on your environment. Many IDEs hide the git staging (git add) step and automatically stage all files before running git commit. Bear in mind that pre-commit by default only works on staged file changes.

If pre-commit modifies a file it will abort the commit with the modifications to that file (by definition) unstaged. Now you have three versions of the file: the original, the changes you made, and the changes a hook or hooks made on top of that. With the right tools it does allow you to compare what you submitted (staged) with what came back (unstaged) to decide how to proceed.

Generally you can commit right after getting aborted and any 'just formatting' changes should commit fine. Or you can choose to apply the formatting before committing: six of one...
