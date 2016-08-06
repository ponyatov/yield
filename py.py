class UnifyingVariable:
    def __init__(self):
        self._isBound = False

    def unify(self, arg):
        if not self._isBound:
            self._value = arg
            self._isBound = True
            yield False
            # Remove the binding.
            self._isBound = False
        elif self._value == arg:
            yield False

def personWithUnify(Person):
    for l1 in Person.unify("Chelsea"): yield False
    for l1 in Person.unify("Hillary"): yield False
    for l1 in Person.unify("Bill"): yield False

def main():
    print("Names using UnifyingVariable:")
    Person = UnifyingVariable()
    for l1 in personWithUnify(Person):
        print(Person._value)
main()
