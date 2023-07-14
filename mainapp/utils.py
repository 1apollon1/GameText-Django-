def set_to_int(num):
    if num in map(str, range(-9, 10)):
        return int(num)
    else:
        raise ValueError('Need digit')
