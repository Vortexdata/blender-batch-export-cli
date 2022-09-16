import bpy
import os


def run():
	# get blender filename
	filename = os.path.split(bpy.data.filepath)[-1]

	# deselect all objects
	for obj in bpy.context.selected_objects:
		
		obj.select_set(False) 

	objects = bpy.context.view_layer.objects
	for ob in objects:
		objects.active = ob
		ob.select_set(True)

		if ob.type == 'MESH':
			fp=os.path.join(os.environ['BBEC_EXPORT_PATH'], os.path.splitext(filename)[0] + "_" + ob.name + "." + os.environ['BBEC_EXPORT_FORMAT'])
			if os.environ['BBEC_EXPORT_FORMAT'].lower() == 'fbx':
				bpy.ops.export_scene.fbx(filepath=fp, use_selection=True)
			elif os.environ['BBEC_EXPORT_FORMAT'].lower() == 'obj':
				bpy.ops.export_scene.obj(filepath=fp, use_selection=True)
			elif os.environ['BBEC_EXPORT_FORMAT'].lower() == 'gltf':
				bpy.ops.export_scene.gltf(filepath=fp, use_selection=True)
			elif os.environ['BBEC_EXPORT_FORMAT'].lower() == 'x3d':
				bpy.ops.export_scene.x3d(filepath=fp, use_selection=True)
			else:
				print("Unknown export format '" + os.environ['BBEC_EXPORT_FORMAT'] + "'!")

		ob.select_set(False)


if __name__ == "__main__":
	run()
