#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = '^ab?'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^a[\w]{2}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = 'sofia.mp[3, 4]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '\w{0,2}ver\w{1,2}'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'^(a|b){3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^(\w\w){3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = 'Aaa a{3} a{3}|a{3} Aaa a{3}|a{3} a{3} Aaa'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'a[^1]*$'
