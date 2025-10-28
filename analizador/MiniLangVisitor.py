# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#statement.
    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assign.
    def visitAssign(self, ctx:MiniLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#print.
    def visitPrint(self, ctx:MiniLangParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ifStatement.
    def visitIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#condition.
    def visitCondition(self, ctx:MiniLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expr.
    def visitExpr(self, ctx:MiniLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#compOp.
    def visitCompOp(self, ctx:MiniLangParser.CompOpContext):
        return self.visitChildren(ctx)



del MiniLangParser