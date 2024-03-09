import ca_lib as lib

x = lib.init_ca(200)

for i in range(256):

    rule = lib.get_rule(i)
    c = lib.evolve(x, 200, rule)
    print(rule)
    lib.plot(c)
