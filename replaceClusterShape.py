import maya.cmds as cmds

cmds.cluster('ball', weightedNode=['ctrl_1', 'ctrl_1'])

//ball是mesh的名称，ctrl_1是想替换的transfor的名称，可以是任何