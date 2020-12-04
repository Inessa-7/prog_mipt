from task5 import get_permutations as g_p


def test_1():
    res = g_p("plan", 2)
    assert res == ["al","an","ap","la","ln","lp","na","nl","np","pa","pl","pn"]


def test_2():
    res = g_p("1nfa", 3)
    ans = ["af1", "afn", "a1f", "a1n", "anf", "an1", "fa1", "fan", "f1a", 
           "f1n", "fna", "fn1", "1af", "1af", "1an", "1fa", "1fn", "1na", 
           "1nf", "naf", "na1", "nfa", "nf1", "n1a"] 
