from gates import gate_and, gate_not, gate_or


def selector(s, a_1, a_0):
    a_1_and = gate_and(s, a_1)
    a_0_and = gate_and(gate_not(s), a_0)
    return gate_or(a_1_and, a_0_and)
