from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor

class MiniLangEvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}
        self.output = ""  # donde se guarda la salida

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        value = self.visit(ctx.expr())
        self.output += str(value) + "\n"  # acumulamos la salida
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
        elif ctx.getChildCount() == 3:  # expr op expr o (expr)
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
                    return left // right  # división entera
        return 0
