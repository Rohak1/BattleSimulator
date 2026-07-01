class Action:
    pass


class Attack(Action):

    def __init__(self, target):
        self.target = target


class Critical(Action):

    def __init__(self, target):
        self.target = target


class Heal(Action):

    pass

