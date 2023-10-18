def isfloat(st):
    try:
        float(st)
        return True
    except ValueError:
        return False

