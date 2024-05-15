'''
Create Helper Joint by Res Yudikata
Batam, September 22, 2020
Description :
    This script is to make helper / deformation joint which is usually needed in the rigging process, 
    instead of making corrective blendshape

how to use:  
    -specify the value,
    -Select the joint or object that requires the helper joint (ex: Elbow Joint, etc)
    -then run the script
'''

import pymel.core as pm

JointRotation_InOut = 'Y'
JointRotation_UpDown = 'Z'
Strenght_In = 15
Strenght_Out = 15
Strenght_Up = 15
Strenght_Down = 15
Position_In = 5
Position_Out = 5
Position_Up = 5
Position_Down = 5



sel=pm.ls(sl=True)
print sel

for i in sel:
    #1. delete node if exist
    helpergroup= (i+'*_SETUP')
    if pm.objExists(helpergroup):
        pm.delete(helpergroup)
        
    mdl= (i+'*_mdl')
    
    if pm.objExists(mdl):
        pm.delete (mdl)
    
    #2. create group and loc
    groupLoc=pm.group(em=True,n=i+'Helper_SETUP')
    snapgroup=pm.parentConstraint(i,groupLoc, n=i+'PAC')
    pm.delete (snapgroup)
    Loc=pm.spaceLocator(n=i+'Helper_LOC')
    snapLoc=pm.parentConstraint(i,Loc, n=i+'PAC')
    pm.delete (snapLoc)
    pm.parent(Loc,groupLoc)
    
    #3. create joint helper and reorder group
    Ij=pm.joint(n=i+'HelperInner_JNT')
    Ic=pm.group(n=i+'HelperInner_Cons')
    Iz=pm.group(n=i+'HelperInner_Zero')
    
    Oj=pm.joint(n=i+'HelperOuter_JNT')
    Oc=pm.group(n=i+'HelperOuter_Cons')
    Oz=pm.group(n=i+'HelperOuter_Zero')
    
    Uj=pm.joint(n=i+'HelperUp_JNT')
    Uc=pm.group(n=i+'HelperUp_Cons')
    Uz=pm.group(n=i+'HelperUp_Zero')
    
    Dj=pm.joint(n=i+'HelperDown_JNT')
    Dc=pm.group(n=i+'HelperDown_Cons')
    Dz=pm.group(n=i+'HelperDown_Zero')
    
    #4 parent group
    pm.parent(Oz,groupLoc)
    pm.parent(Iz,groupLoc)
    pm.parent(Uz,groupLoc)
    pm.parent(Dz,groupLoc)
    
    pm.parentConstraint(i,groupLoc, mo=1, n=groupLoc+'_PAC')


    #5. Point constraint the cons_grpto the parent_jnt(shoulder_jnt).

    Up_i = pm.listRelatives(i, p=True)
    
    pm.pointConstraint( i, Ic, mo=1, n=Ic+'_PC')
    pm.pointConstraint( i, Oc, mo=1, n=Oc+'_PC')
    pm.pointConstraint( i, Uc, mo=1, n=Uc+'_PC')
    pm.pointConstraint( i, Dc, mo=1, n=Dc+'_PC')
    


    #6. Orient constraint the cons_grp to both the parent_jnt and the bend_jnt with maintain offset checked.
    orientConsI = pm.orientConstraint(i, Ic, mo=1, n=Ic+'_OC')
    pm.orientConstraint(Up_i, Ic, mo=1)
    pm.setAttr (orientConsI+'.interpType', 2)

    orientConsO = pm.orientConstraint(i, Oc, mo=1, n=Oc+'_OC')
    pm.orientConstraint(Up_i, Oc, mo=1)
    pm.setAttr (orientConsO+'.interpType', 2)

    orientConsU = pm.orientConstraint(i, Uc, mo=1, n=Uc+'_OC')
    pm.orientConstraint(Up_i, Uc, mo=1)
    pm.setAttr (orientConsU+'.interpType', 2)

    orientConsD = pm.orientConstraint(i, Dc, mo=1, n=Dc+'_OC')
    pm.orientConstraint(Up_i, Dc, mo=1)
    pm.setAttr (orientConsD+'.interpType', 2)

    #7. Add a float attribute called 'multiplier' with the minimum value of 0 at the bend_jnt. This attribute is there to tweak how far the 'push' will go.

    Loc.addAttr('multiplierInner', keyable=True, attributeType='float', min=0.0, max=1000.0)
    Loc.addAttr('multiplierOuter', keyable=True, attributeType='float', min=0.0, max=1000.0)
    pm.setAttr(Loc+'.multiplierInner',Strenght_In)
    pm.setAttr(Loc+'.multiplierOuter',Strenght_Out)

    Loc.addAttr('multiplierUp', keyable=True, attributeType='float', min=0.0, max=1000.0)
    Loc.addAttr('multiplierDown', keyable=True, attributeType='float', min=0.0, max=1000.0)
    pm.setAttr(Loc+'.multiplierUp',Strenght_Up)
    pm.setAttr(Loc+'.multiplierDown',Strenght_Down)
    
    #8. Create 3 multDoubleLinear nodes. 1.devideDegree_mdl 2.multiplier_mdl 3.inverseValue_mdl

    MDL1_Inner = pm.shadingNode('multDoubleLinear', au=1, n=i+'devideDegreeInner_mdl')
    MDL2_Inner = pm.shadingNode('multDoubleLinear', au=1, n=i+'multiplierInner_mdl')
    MDL3_Inner = pm.shadingNode('multDoubleLinear', au=1, n=i+'inverseValueInner_mdl')


    MDL1_Outer = pm.shadingNode('multDoubleLinear', au=1, n=i+'devideDegreeOuter_mdl')
    MDL2_Outer = pm.shadingNode('multDoubleLinear', au=1, n=i+'multiplierOuter_mdl')
    MDL3_Outer = pm.shadingNode('multDoubleLinear', au=1, n=i+'inverseValueOuter_mdl')
    
    MDL1_Up = pm.shadingNode('multDoubleLinear', au=1, n=i+'devideDegreeUp_mdl')
    MDL2_Up = pm.shadingNode('multDoubleLinear', au=1, n=i+'multiplierUp_mdl')
    MDL3_Up = pm.shadingNode('multDoubleLinear', au=1, n=i+'inverseValueUp_mdl')
    
    MDL1_Down = pm.shadingNode('multDoubleLinear', au=1, n=i+'devideDegreeDown_mdl')
    MDL2_Down = pm.shadingNode('multDoubleLinear', au=1, n=i+'multiplierDown_mdl')
    MDL3_Down = pm.shadingNode('multDoubleLinear', au=1, n=i+'inverseValueDown_mdl')
  
 
    #9. Connect bend_jnt.roateY(in this case the axis is Y) to the multiplider_mdl.input1
    pm.connectAttr (i+'.rotate'+JointRotation_InOut, MDL2_Inner+'.input1')
    pm.connectAttr (i+'.rotate'+JointRotation_InOut, MDL2_Outer+'.input1')
    
    pm.connectAttr (i+'.rotate'+JointRotation_UpDown, MDL2_Up+'.input1')
    pm.connectAttr (i+'.rotate'+JointRotation_UpDown, MDL2_Down+'.input1')
    
    #10. Connect bend_jnt.multiplier to the devideDegree_mdl.input1 and set its input2 to 1/360(0.002778).
    pm.connectAttr(Loc+'.multiplierInner', MDL1_Inner+'.input1')
    pm.setAttr(MDL1_Inner+'.input2', 0.002778)
    
    pm.connectAttr(Loc+'.multiplierOuter', MDL1_Outer+'.input1')
    pm.setAttr(MDL1_Outer+'.input2', 0.002778)
    
    pm.connectAttr(Loc+'.multiplierUp', MDL1_Up+'.input1')
    pm.setAttr(MDL1_Up+'.input2', 0.002778)
    
    pm.connectAttr(Loc+'.multiplierDown', MDL1_Down+'.input1')
    pm.setAttr(MDL1_Down+'.input2', 0.002778)
    
    #11 Connect devideDegree_mdl.output to multiplier_mdl.input2.
    pm.connectAttr(MDL1_Inner+'.output', MDL2_Inner+'.input2')
    pm.connectAttr(MDL1_Outer+'.output', MDL2_Outer+'.input2')
    pm.connectAttr(MDL1_Up+'.output', MDL2_Up+'.input2')
    pm.connectAttr(MDL1_Down+'.output', MDL2_Down+'.input2')
        
    #12 Connect multiplier_mdl output to inverseValue_mdlinput 1 and set its input2 to -1
    pm.connectAttr(MDL2_Inner+'.output', MDL3_Inner+'.input1')
    pm.setAttr(MDL3_Inner+'.input2', -1)
    
    pm.connectAttr(MDL2_Outer+'.output', MDL3_Outer+'.input1')
    pm.setAttr(MDL3_Outer+'.input2', -1)

    pm.connectAttr(MDL2_Up+'.output', MDL3_Up+'.input1')
    pm.setAttr(MDL3_Up+'.input2', -1)

    pm.connectAttr(MDL2_Down+'.output', MDL3_Down+'.input1')
    pm.setAttr(MDL3_Down+'.input2', -1)
    



    #13 Create a condition node set its second term to 0 and operation to 'less than'.
    Con_Inner = pm.shadingNode('condition', au=1, n=i+'ConInner_mdl')
    pm.setAttr(Con_Inner+'.operation', 4)
    Con_Outer = pm.shadingNode('condition', au=1, n=i+'ConOuter_mdl')
    pm.setAttr(Con_Outer+'.operation', 2)

    Con_Up = pm.shadingNode('condition', au=1, n=i+'ConUp_mdl')
    pm.setAttr(Con_Up+'.operation', 4)
    Con_Down = pm.shadingNode('condition', au=1, n=i+'ConDown_mdl')
    pm.setAttr(Con_Down+'.operation', 2)


    #14 Connect multipliler_mdl.output to the conditon's firstTerm and colorIfFalseR.
    pm.connectAttr(MDL2_Inner+'.output', Con_Inner+'.firstTerm')
    pm.connectAttr(MDL2_Inner+'.output', Con_Inner+'.colorIfFalseR')
    pm.connectAttr(MDL2_Outer+'.output', Con_Outer+'.firstTerm')
    pm.connectAttr(MDL2_Outer+'.output', Con_Outer+'.colorIfFalseR')

    pm.connectAttr(MDL2_Up+'.output', Con_Up+'.firstTerm')
    pm.connectAttr(MDL2_Up+'.output', Con_Up+'.colorIfFalseR')
    pm.connectAttr(MDL2_Down+'.output', Con_Down+'.firstTerm')
    pm.connectAttr(MDL2_Down+'.output', Con_Down+'.colorIfFalseR')

    
    #15. Connect inverseValue_mdl.output to the condition node's colorIfTrueR.
    pm.connectAttr(MDL3_Inner+'.output', Con_Inner+'.colorIfTrueR')
    pm.connectAttr(MDL3_Outer+'.output', Con_Outer+'.colorIfTrueR')

    pm.connectAttr(MDL3_Up+'.output', Con_Up+'.colorIfTrueR')
    pm.connectAttr(MDL3_Down+'.output', Con_Down+'.colorIfTrueR')
    
    
    #16. Create a addDoubleLiner node, call it addTranslate_adl. Set its input2 to whatever value the
    Add_Inner = pm.shadingNode('addDoubleLinear', au=1, n=i+'AddTranslateInner_mdl')
    pm.setAttr(Add_Inner+'.input2',Position_In)
    Add_Outer = pm.shadingNode('addDoubleLinear', au=1, n=i+'AddTranslateOuter_mdl')
    pm.setAttr(Add_Outer+'.input2',-+Position_Out)    

    Add_Up = pm.shadingNode('addDoubleLinear', au=1, n=i+'AddTranslateUp_mdl')
    pm.setAttr(Add_Up+'.input2',Position_Up)
    Add_Down = pm.shadingNode('addDoubleLinear', au=1, n=i+'AddTranslateDown_mdl')
    pm.setAttr(Add_Down+'.input2',-+Position_Down)    

    #17. Connect the conditon node's outColorR to addTranslate_adl.input1.
    pm.connectAttr(Con_Inner+'.outColorR', Add_Inner+'.input1')
    pm.connectAttr(Con_Outer+'.outColorR', Add_Outer+'.input1')
    
    pm.connectAttr(Con_Up+'.outColorR', Add_Up+'.input1')
    pm.connectAttr(Con_Down+'.outColorR', Add_Down+'.input1')
    #18. Connect addTranslate_adl.output to corrective_jnt.translateZ.
    pm.connectAttr(Add_Inner+'.output', Ij+'.tz')
    pm.connectAttr(Add_Outer+'.output', Oj+'.tz')
    pm.connectAttr(Add_Up+'.output', Uj+'.ty')
    pm.connectAttr(Add_Down+'.output', Dj+'.ty')
    


    
    
    
    