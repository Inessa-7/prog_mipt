class Mother:
    pass


class Daughter(Mother):
    def __repr__(self):
        return "I am a Daughter"


m = Mother()
d = Daughter()
print(m)
print(d)
