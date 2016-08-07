
class UnifyingVariable:
    def __init__(self):
        self._isBound = False

    def unify(self, arg):
        if not self._isBound:
            self._value = arg
            self._isBound = True
            yield None
            # Remove the binding.
            self._isBound = False
        elif self._value == arg:
            yield None
            
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
            yield None
    elif arg2Value.__class__ == UnifyingVariable:
        for l1 in arg2Value.unify(arg1Value):
            yield None
    else:
        # Arguments are "normal" nonVar types.
        if arg1Value == arg2Value:
            yield None


def brother(Person, Brother):    
    for l1 in generalUnify(Person, "Hillary"):
        for l2 in generalUnify(Brother, "Tony"):
            yield None
        for l2 in generalUnify(Brother, "Hugh"):
            yield None
    for l1 in generalUnify(Person, "Bill"):
        for l2 in generalUnify(Brother, "Roger"):
            yield None

def main():
    print("Find relations:")
    Brother = UnifyingVariable()
    for l1 in brother("Hillary", Brother):
        print l1,("Hillary has brother " + 
      Brother._value + ".")
main()
