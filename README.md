# Shell Builder
## Create your custom shell in a few seconds

## Install SymbolicAI

```bash
$> pip install symbolicai
```

See more info at the original [Repository](https://github.com/ExtensityAI/symbolicai).

## Shell Builder commands

### Installation

Use the builtin `sympkg` to install the package
```bash
$> sympkg i ExtensityAI/shellbuilder
```
Create an alias for the `shellbuilder` command
```bash
$> symrun c newshell ExtensityAI/shellbuilder
```

### Usage:

Now simply call:
```bash
$> symrun newshell "<github_user>/<github_repo>" "<description_of_the_repo>"
```

Example:
```bash
$> symrun newshell "ExtensityAI/demoshell" "A demo shell style showing a lot of examples"
```
