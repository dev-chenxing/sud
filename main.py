import os
from ansi import color_cat, write
from user import query_save_file
from utils import input_to


welcome = "welcome"


class Player:
    def __init__(self):
        self.id = ""

    def __str__(self):
        return f"Player {{ id: {self.id} }}"


illegal_id = ["admin", "exit"]


def check_legal_id(id: str) -> bool:
    if id in illegal_id:
        write(f"对不起，[bold cyan]“{id}”[normal]保留供内部使用，不能用作用户名。\n")
        return False

    i = len(id)
    if i < 3 or i > 10:
        write(
            "[white]对不起，用户名必须是 [bold yellow]3 [normal]到 [bold yellow]10[normal] 位\n")
        return False
    while i > 0:
        i = i-1
        if id[i] < 'a' or id[i] > 'z':
            write("对不起，用户名只能输入英文字母。\n")
            return False

    return True


def logon():
    color_cat(welcome)
    write("请输入用户名（登录/新用户创建）：")
    input_to(get_id)


def get_id(arg: str):
    arg = arg.lower().strip()
    if not check_legal_id(arg):
        write("请输入用户名（登录/新玩家注册）：")
        input_to(get_id)
        return
    if os.path.exists(query_save_file(arg)):
        write("请输入密码：")
        input_to(get_password)
        return
    write(f"确定创建一个新的用户[[bold cyan]{
          arg}[normal]]吗 ([bold green]y[normal]/[bold red]n[normal])？")
    input_to(confirm_id)


def get_password():
    pass


def confirm_id():
    pass


if __name__ == "__main__":
    logon()
