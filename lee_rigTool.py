import maya.cmds as cmds

# 定义子按钮尺寸
sub_button_w = 115
sub_button_h = 44

# 定义Skin和BS按钮尺寸
tab_w = 350
tab_h = 200

def create_skin_window():
    # 检查窗口是否已存在，如果存在则删除
    if cmds.window("skinWindow", exists=True):
        cmds.deleteUI("skinWindow")
    
    # 创建主窗口
    window = cmds.window("skinWindow", title="皮肤工具", widthHeight=(tab_w, tab_h))
    
    # 创建主布局
    main_layout = cmds.columnLayout(adjustableColumn=True)
    
    # 创建标签页布局
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    
    # 创建Skin标签页
    skin_tab = cmds.columnLayout(adjustableColumn=True)
    skin_row = cmds.rowLayout(numberOfColumns=3, columnWidth3=(sub_button_w, sub_button_w, sub_button_w), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
    skin_button1 = cmds.button(label="皮肤工具1", command=lambda x: print("皮肤工具1被点击"), width=sub_button_w, height=sub_button_h)
    skin_button2 = cmds.button(label="皮肤工具2", command=lambda x: print("皮肤工具2被点击"), width=sub_button_w, height=sub_button_h)
    skin_button3 = cmds.button(label="皮肤工具3", command=lambda x: print("皮肤工具3被点击"), width=sub_button_w, height=sub_button_h)
    cmds.setParent('..')  # 返回到skin_tab
    cmds.setParent('..')  # 返回到tabs
    
    # 创建BS标签页
    bs_tab = cmds.columnLayout(adjustableColumn=True)
    bs_row = cmds.rowLayout(numberOfColumns=3, columnWidth3=(sub_button_w, sub_button_w, sub_button_w), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
    bs_button1 = cmds.button(label="BS工具1", command=lambda x: print("BS工具1被点击"), width=sub_button_w, height=sub_button_h)
    bs_button2 = cmds.button(label="BS工具2", command=lambda x: print("BS工具2被点击"), width=sub_button_w, height=sub_button_h)
    bs_button3 = cmds.button(label="BS工具3", command=lambda x: print("BS工具3被点击"), width=sub_button_w, height=sub_button_h)
    cmds.setParent('..')  # 返回到bs_tab
    cmds.setParent('..')  # 返回到tabs
    
     # 创建Other标签页
    Other_tab = cmds.columnLayout(adjustableColumn=True)
    Other_row = cmds.rowLayout(numberOfColumns=3, columnWidth3=(sub_button_w, sub_button_w, sub_button_w), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
    Other_button1 = cmds.button(label="Other工具1", command=lambda x: print("Other工具1被点击"), width=sub_button_w, height=sub_button_h)
    Other_button2 = cmds.button(label="Other工具2", command=lambda x: print("Other工具2被点击"), width=sub_button_w, height=sub_button_h)
    Other_button3 = cmds.button(label="Other工具3", command=lambda x: print("Other工具3被点击"), width=sub_button_w, height=sub_button_h)
    cmds.setParent('..')  # 返回到Other_tab
    cmds.setParent('..')  # 返回到tabs

    # 设置标签页
    cmds.tabLayout(tabs, edit=True, tabLabel=((skin_tab, 'Skin'), (bs_tab, 'BS'), (Other_tab, 'other')))
    
    # 显示窗口
    cmds.showWindow(window)

# 运行创建窗口的函数
create_skin_window()