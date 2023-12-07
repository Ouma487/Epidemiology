
import numpy as np

from chgmt_etat2 import *

def test_changement_etat2():

    a=np.array([[0,1,3,0,0],[0,0,0,1,4],[0,0,1,0,0]])#fais le test avec cet univers 
    print(chgmt_etat2(a,0.3,0.2,0.4,4,0.01,0.01,0))


print(test_changement_etat2())
