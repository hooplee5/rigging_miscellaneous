import maya.cmds as cmds

# 定义刷新Driver列表框的函数
def refreshDriverList(*args):
    selected_objects = cmds.ls(selection=True)  # 获取当前选择的物体
    object_names = ', '.join(selected_objects)  # 将物体名称用逗号隔开
    cmds.scrollField(driver_list_text, edit=True, text=object_names)  # 更新Driver列表框中的物体名称

# 定义刷新Driven列表框的函数
def refreshDrivenList(*args):
    selected_objects = cmds.ls(selection=True)  # 获取当前选择的物体
    object_names = ', '.join(selected_objects)  # 将物体名称用逗号隔开
    cmds.scrollField(driven_list_text, edit=True, text=object_names)  # 更新Driven列表框中的物体名称

# 定义执行BlendShape操作的函数
def createBlendShape(*args):
    driver_objects = cmds.scrollField(driver_list_text, query=True, text=True).split(', ')  # 获取Driver列表框中的物体名称
    driven_objects = cmds.scrollField(driven_list_text, query=True, text=True).split(', ')  # 获取Driven列表框中的物体名称

    if len(driver_objects) != len(driven_objects):
        cmds.warning("The number of driver objects does not match the number of driven objects!")
        return

    for i in range(len(driver_objects)):
        blendshape_node = cmds.blendShape(driver_objects[i], driven_objects[i])[0]  # 创建BlendShape节点
        cmds.setAttr(blendshape_node + '.' + driver_objects[i], 1)  # 设置BlendShape权重为1

# 创建窗口和布局
window = cmds.window(title="BlendShape Objects", widthHeight=(400, 200))
cmds.columnLayout()

# 创建Driver按钮和列表框
cmds.text(label="Driver Objects:")
driver_list_text = cmds.scrollField(wordWrap=False, editable=False, height=80)
driver_button = cmds.button(label="Refresh Driver List", command=refreshDriverList)

# 创建Driven按钮和列表框
cmds.text(label="Driven Objects:")
driven_list_text = cmds.scrollField(wordWrap=False, editable=False, height=80)
driven_button = cmds.button(label="Refresh Driven List", command=refreshDrivenList)

# 创建BlendShape按钮
blendshape_button = cmds.button(label="Create BlendShape", command=createBlendShape)

cmds.showWindow(window)