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
			bpy.ops.export_scene.obj(filepath=os.path.join(os.environ['BBEC_EXPORT_PATH'], os.path.splitext(filename)[0] + "_" + ob.name + os.environ['BBEC_EXPORT_FORMAT']), use_selection=True)

		ob.select_set(False)


if __name__ == "__main__":
	run()
