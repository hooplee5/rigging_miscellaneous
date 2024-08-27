import maya.cmds as cmds

# 设置变量
blendShapeNode = "blendShape1"  # 这里替换为你的blendShape节点名称
targets = cmds.listAttr(blendShapeNode + ".weight", multi=True)  # 获取所有目标的权重属性
targetCount = len(targets)  # 获取目标数量

# 遍历所有目标，并为每个目标设置关键帧
for i in range(targetCount):
    for frame in range(1, targetCount + 1):
        cmds.setKeyframe(f"{blendShapeNode}.w[{i}]", time=frame, value=1.0 if i == frame - 1 else 0.0)