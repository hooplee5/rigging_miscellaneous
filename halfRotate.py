import maya.cmds as cmds

def connect_rotateZ(first_bone, second_bone):
    # 创建一个multiplyDivide节点
    multiply_node = cmds.createNode('multiplyDivide')
    
    # 将第一个骨骼的rotateZ属性连接到multiplyDivide节点的input1X
    cmds.connectAttr(first_bone + '.rotateZ', multiply_node + '.input1X')
    
    # 设置multiplyDivide节点的input2X为0.5
    cmds.setAttr(multiply_node + '.input2X', 0.5)
    
    # 将multiplyDivide节点的outputX连接到第二个骨骼的rotateZ属性
    cmds.connectAttr(multiply_node + '.outputX', second_bone + '.rotateZ')

# 选择需要操作的两个骨骼
first_bone = cmds.ls(selection=True)[0]
second_bone = cmds.ls(selection=True)[1]

# 调用函数进行操作
connect_rotateZ(first_bone, second_bone)
