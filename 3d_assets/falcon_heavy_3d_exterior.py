import bpy

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create the main body
bpy.ops.mesh.primitive_cylinder_add(radius=3.7, depth=50)
main_body = bpy.context.active_object

# Create the engine section
bpy.ops.mesh.primitive_cylinder_add(radius=3.5, depth=10)
engine_section = bpy.context.active_object
engine_section.location.z = -main_body.dimensions.z / 2 - engine_section.dimensions.z / 2

# Create the engine nozzles
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=3)
engine_nozzle = bpy.context.active_object
engine_nozzle.location.z = engine_section.location.z - engine_nozzle.dimensions.z / 2

# Add engine nozzles to the engine section
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()

# Add some detail (optional)
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2

# Apply the modifier
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Add material (optional)
mat = bpy.data.materials.new(name="RocketMaterial")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
links = node_tree.links

# Create nodes
output_node = nodes.get("Material Output")
principled_bsdf = nodes.get("Principled BSDF")

# Create links
links.new(principled_bsdf.outputs['BSDF'], output_node.inputs['Surface'])

# Assign material to the rocket
main_body.data.materials.append(mat)
engine_section.data.materials.append(mat)
