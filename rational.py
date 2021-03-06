import math

class Q(object):
    def __init__(self, a, b=1): 
        gcd = math.gcd(a,b)
        self.a = a//gcd
        self.b = b//gcd
    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        return f'{self.a}/{self.b}'
    def add(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c, b*d)
    def sub(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c, b*d)
    def mul(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d*b*c, b*d)
    def truediv(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d/b*c, b*d)

q1 = Q(1,2)
q1.a => 1
q1.b => 2

print(q1.add(q2))
print(q1.sub(q2))
print(q1.mul(q2))
print(q1.truediv(q2))