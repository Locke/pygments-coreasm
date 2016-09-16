# -*- coding: utf-8 -*-
"""
    pygments.lexers.coreasm
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for CoreASM.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import *

__all__ = ['CoreASMLexer']


class CoreASMLexer(RegexLexer):
    """
    For CoreASM source code.
    """

    name = 'CoreASM'
    aliases = ['coreasm', 'casm']
    filenames = ['*.coreasm', '*.casm']
    mimetypes = []

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
        ],
        'string': [
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ],
        'root': [
            include('commentsandwhitespace'),
            (r'->', Punctuation),
            (r'([-<>+*/]|=|!=|<=|>=)', Operator),
            (r'(not|or|and)', Operator.Word),
            (r'[{(\[:;,]', Punctuation),
            (r'[})\].]', Punctuation),
            (r'(for|in|while|do|return|switch|case|if|then|else)\b', Keyword),
            (r'(include)(\s+)', bygroups(Keyword, Text), 'string'),
            (r'(CoreASM|use)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name.Namespace)),
            (r'(init)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name.Function)),
            (r'(option)(\s+)([\w.]+)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name, Text, Name)),
            (r'(let|universe)\b', Keyword.Declaration),
            (r'(function|derived|rule)(\s+)(\w+)', bygroups(Keyword.Declaration, Text, Name.Function)),
            #(r'(boolean|number)\b', Keyword.Reserved),
            (r'(true|false|undef)\b', Keyword.Constant),
            (r'(STRING|NUMBER|MAP|SET|RULE)\b', Name.Builtin),
            (r'[0-9][0-9]*\.[0-9]', Number.Float),
            (r'[0-9]+', Number.Integer),
            include('string'),
        ]
    }

def main():
    from pygments import highlight
    from pygments.formatters import TerminalFormatter, HtmlFormatter

    code = """
CoreASM MyFoo

use Options
use Time

option DebugInfo.activeChannels ALL

include "bar.coreasm"

init Foo

function sBPMFunction : NUMBER * STRING -> RULE

rule Foo(x) = {
  while (i < 5 + (2*3/4)) do {
    if (x = true and y != undef) then {
      //not good
      /*
      at least not undef
      */
      Crash()
    }
    else { print "asdf!" }
  }
  
  let x = foo(y) in {
    print "x = " + x
  }
}
"""

    print highlight(code, CoreASMLexer(), TerminalFormatter())
    #print highlight(code, CoreASMLexer(), HtmlFormatter())

if __name__ == "__main__":
    main()
