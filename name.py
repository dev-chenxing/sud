from ansi import write

family_name = ["东方", "独孤", "慕容", "欧阳", "司马",
               "西门", "尉迟", "长孙", "诸葛", "上官",
               "夏候", "闻人", "皇甫", "澹台", "公治",
               "淳于", "申屠", "公孙", "公羊", "轩辕",
               "令狐", "钟离", "宇文", "幕容", "仲孙",
               "司徒", "司空", "端木", "公良", "百里",
               "东郭", "南郭", "呼延", "羊舌", "东门",
               "南官", "南宫", "拓拔", "完颜", "耶律",
               "鲜于"]


def invalid_new_name(name: str):
    if len(name) < 1:
        return "不能使用空名字。\n"

    if name in family_name:
        return "不能使用家族名作为名字。\n"

    # assure_map_name(name);
    # id = query(PATH(name))
    # if id:
        return "这个名字和 " + id + " 的名字重复了。\n"

    return False
