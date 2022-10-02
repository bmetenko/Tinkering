import bpy
from bpy import context

scene = context.scene

for i in range(5):
    if i == 0:
        continue
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(i, i, 1), scale=(1/2, 1/2, 1/2))
    
for i in range(5):
    if i == 0:
        continue
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(-i, i, 1), scale=(1/2, 1/2, 1/2))

for i in range(5):
    if i == 0:
        continue
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(i, -i, 1), scale=(1/2, 1/2, 1/2))

for i in range(5):
    if i == 0:
        continue
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(-i, -i, 1), scale=(1/2, 1/2, 1/2))
        
        
bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 1), 
    scale=(1/2, 1/2, 1/2)
    )

bpy.ops.object.select_all(action='SELECT')
        
bpy.ops.object.join()

bpy.ops.object.camera_add(
    enter_editmode=False, 
    align='VIEW', 
    location=(0, -20, 20), 
    rotation=(3.14 * 1.25, 3.14158, 3.14159), 
    scale=(1, 1, 1))
    
scene.camera = context.object

bpy.ops.object.light_add(
    type='SUN', 
    radius=1, 
    align='WORLD', 
    location=(0, 0, 5), 
    scale=(1, 1, 1))

bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)

bpy.ops.render.view_show()