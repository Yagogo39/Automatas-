from .MiniLangParser import MiniLangParser
from .MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}
        self.output = ""

    # Asignación
    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    # Print
    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        value = self.visit(ctx.expr())
        self.output += str(value) + "\n"
        return value

    # Expresiones aritméticas
    def visitExpr(self, ctx: MiniLangParser.ExprContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise Exception(f"Variable '{var_name}' no definida.")
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

    # Condición
    def visitCondition(self, ctx: MiniLangParser.ConditionContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.compOp().getText()
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        else:
            raise Exception(f"Operador desconocido: {op}")

    # If statement
    def visitIfStatement(self, ctx: MiniLangParser.IfStatementContext):
        if self.visit(ctx.condition()):
            for stmt in ctx.block().statement():
                self.visit(stmt)
