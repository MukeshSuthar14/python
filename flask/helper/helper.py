def isset(var):
    try:
        return True if var() != None else False;
    except:
        return False;

def empty(var):
    if isset(lambda: var):
        return True if var == 0 and len(var) == 0 else False;
    else:
        return False;