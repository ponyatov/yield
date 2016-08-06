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
    for l1 in Person.unify("Chelsea"):
        yield False
    for l1 in Person.unify("Hillary"): # Person = "Hillary"
        yield False
    for l1 in Person.unify("Bill"):
        yield False

# def main():
#     print("Names using UnifyingVariable:")
#     Person = UnifyingVariable()
#     for l1 in personWithUnify(Person):
#         print(Person._value)
def main():
    print("Use unify to check a person:")
    Person = UnifyingVariable()
    for l1 in Person.unify("Hillary"):
        for l2 in personWithUnify(Person):
            print("Hillary is a person.")
    for i0 in personWithUnify(Person):      # personWithUnify(Person)
        for i1 in Person.unify("Hillary"):  # Person = "Hillary"
            print i0,i1,Person
    for l1 in Person.unify("Buddy"):
        for l2 in personWithUnify(Person):
            # This won't print.
            print("Buddy is a person.")
main()
