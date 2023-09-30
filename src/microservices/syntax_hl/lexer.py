from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

def highlighting(text: str) -> list:
    lexer = lex(text, PythonLexer())
    highlights = []

    current_position = 0

    for token_type, token_text in lexer:
        category = None

        if token_type in Token.Keyword:
            category = "Keyword"
        elif token_type in Token.String:
            category = "String"
        elif token_type in Token.Name:
            category = "Name"
        elif token_type in Token.Operator:
            category = "Operator"
        elif token_type in Token.Comment:
            category = "Comment"
        elif token_type in Token.Literal:
            category = "Literal"
        elif token_type in Token.Punctuation:
            category = "Punctuation"
        elif token_type in Token.Number:
            category = "Number"
        elif token_type in Token.Whitespace:
            category = "Whitespace"
        
        if category:
            start_position = current_position
            end_position = current_position + len(token_text)
            highlights.append([category, start_position, end_position])
            current_position = end_position
            print(highlights)

    return highlights


"""
"category": category,
"text": token_text,
"start": start_position,
"end": end_position
"""