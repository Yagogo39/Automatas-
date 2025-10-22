from django.shortcuts import render
from antlr4 import InputStream, CommonTokenStream
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .MiniLangVisitor import MiniLangVisitor

# Visitor para evaluar MiniLang
class MiniLangEvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}
        self.output = ""

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        value = self.visit(ctx.expr())
        self.output += str(value) + "\n"
        return value

    def visitExpr(self, ctx: MiniLangParser.ExprContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise Exception(f"Variable '{var_name}' is not defined.")
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expr(0))
            else:
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
                op = ctx.op.text
                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    return left // right
        return 0

# Vista principal: GET muestra el formulario, POST ejecuta el código
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

            # Suponiendo que tu regla raíz se llama 'program'
            tree = parser.program()

            # Evaluar con el visitor
            visitor = MiniLangEvalVisitor()
            visitor.visit(tree)
            output = visitor.output
        except Exception as e:
            output = f"Error: {e}"

    return render(request, "analizador/index.html", {"output": output, "code": code})
