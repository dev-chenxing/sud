from utils import read_file


esc = "\033"
csi = esc + "["  # Control Sequence Introducer


def sgr(text: str): return csi + text + "m"  # Select Graphic Rendition


black = sgr("30")
red = sgr("31")
green = sgr("32")
yellow = sgr("33")
blue = sgr("34")
magenta = sgr("35")
cyan = sgr("36")
white = sgr("37")
bold_black = sgr("1;30")
bold_red = sgr("1;31")
bold_green = sgr("1;32")
bold_yellow = sgr("1;33")
bold_blue = sgr("1;34")
bold_magenta = sgr("1;35")
bold_cyan = sgr("1;36")
bold_white = sgr("1;37")
normal = sgr("0")


def color_filter(content: str):

    if not content:
        return ""

    # Foreground color
    content = content.replace("[black]", black)
    content = content.replace("[red]", red)
    content = content.replace("[green]", green)
    content = content.replace("[yellow]", yellow)
    content = content.replace("[blue]", blue)
    content = content.replace("[magenta]", magenta)
    content = content.replace("[cyan]", cyan)
    content = content.replace("[white]", white)
    content = content.replace("[bold red]", bold_red)
    content = content.replace("[bold green]", bold_green)
    content = content.replace("[bold yellow]", bold_yellow)
    content = content.replace("[bold blue]", bold_blue)
    content = content.replace("[bold magenta]", bold_magenta)
    content = content.replace("[bold cyan]", bold_cyan)
    content = content.replace("[bold white]", bold_white)
    content = content.replace("[normal]", normal)

    return content


def color_cat(file: str):
    print(color_filter(read_file(file)))
