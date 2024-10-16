from ansi import color_cat
from utils import input_to, write


welcome = "welcome"


class Player:
    def __init__(self):
        self.id = ""

    def __str__(self):
        return f"Player {{ id: {self.id} }}"


def logon():
    color_cat(welcome)
    player = Player()
    write("您的英文名字(新玩家可以选择一喜欢的名字)：")
    input_to(get_id, player)


def get_id(arg: str, player):
    player.id = arg
    print(player)


if __name__ == "__main__":
    logon()
