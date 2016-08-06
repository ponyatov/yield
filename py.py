from __builtin__ import False
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
            
def generalGetValue(value):
    if value.__class__ == UnifyingVariable: 
        if value._isBound:
            return value._value
        else:
            return value
    else:
        return value

def generalUnify(arg1, arg2):
    arg1Value = generalGetValue(arg1)
    arg2Value = generalGetValue(arg2)
    if arg1Value.__class__ == UnifyingVariable:
        for l1 in arg1Value.unify(arg2Value):
            yield False
    elif arg2Value.__class__ == UnifyingVariable:
        for l1 in arg2Value.unify(arg1Value):
            yield False
    else:
        # Arguments are "normal" nonVar types.
        if arg1Value == arg2Value:
            yield False


# def personWithUnify(Person):
#     for l1 in Person.unify("Chelsea"):
#         yield False
#     for l1 in Person.unify("Hillary"): # Person = "Hillary"
#         yield False
#     for l1 in Person.unify("Bill"):
#         yield False
        
def person(Person):
    for l1 in generalUnify(Person, "Chelsea"):  # Person = "Chelsea"
        yield False
    for l1 in generalUnify(Person, "Hillary"):
        yield False
    for l1 in generalUnify(Person, "Bill"):
        yield False

# def main():
#     print("Names using UnifyingVariable:")
#     Person = UnifyingVariable()
#     for l1 in personWithUnify(Person):
#         print(Person._value)

# def main():
#     print("Use unify to check a person:")
#     Person = UnifyingVariable()
#     for l1 in Person.unify("Hillary"):
#         for l2 in personWithUnify(Person):
#             print("Hillary is a person.")
#     for i0 in personWithUnify(Person):      # personWithUnify(Person)
#         for i1 in Person.unify("Hillary"):  # Person = "Hillary"
#             print i0,i1,Person
#     for l1 in Person.unify("Buddy"):
#         for l2 in personWithUnify(Person):
#             # This won't print.
#             print("Buddy is a person.")

def main():
    print("Use generalUnify to check a person:")
    for l1 in person("Hillary"):
        print("Hillary is a person.")
    for l1 in person("Buddy"):
        # This won't print.
        print ("Buddy is a person.")
main()
