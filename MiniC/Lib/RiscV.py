"""
MIF08, CAP, CodeGeneration, RiscV API
Functions to define instructions.
"""

from Lib.Errors import MiniCInternalError
from Lib.Operands import (Condition, Immediate, Operand, Function)
from Lib.Statement import (Instru3A, AbsoluteJump, ConditionalJump, Label)


def call(function: Function) -> Instru3A:
    """Function call."""
    return Instru3A('call', function)


def jump(label: Label) -> AbsoluteJump:
    """Unconditional jump to label."""
    return AbsoluteJump(label)


def conditional_jump(label: Label, op1: Operand, cond: Condition, op2: Operand):
    """Add a conditional jump to the code.
    This is a wrapper around bge, bgt, beq, ... c is a Condition, like
    Condition('bgt'), Condition(MiniCParser.EQ), ...
    """
    return ConditionalJump(cond=cond, op1=op1, op2=op2, label=label)


def add(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    if isinstance(sr2orimm7, Immediate):
        return Instru3A("addi", dr, sr1, sr2orimm7)
    else:
        return Instru3A("add", dr, sr1, sr2orimm7)


def mul(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    if isinstance(sr2orimm7, Immediate):
        raise MiniCInternalError("Cant multiply by an immediate")
    else:
        return Instru3A("mul", dr, sr1, sr2orimm7)


def div(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    if isinstance(sr2orimm7, Immediate):
        raise MiniCInternalError("Cant divide by an immediate")
    else:
        return Instru3A("div", dr, sr1, sr2orimm7)


def rem(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    if isinstance(sr2orimm7, Immediate):
        raise MiniCInternalError("Cant divide by an immediate")
    return Instru3A("rem", dr, sr1, sr2orimm7)


def sub(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    if isinstance(sr2orimm7, Immediate):
        raise MiniCInternalError("Cant substract by an immediate")
    return Instru3A("sub", dr, sr1, sr2orimm7)


def land(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    """And instruction (cannot be called `and` due to Python and)."""
    return Instru3A("and", dr, sr1, sr2orimm7)


def lor(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:
    """Or instruction (cannot be called `or` due to Python or)."""
    return Instru3A("or", dr, sr1, sr2orimm7)


def xor(dr: Operand, sr1: Operand, sr2orimm7: Operand) -> Instru3A:  # pragma: no cover
    if isinstance(sr2orimm7, Immediate):
        return Instru3A("xori", dr, sr1, sr2orimm7)
    else:
        return Instru3A("xor", dr, sr1, sr2orimm7)


# add by myself #################################################
def slt(dr: Operand, sr1: Operand, sr2: Operand) -> Instru3A:
    return Instru3A("slt", dr, sr1, sr2)
#################################################################


def li(dr: Operand, imm7: Immediate) -> Instru3A:
    return Instru3A("li", dr, imm7)


def mv(dr: Operand, sr: Operand) -> Instru3A:
    return Instru3A("mv", dr, sr)


def ld(dr: Operand, mem: Operand) -> Instru3A:
    return Instru3A("ld", dr, mem)


def sd(sr: Operand, mem: Operand) -> Instru3A:
    return Instru3A("sd", sr, mem)
