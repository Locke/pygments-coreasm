# pygments-coreasm

## About

This repository contains a CoreASM lexer for pygments. It's intention is to be used with [minted](https://github.com/gpoore/minted).

## Requirements

- Python setuptools
  - on Debian: `sudo apt-get install python3-setuptools`

- pygments
  - on Debian: `sudo apt-get install python3-pygments`
  - alternative: `sudo easy_install Pygments`


## Setup

One-Shot installation via: `sudo python setup.py install` (copies the files)

Development installation via: `sudo python setup.py develop` (links to the files)


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

