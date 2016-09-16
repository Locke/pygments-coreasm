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
            (r'(->|:=|:)', Punctuation),
            (r'(memberof|implies|not|xor|or|and|div)', Operator.Word),
            (r'[{(\[,|?]', Punctuation),
            (r'[})\].]', Punctuation),
            (r'(<<|>>)', Punctuation),
            (r'([-<>+*/%]|=|!=|<=|>=)', Operator),
            (r'(end)?(seqblock|par|choose|case)\b', Keyword),
            (r'(seq|next|iterate|return|result)', Keyword),
            (r'(import|extend|do|skip|pick|forall|exists|in|is|with|holds|ifnone|if|then|else|while|step)\b', Keyword),
            (r'(add|remove|push|pop|shift (left|right)|(en|de)queue|from|(in)?to)', Keyword),
            (r'(deuginfo)', Keyword),
            (r'(suspend|resume|terminate|shutdown)', Keyword),
            (r'(include)(\s+)', bygroups(Keyword, Text), 'string'),
            (r'(CoreASM|use)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name.Namespace)),
            (r'(init)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name.Function)),
            (r'(call)(\s+)(\w+)', bygroups(Keyword, Text, Name.Function)),
            (r'(option)(\s+)([\w.]+)(\s+)(\w+)', bygroups(Keyword.Namespace, Text, Name, Text, Name)),
            (r'(@)(\w+)', bygroups(Operator, Name.Function)),
            (r'(ruleelement)(\s+)(\w+)', bygroups(Operator.Word, Text, Name.Function)),
            (r'(local|let|universe|enum)\b', Keyword.Declaration),
            (r'(function|derived|rule)(\s+)(\w+)', bygroups(Keyword.Declaration, Text, Name.Function)),
            (r'(true|false|undef|self|program)\b', Keyword.Constant),
            (r'(STRING|NUMBER|MAP|SET|RULE)\b', Name.Builtin),
            (r'(input)\b', Name.Builtin),
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
      shift right value into loc
      //not good
      /*
      at least not undef
      */
      Crash()
    }
    else { print "asdf: " + (1 + 12.37 + |{"a", {4 -> undef}}|) }
  }
}
 
derived spameggs = return fish in {
  let x = foo(y) in {
    print "x = " + x
    fish := << spam | spam in eggs with |spam| < x >>
  }
}

rule InitRule =
  par
    terminate := false
    program(self) := @MainProgram
    program(foo) := ruleelement MainProgram
  endpar

rule MainProgram =
  if not terminate then
    par
      print "This is CoreASM."
      terminate := true
    endpar
  else
    program(self) := undef
"""

    print highlight(code, CoreASMLexer(), TerminalFormatter())
    #print highlight(code, CoreASMLexer(), HtmlFormatter())

if __name__ == "__main__":
    main()
