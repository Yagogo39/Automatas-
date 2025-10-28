from django.shortcuts import render
from antlr4 import InputStream, CommonTokenStream
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .EvalVisitor import EvalVisitor  # <- aquí

def analizar(request):
    output = ""
    code = ""
    if request.method == "POST":
        code = request.POST.get("codigo", "")
        try:
            input_stream = InputStream(code)
            lexer = MiniLangLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = MiniLangParser(tokens)

            tree = parser.program()
            visitor = EvalVisitor()  # <- y aquí
            visitor.visit(tree)
            output = visitor.output
        except Exception as e:
            output = f"Error: {e}"

    return render(request, "analizador/index.html", {"output": output, "code": code})
