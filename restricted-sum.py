def checkio(data):
    """
    It could also be something like:
    def checkio(data):
        if not data:
            return 0
        return data[0]+checkio(data[1:])
    """
    def _do(data, total):
        if data:
            return _do(data, data.pop() + total)
        else:
            return total
    
    return _do(data, total=0)
