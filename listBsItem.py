import maya.cmds as cmds

# 获取场景中所有的BlendShape节点
blendshapes = cmds.ls(type='blendShape')

# 统计BlendShape节点中的目标项数量
total_items = 0
for blendshape in blendshapes:
    targets = cmds.blendShape(blendshape, q=True, weight=True)
    total_items += len(targets)

print("场景中总共有 {} 个BlendShape项。".format(total_items))