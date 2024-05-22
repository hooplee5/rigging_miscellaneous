import maya.cmds as cmds

# 选择所有的骨骼
bones = cmds.ls(type='joint')

# 打开"enable overrides"并设置颜色为蓝色
for bone in bones:
    cmds.setAttr(bone + ".overrideEnabled", 1)
    cmds.setAttr(bone + ".overrideColor", 6)  # 蓝色的颜色索引为6