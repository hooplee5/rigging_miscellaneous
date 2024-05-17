import maya.cmds as cmds

def zero_out_selected_controllers():
    selection = cmds.ls(selection=True)
    
    if not selection:
        cmds.warning("请先选择需要归零的控制器！")
        return
    
    for obj in selection:
        # 归零位移
        cmds.setAttr(obj + ".translateX", 0)
        cmds.setAttr(obj + ".translateY", 0)
        cmds.setAttr(obj + ".translateZ", 0)
        
        # 归零旋转
        cmds.setAttr(obj + ".rotateX", 0)
        cmds.setAttr(obj + ".rotateY", 0)
        cmds.setAttr(obj + ".rotateZ", 0)
        
        # 归一缩放
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
        
        # 归零自定义属性
        user_attrs = cmds.listAttr(obj, userDefined=True) or []
        for attr in user_attrs:
            default_value = cmds.attributeQuery(attr, node=obj, ld=True)[0]
            cmds.setAttr(obj + "." + attr, default_value)
    
    cmds.select(clear=True)
    cmds.select(selection)

zero_out_selected_controllers()