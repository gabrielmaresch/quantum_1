from boolean_to_qc import get_fulltree, get_projectionprobs

def test_bool(x):
    # two out of three:
    # (x0 /\ x1) \/ (x0 /\ x2) \/ (x1 /\ x2)
    def f(tupel)
        return (tupel[0] and tupel[1]) or (tupel[0] and tupel[2]) or  (tupel[1] and tupel[2])
    f_tree = get_fulltree(f,3)
    


def test_one(tupel):
    return 1

def test_or(tupel):
    return (tupel[0] or tupel[1])

def test_and(tupel):
    return (tupel[0] and tupel[1])

def test_range(a,b):
    # a..start, b..end, n .. size of tupel
    
    def f(tupel):
        x = ''.join([str(digit) for digit in tupel])[::-1]
        if a <= int(x,2) and int(x,2) < b:
            return 1
        else: 
            return 0
    return f