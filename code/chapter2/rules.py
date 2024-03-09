def get_rule(index: int):
    assert(index < 255, "Hey, we only have 256 rules, so keep the index between 0 - 255")
    return [int(i) for i in '{0:08b}'.format(index)]