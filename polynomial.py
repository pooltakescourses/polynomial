class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Op:
  def __repr__(self):
    raise ValueError()
  def evaluate(self, x):
    eqn = str(self).replace("X", str(x))
    print("Evaluating Polynomial:", eqn)
    return eval(eqn)

class AddOp(Op):
    def __init__(self, p1, p2, sign):
        assert sign in ["+", "-"], "AddOp only takes '+' or '-' sign"
        self.p1 = p1
        self.p2 = p2
        self._sign = sign
    
    def __repr__(self):
        return repr(self.p1) + f" {self._sign} " + repr(self.p2)


class MulOp(Op):
    def __init__(self, p1, p2, sign):
        self.p1 = p1
        self.p2 = p2
        self._sign = sign
    
    def __repr__(self):
        if isinstance(self.p1, AddOp):
            if isinstance(self.p2, AddOp):
                 return "( " + repr(self.p1) + f" ) {self._sign} ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + f" ) {self._sign} " + repr(self.p2)
        if isinstance(self.p2, AddOp):
            return repr(self.p1) + f" {self._sign} ( " + repr(self.p2) + " )"
        return repr(self.p1) + f" {self._sign} " + repr(self.p2)

class Add(AddOp):
  def __init__(self, p1, p2):
    super().__init__(p1, p2, "+")

class Sub(AddOp):
  def __init__(self, p1, p2):
    super().__init__(p1, p2, "-")

class Mul(MulOp):
  def __init__(self, p1, p2):
    super().__init__(p1, p2, "*")

class Div(MulOp):
  def __init__(self, p1, p2):
    super().__init__(p1, p2, "/")

poly = Add( Sub( Int(4), Int(3)), Add( X(), Div( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print("Answer:", poly.evaluate(2))
