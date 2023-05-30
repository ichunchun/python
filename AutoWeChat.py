from pywinauto.application import Application
import time

SoftWare = input("请输入你想要生效的软件名字：")

app = Application("uia").connect(title_re=SoftWare)

dlg = app.window(class_name="WeChatMainWndForPC")


# 删除指定聊天内容
def del_chat(user):
    current = dlg.child_window(title=user, control_type="ListItem").wrapper_object()
    current.click_input("right")
    # 这里右键会弹出菜单，直接点击该菜单中的删除聊天选项
    app.Menu["删除聊天"].click_input("left")
    dlg.child_window(title="删除", control_type="Button").wrapper_object().click_input(
        "left"
    )


# 这个用来获取列表框里面的最后一句话，
def get_list_lastword():
    chat_list = dlg.child_window(title="会话", control_type="List")
    temp_list = []
    count = len(chat_list.children())
    limit = min(count, 9)  # 计算循环的上限，因为在COUNT等于10的时候会报错，超出范围
    for i, child in enumerate(chat_list.children()):
        if i >= limit:
            break
        single_chat = chat_list.child_window(
            title=child.window_text(), control_type="ListItem"
        )
        tt = single_chat.child_window(
            best_match="Edit3", control_type="Edit"
        ).text_block()
        temp_list.append(tt)
    return temp_list


# 获取当前窗口聊天内容并输入为列表，如果要得到最后一条get_last_msg()[-1]
def get_msg():
    msgs = dlg.child_window(title="消息", control_type="List")
    temp_list = []
    for msg in msgs.children():
        temp_list.append(msg.window_text())
    return temp_list


# 在当前页面输入内容
def input_msg(name, sms):
    dlg.set_focus()
    time.sleep(0.5)
    input_box = dlg.child_window(title=name, control_type="Edit")
    input_box.type_keys(sms, with_spaces=True, set_foreground=True)
    input_box.type_keys("{ENTER}")


def search_user(name):
    dlg.set_focus()
    search_box = dlg.child_window(title="搜索", control_type="Edit").wrapper_object()
    # search_box.draw_outline("red")
    search_box.click_input()
    search_box.type_keys(name)
    # 速度太快的话点击会失效，加0.5秒休息
    time.sleep(0.5)
    search_box.type_keys("{ENTER}")
