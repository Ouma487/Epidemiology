from initialisation import *
def test_initialisation():
    u = initialisation(50, 100)
    n = 0
    for x in range(50):
        for y in range(50):
            if u[x][y] == 1:
                n+=1
    assert n == 100           