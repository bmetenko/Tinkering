import bpy

for i in range(10):
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(i, i, 1), scale=(1/2, 1/2, 1/2))
    
for i in range(10):
    if i != 0:
        bpy.ops.mesh.primitive_cube_add(
        size=2, 
        enter_editmode=False, 
        align='WORLD', 
        location=(-i, i, 1), scale=(1/2, 1/2, 1/2))
    
for i in range(10):
    if i != 0:
        bpy.ops.mesh.primitive_cube_add(
        size=2, 
        enter_editmode=False, 
        align='WORLD', 
        location=(i, -i, 1), scale=(1/2, 1/2, 1/2))

for i in range(10):
    if i != 0:
        bpy.ops.mesh.primitive_cube_add(
        size=2, 
        enter_editmode=False, 
        align='WORLD', 
        location=(-i, -i, 1), scale=(1/2, 1/2, 1/2))
        

bpy.ops.object.select_all(action='SELECT')
        
bpy.ops.object.join()