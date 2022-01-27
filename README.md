# pygments-coreasm

## About

This repository contains a [CoreASM](https://github.com/CoreASM/coreasm.core) lexer for [Pygments](https://github.com/pygments/pygments). It's motivation is to be used with [minted](https://github.com/gpoore/minted).

## Requirements

- Python setuptools
  - on Debian: `sudo apt-get install python3-setuptools`

- pygments
  - on Debian: `sudo apt-get install python3-pygments`
  - alternative: `sudo easy_install Pygments`


## Setup

One-Shot installation via: `sudo python3 setup.py install` (copies the files).

Development installation via: `sudo python3 setup.py develop` (links to the files). Uninstall with `sudo python3 setup.py develop --uninstall`.


## Usage with minted

- install the minted package in your latex distribution
  - on Debian: `sudo apt-get install texlive-latex-extra`

Example usage:

```LaTeX
\usepackage{minted}

\newmintinline[coreinline]{coreasm}{escapeinside=||}

Hello \coreinline{undef}!
```

shell escape must be enabled (unless you use the draft mode), e.g. via `pdflatex -shell-escape`.

## Status

Developed on Debian 11 with Pygments 2.7.1 and CoreASM [v1.7.3-locke-5](https://github.com/Locke/coreasm.core/releases/tag/v1.7.3-locke-5).

Coverage of the CoreASM language might still be incomplete.

Contibutions / PRs are welcome.
