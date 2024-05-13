import maya.cmds as cmds

def toggle_blendshape_envelope():
    blendshapes = cmds.ls(type='blendShape')
    
    for blendshape in blendshapes:
        envelope_attr = blendshape + '.envelope'
        current_envelope = cmds.getAttr(envelope_attr)
        
        if current_envelope == 0:
            cmds.setAttr(envelope_attr, 1)
        else:
            cmds.setAttr(envelope_attr, 0)

toggle_blendshape_envelope()