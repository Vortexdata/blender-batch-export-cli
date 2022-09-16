import bpy
import os


def run():
	# deselect all objects
	for obj in bpy.context.selected_objects:
		print("Hello")
		obj.select_set(False) 

	objects = bpy.context.view_layer.objects
	for ob in objects:
		objects.active = ob
		ob.select_set(True)

		if ob.type == 'MESH':
			bpy.ops.export_scene.obj(filepath=os.path.join(os.environ['BBEC_EXPORT_PATH'], ob.name + os.environ['BBEC_EXPORT_FORMAT']), use_selection=True)

		ob.select_set(False)


if __name__ == "__main__":
	run()
