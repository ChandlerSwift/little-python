from littlepython.ast import Var, Block, If, ControlBlock, Int
from tests import t


def test_ast_eq_dif_types():
    assert Int(t("1")) != Var(t("1"))


def test_ast_eq_same_type_diff_attr():
    c1 = Int(t("1"))
    c2 = Int(t("1"))
    c2.left = "bla"
    assert c1 != c2


def test_ast_eq_same_type_same_attr_diff_value():
    c1 = Int(t("1"))
    c2 = Int(t("1"))
    c1.left = "bla"
    c2.left = "bla1"
    assert c1 != c2


def test_if_eq_diff_type():
    assert If([], Block()) != Var(t("1"))


def test_control_block_eq_diff_type():
    assert ControlBlock([If([], Block())]) != Var(t("1"))
