import maya.cmds as cmds

def toggle_selected_objects_visibility():
    # 获取当前选中的物体列表
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        print("Error: No objects selected.")
        return

    for obj in selected_objects:
        # 获取物体的所有 Shape 节点
        shape_nodes = cmds.listRelatives(obj, shapes=True, fullPath=True)

        if not shape_nodes:
            continue

        for shape_node in shape_nodes:
            # 获取 Shape 节点的 Visibility 属性的当前值
            visibility_value = cmds.getAttr(shape_node + ".visibility")

            # 切换 Visibility 属性的值（0 表示不可见，1 表示可见）
            new_visibility_value = 1 - visibility_value

            # 设置新的 Visibility 属性值
            cmds.setAttr(shape_node + ".visibility", new_visibility_value)

        print("Toggled visibility for shapes of object: {}".format(obj))

# 执行脚本，切换所选物体的 Shape 节点 Visibility 属性
toggle_selected_objects_visibility()