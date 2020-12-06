from task7 import get_combinations_with_r as g_c_w_r


def test_1():
    res = g_c_w_r("day", 2)
    assert res == ["aa", "ad", "ay", "dd", "dy", "yy"]


def test_2():
    res = g_c_w_r("3pla1", 3)
    assert res == ['111', '113', '11a', '11l', '11p', '133', '13a', 
                   '13l', '13p', '1aa', '1al', '1ap', '1ll', '1lp', 
                   '1pp', '333', '33a', '33l', '33p', '3aa', '3al', 
                   '3ap', '3ll', '3lp', '3pp', 'aaa', 'aal', 'aap',
                   'all', 'alp', 'app', 'lll', 'llp', 'lpp', 'ppp']
