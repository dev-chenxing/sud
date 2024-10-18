from crypt import crypt
import os
from ansi import color_cat, write
from charset import is_chinese
from player import Player
from user import query_save_file
from utils import input_to
import name


welcome = "welcome"


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
    id = arg.lower().strip()
    if not check_legal_id(id):
        write("请输入用户名（登录/新玩家注册）：")
        input_to(get_id)
        return
    player = Player(id=arg)
    if os.path.exists(query_save_file(id)):
        write("请输入密码：")
        input_to(get_password, player)
        return
    write(f"确定创建一个新的用户[[bold cyan]{
          id}[normal]]吗 ([bold green]y[normal]/[bold red]n[normal])？")
    input_to(confirm_id, arg, player)


def get_password(arg: str, player: Player):
    write("[red]功能未实现[normal]")


def confirm_id(yes_or_no: str, id: str, player: Player):
    if (yes_or_no == ""):
        write(f"确定创建一个新的用户[[bold cyan]{
            id}[normal]]吗 ([bold green]y[normal]/[bold red]n[normal])？")
        input_to(confirm_id, id, player)
        return

    if (yes_or_no.lower()[0] != 'y'):
        del player
        write("好吧，那么请重新输入您的英文名字：")
        input_to(get_id)
        return

    write("[bold green]\n\
请输入您的高姓大名，由于这个名字将代表你的人物，而且以后不会再\n\
作任何更改，请务必慎重择名。[bold red]不雅观或带有政治色彩的姓名将被无条\n\
件删除。[bold green]此外，请不要选择金庸小说中已有人物姓名。首先输入的是姓\n\
氏，假如你想扮演的角色叫做「[bold white]张三[bold green]」的话，请先输入「[bold white]张[bold green]」，然后电\n\
脑会询问你的名字，那时你再输入「[bold white]三[bold green]」。如果你想扮演的角色的名字\n\
比较怪，比如叫「恐龙」，可以不输入姓，直接敲回车略过。但是建议\n\
你还是输入一个比较像样子的姓名，而这些比较怪的称号可以用昵称代\n\
替，否则某些地方的称呼可能会比较怪。如果你要加入世家，那就不必\n\
输入姓了，因为加入世家后将自动选择家传祖姓，并不是玩家自己决定。\n\n[normal]")

    write("您的中文[bold green]姓氏[normal](不要超过两个汉字)：")
    input_to(get_surname, player)


def check_legal_name(name: str, max_length: int):
    i = len(name)
    if not is_chinese(name):
        write("[white]对不起，请您用「[bold yellow]中文[normal][white]」取名字。[normal]\n")
        return False

    if ((i < 1) or (i > max_length)):
        write("[white]对不起，你的中文姓名不能太长。\n[normal]")
        return False

    return True


def get_surname(arg: str, player: Player):
    if len(arg) > 0:
        if (not check_legal_name(arg, 2)):
            write("请输入您的中文[bold green]姓氏[normal](不要超过两个汉字)：")
            input_to(get_surname)
            return
        player.surname = arg
    else:
        player.surname = ""
    write("请输入您的中文[bold yellow]名字[normal](不要超过两个汉字)：")
    input_to(get_name, player)


def get_name(arg: str, player: Player):
    if (not check_legal_name(arg, 2)):
        write("您的中文[bold yellow]名字[normal](不要超过两个汉字)：")
        input_to(get_name, player)
        return

    player.given_name = arg
    full_name = player.surname + arg

    if len(full_name) < 2:
        write("对不起，你的中文名字（姓和名的组合）至少要有两个汉字。\n")
        write("\n请重新输入您中文[bold green]姓氏[normal]：")
        input_to(get_surname, player)
        return

    result = name.invalid_new_name(full_name) or name.invalid_new_name(arg)
    if result:
        write("对不起，" + result)
        write("\n请重新输入您中文[bold green]姓氏[normal]：")
        input_to(get_surname, player)
        return

    if arg == player.surname:
        write(f"[bold white]\n\
[bold green]系统发现你所输入的姓氏与名字相同，不知你是否因为不了解本游戏的\n\
设定，并且没有仔细阅读前面给出的帮助而导致错误的输入姓名。如果\n\
是，请你重新连接并且输入你的名字，否则请你再次输入一遍你的全名\n\
表明你的确是想使用「[bold yellow]{arg}{arg}[bold green]」这个名字。\n\n[normal]")
        write("请输入您的全名(即姓和名字的组合)：")
        input_to(input_full_name, player, arg + arg)
        return

    write("[bold white]\n\
为了保证您的人物的安全，游戏要求您设置两个密码。第一个是管理密\n\
码，这个密码可以在您遗失了普通密码时登录游戏，并且可以用来修改\n\
您的普通密码。平时登陆游戏时请您尽量使用普通密码，此举将会避免\n\
过于频繁的使用管理密码以导致潜在的泄漏风险。\n\n[normal]")

    write("请设定您的[bold white]管理密码[normal]：")
    input_to("new_ad_password", 1, player)


def input_full_name(arg: str, player: Player,  full_name: str):
    if arg != full_name:
        write("[white]\n\
你输入的全名并不是你姓和名字的的组合，系统认为你开始没有理解输\n\
入名字的要求，[bold red]请你仔细阅读所有提示的条款，不要自作聪明。[normal]包括在\n\
今后的游戏过程中请仔细阅读各种帮助和公告，避免因为自以为是而导\n\
致浪费时间或是遭受不必要的损失。")
        confirm_id("y", player)
        return

    write("[bold white]\n\
为了保证您的人物的安全，游戏要求您设置两个密码。第一个是管理密\n\
码，这个密码可以在您遗失了普通密码时登录游戏，并且可以用来修改\n\
您的普通密码。平时登陆游戏时请您尽量使用普通密码，此举将会避免\n\
过于频繁的使用管理密码以导致潜在的泄漏风险。\n\n[normal]")

    write("请设定您的[bold white]管理密码[normal]：")
    input_to(new_ad_password, player)


def new_ad_password(password: str, player: Player):
    write("\n")
    if len(password) < 5:
        write("管理密码的长度至少要5位，请重设您的管理密码：")
        input_to(new_ad_password, player)
        return

    player.ad_password = crypt.crypt(password)
    print(player.ad_password)
    write("请再输入一次您的[bold white]管理密码[normal]，以确认您没记错：")
    input_to(confirm_ad_password, player)


def confirm_ad_password():
    pass
