import maya.cmds as cmds

# 获取所有 animCurveUU 节点
anim_curve_nodes = cmds.ls(type='animCurveUU')

# 遍历 animCurveUU 节点列表，检查是否有输出连接
for node in anim_curve_nodes:
    outputs = cmds.listConnections(node, source=False, destination=True)
    if not outputs:
        # 删除没有输出连接的 animCurveUU 节点
        cmds.delete(node)
        print("Deleted animCurveUU node with no output connections: {}".format(node))