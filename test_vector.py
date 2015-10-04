from vector import vec
from random import shuffle

def test_creation_empty():
    v = vec()
    assert len(v) == 0
    w = vec([])
    assert len(w) == 0


def test_creation_non_empty():
    v = vec([1, 2, 3])
    assert len(v) == 3


def test_cons():
    # Like list.append, except returns new vector w/ structural sharing.
    v0 = vec()
    assert len(v0) == 0
    v1 = v0.cons(1)
    assert len(v0) == 0
    assert len(v1) == 1
    assert v1[0] == 1


def test_cons_128():
    N = 128
    v = vec()
    for i in range(N):
        v = v.cons(i)
    assert len(v) == N
    for i in range(N):
        assert v[i] == i

def test_cons_1048576():
    N = 1048576
    v = vec()
    for i in xrange(N):
        v = v.cons(i)
    assert len(v) == N
    for i in xrange(N):
        assert v[i] == i


def test_indexing_pos():
    v = vec([1, 2, 3])
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    

def test_assoc():
    a = vec(range(31))
    b = a.assoc(0, 10)
    assert a[0] == 0
    assert b[0] == 10
    assert a[1] == b[1]
    assert a[2] == b[2]
    c = b.assoc(1, 5)
    assert c[1] == 5

"""

def test_big_vector():
    # TODO: test a vector that pushes the limits of len(), etc.
    # See if we can get it to break when using a list over the maxint size.
    pass


def test_indexing_neg():
    v = vec([1, 2, 3])
    assert v[-3] == 1
    assert v[-2] == 2
    assert v[-1] == 3


def test_equality_with_list_and_tuple():
    l = range(10, 20)
    t = tuple(l)
    v = vec(l)
    assert l == v
    assert t == v




def test_pop():
    # TODO XXX: "pop" in clojure returns a new vec with the last element
    # removed.  Consider renaming to not collide with Python's list.pop.
    v0 = vec([1, 2])
    v1 = v0.pop()
    assert v0 == [1, 2]
    assert v1 == [1]
    v2 = v1.pop()
    assert v2 == []
    v3 = v2.pop()
    assert v3 == v2 == []


def test_replace():
    # TODO XXX: think about this one...
    pass


def test_hash():
    v0 = vec()
    assert isinstance(hash(v0), int)
    v1 = vec()
    assert hash(v0) == hash(v1)
    vals = range(10)
    shuffle(vals)
    v0 = vec(vals)
    v1 = vec(vals)
    assert hash(v0) == hash(v1)


def test_iteration():
    l = [10, 11, 12]
    vv = vec(l)
    nl = []
    for v in vv:
        nl.append(v)
    assert vv == nl == l


def test_slice():
    vv = vec([1, 2, 3, 4])

    s0 = vv[:]
    assert s0 == vec
    
    s1 = vv[2:]
    assert s1 == [3, 4]

    s2 = vv[::2]
    assert s2 == [1, 3]

    s3 = vv[1::2]
    assert s3 == [2, 4]

   # TODO: test negative indices...


def test_coercion_to_list_tuple():
    vv = vec(range(10))
    ll = list(vv)
    assert isinstance(ll, list)
    assert ll == range(10)
    tt = tuple(vec)
    assert isinstance(tt, tuple)
    assert tt == tuple(range(10))

def test_reduction():
    assert reduce(lambda seq, val: seq.conj(val+1),
                  range(10), 0) == range(1, 11)
"""