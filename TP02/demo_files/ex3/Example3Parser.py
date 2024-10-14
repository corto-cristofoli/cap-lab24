# Generated from Example3.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,27,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,0,
        1,2,2,0,2,0,0,27,0,4,1,0,0,0,2,14,1,0,0,0,4,5,3,2,1,0,5,6,5,1,0,
        0,6,7,5,0,0,1,7,8,6,0,-1,0,8,1,1,0,0,0,9,15,6,1,-1,0,10,11,5,4,0,
        0,11,15,6,1,-1,0,12,13,5,3,0,0,13,15,6,1,-1,0,14,9,1,0,0,0,14,10,
        1,0,0,0,14,12,1,0,0,0,15,23,1,0,0,0,16,17,10,3,0,0,17,18,5,2,0,0,
        18,19,3,2,1,4,19,20,6,1,-1,0,20,22,1,0,0,0,21,16,1,0,0,0,22,25,1,
        0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,3,1,0,0,0,25,23,1,0,0,0,2,14,
        23
    ]

class Example3Parser ( Parser ):

    grammarFileName = "Example3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "OP", "INT", "ID", "WS" ]

    RULE_full_expr = 0
    RULE_expr = 1

    ruleNames =  [ "full_expr", "expr" ]

    EOF = Token.EOF
    T__0=1
    OP=2
    INT=3
    ID=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Full_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e0 = None # ExprContext

        def EOF(self):
            return self.getToken(Example3Parser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(Example3Parser.ExprContext,0)


        def getRuleIndex(self):
            return Example3Parser.RULE_full_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_expr" ):
                listener.enterFull_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_expr" ):
                listener.exitFull_expr(self)




    def full_expr(self):

        localctx = Example3Parser.Full_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_full_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            localctx.e0 = self.expr(0)
            self.state = 5
            self.match(Example3Parser.T__0)
            self.state = 6
            self.match(Example3Parser.EOF)
            print((None if localctx.e0 is None else self._input.getText(localctx.e0.start,localctx.e0.stop)) + " has " + str(localctx.e0.count) + " operators!")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None
            self.e0 = None # ExprContext
            self.e1 = None # ExprContext

        def ID(self):
            return self.getToken(Example3Parser.ID, 0)

        def INT(self):
            return self.getToken(Example3Parser.INT, 0)

        def OP(self):
            return self.getToken(Example3Parser.OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Example3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Example3Parser.ExprContext,i)


        def getRuleIndex(self):
            return Example3Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Example3Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 10
                self.match(Example3Parser.ID)
                localctx.count = 0
                pass

            elif la_ == 3:
                self.state = 12
                self.match(Example3Parser.INT)
                localctx.count = 0
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Example3Parser.ExprContext(self, _parentctx, _parentState)
                    localctx.e0 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 16
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 17
                    self.match(Example3Parser.OP)
                    self.state = 18
                    localctx.e1 = self.expr(4)
                    localctx.count = localctx.e0.count + localctx.e1.count + 1 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




