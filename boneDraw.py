import maya.cmds as cmds

# 获取选择的所有骨骼
selected_joints = cmds.ls(selection=True, type='joint')

# 循环设置骨骼的绘制样式
for joint in selected_joints:
    cmds.setAttr(joint + ".drawStyle", 2)  # 2 表示 "None"
