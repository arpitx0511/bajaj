def is_out_of_range(value, low, high):
    if low is not None and value < low:
        return True
    if high is not None and value > high:
        return True
    return False
