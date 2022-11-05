from typing import List


class Agent:
    def __init__(self):
        self.options = dict()

    def set_option(self, option: int, value: int):
        self.options[option] = value

    def value(self, option: int) -> float:
        return self.options[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    for i in agents:
        if i.value(option1) < i.value(option2):
            return False
    return True


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for i in allOptions:
        if isParetoImprovement(agents, i, option) and i != option:
            return False
    return True


ami = Agent()
tami = Agent()
rami = Agent()
A = 1
B = 2
C = 3
D = 4
E = 5
ami.set_option(A, 1)
ami.set_option(B, 2)
ami.set_option(C, 3)
ami.set_option(D, 4)
ami.set_option(E, 5)

tami.set_option(A, 3)
tami.set_option(B, 1)
tami.set_option(C, 2)
tami.set_option(D, 5)
tami.set_option(E, 4)

rami.set_option(A, 3)
rami.set_option(B, 5)
rami.set_option(C, 5)
rami.set_option(D, 1)
rami.set_option(E, 1)

l = {ami, tami, rami}
opt = {A, B, C, D, E}

print(isParetoImprovement(l, C, B))
print(isParetoImprovement(l, A, B))
print(isParetoOptimal(l, B, opt))
