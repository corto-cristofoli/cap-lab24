# Generated from ITE.g4 by ANTLR 4.13.2
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
        4,1,5,28,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,2,1,2,1,2,0,
        0,3,0,2,4,0,0,27,0,6,1,0,0,0,2,15,1,0,0,0,4,17,1,0,0,0,6,7,3,2,1,
        0,7,8,5,0,0,1,8,1,1,0,0,0,9,16,1,0,0,0,10,11,3,4,2,0,11,12,6,1,-1,
        0,12,16,1,0,0,0,13,14,5,4,0,0,14,16,6,1,-1,0,15,9,1,0,0,0,15,10,
        1,0,0,0,15,13,1,0,0,0,16,3,1,0,0,0,17,18,5,1,0,0,18,19,5,4,0,0,19,
        20,5,2,0,0,20,23,3,2,1,0,21,22,5,3,0,0,22,24,3,2,1,0,23,21,1,0,0,
        0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,6,2,-1,0,26,5,1,0,0,0,2,15,23
    ]

class ITEParser ( Parser ):

    grammarFileName = "ITE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_ifStmt = 2

    ruleNames =  [ "prog", "stmt", "ifStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.st0 = None # StmtContext

        def EOF(self):
            return self.getToken(ITEParser.EOF, 0)

        def stmt(self):
            return self.getTypedRuleContext(ITEParser.StmtContext,0)


        def getRuleIndex(self):
            return ITEParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ITEParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            localctx.st0 = self.stmt()
            self.state = 7
            self.match(ITEParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.id0 = None # Token

        def ifStmt(self):
            return self.getTypedRuleContext(ITEParser.IfStmtContext,0)


        def ID(self):
            return self.getToken(ITEParser.ID, 0)

        def getRuleIndex(self):
            return ITEParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ITEParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 3]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.ifStmt()

                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                localctx.id0 = self.match(ITEParser.ID)
                print((None if localctx.id0 is None else localctx.id0.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.id0 = None # Token
            self.thenstmt = None # StmtContext
            self.elsestmt = None # StmtContext

        def ID(self):
            return self.getToken(ITEParser.ID, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ITEParser.StmtContext)
            else:
                return self.getTypedRuleContext(ITEParser.StmtContext,i)


        def getRuleIndex(self):
            return ITEParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = ITEParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(ITEParser.T__0)
            self.state = 18
            localctx.id0 = self.match(ITEParser.ID)
            self.state = 19
            self.match(ITEParser.T__1)
            self.state = 20
            localctx.thenstmt = self.stmt()
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 21
                self.match(ITEParser.T__2)
                self.state = 22
                localctx.elsestmt = self.stmt()


            print((None if localctx.id0 is None else localctx.id0.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





