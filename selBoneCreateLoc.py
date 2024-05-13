import maya.cmds as cmds

# 获取选择的骨骼
joints = cmds.ls(sl=True, type='joint')

for joint in joints:

  # 获取骨骼的转换信息
  trans = cmds.xform(joint, q=True, translation=True, worldSpace=True)
  rot = cmds.xform(joint, q=True, rotation=True, worldSpace=True)

  # 创建locator
  loc = cmds.spaceLocator()

  # 设置locator的转换信息
  cmds.xform(loc, translation=trans, rotation=rot, worldSpace=True)

print('Locators created with aligned rotation!')