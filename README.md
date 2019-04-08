# format-code

Pre-commit formatting hooks for NOLS code, including a NOLS-specific Python hook.

This repository contains two important items: a NOLS-specific Python formatting package and a sample
pre-commit configuration file.

The `format_python_code.py` wraps black, isort, and docformatter in such a way that they work as an
atomic unit. Without this wrapping, black and isort can interact in frustrating ways when used with
pre-commit.

The sample pre-commit file contains default settings for prettier, which formats a variety of
formats (mostly HTML, CSS, JavaScript, and Markdown in our situation).

# Typical usage

Many (soon to be most) NOLS repositories come pre-configured with `pre-commit`. In those instances
you will simply need to do the following.

```bash
git clone some-repo
pip install -r some-requirements.txt
pre-commit install
```

### Reformat as you go

You will almost assuredly want to configure your editor to re-format the current file with the same
rules that our pre-commit hooks are using. See the section below titled
[Configuring your editor](https://github.com/NationalOutdoorLeadershipSchool/format-code#configuring-your-editor).

Remember, the automated builds will fail code that does not adhere to our standard, so you'll always
want to install the pre-commit hooks!

## Configuring a project with pre-commit

If you're starting a new repository, you will want to configure it with our pre-commit hooks.

- After creating the git repository, install pre-commit:

```bash
pip install pre-commit
```

- Better yet, include it in a requirements file:

```bash
pip freeze > requirements.txt
```

- Create or copy a **.pre-commit-config.yaml** file to the root project directory. Look at
  **example_pre-commit-config.yaml** for the general case.

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

**TL;DR:** Pre-commit can refuse your commits a lot. Always stage before committing, pay attention
to what it is telling you. When in doubt, stage and commit again. Life is MUCH easier if you format
as you go.

At first pre-commit will take some getting used to and you'll probably become more aware of the git
commit flow than you used to be. First thing to know is that **PRE-COMMIT IS A VALIDATOR: if any of
the hooks modify even one file it fails validation and will abort the commit**, even if all the
hooks function properly.

This might require you to adjust your approach depending on your environment. Many IDEs hide the git
staging (git add) step and automatically stage all files before running git commit. Bear in mind
that pre-commit by default only works on staged file changes.

If pre-commit modifies a file it will abort the commit with the modifications to that file (by
definition) unstaged. Now you have three versions of the file: the original, the changes you made,
and the changes a hook or hooks made on top of that. With the right tools it does allow you to
compare what was validated (staged) with what came back (unstaged) to decide how to proceed.

Generally you can commit right after getting aborted and any 'just formatting' changes should commit
fine. Or you can choose to apply the formatting before committing: six of one...

## Configuring your editor

Given the above gotcha, your life will be much easier if you configure it to reformat code with the
same tools used by our pre-commit hooks.

The command we'll want to run would look like this on the command-line:

```bash
pre-commit run --files current-file.py
```

Every editor should allow you to execute external tools. We've included the settings for the PyCharm
**External Tools** tool available in Preferences. Assign this command an easy-to-use shortcut ...
and use it a LOT.

- **Program**:
  - `$PyInterpreterDirectory$/pre-commit`
- **Arguments**:
  - `run --files $FilePath$`
- **Working directory:**
  - `$ProjectFileDir$`

You can see how the settings above will resolve into the `pre-commit run --files current-file.py`
example. This configuration uses PyCharm's environment variables (called Macros) that help use here.
Because External Tools are an IDE-wide option, we use the `$PyInterpreterDirectory$` variable so we
can configure this once and have it work across projects. Without this macro the setting would be
this for the website project `${NOLSCODE}/venvs/website/bin/precommit`. But we don't want ALL
projects using the website pre-commit binary, hence the variable.

Similarly, PyCharm offers variable for the current file and working directory.

Most editors should have similar tools to aid configuration.
