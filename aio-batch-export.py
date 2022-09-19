import bpy
import glob
import sys
import time
import argparse
import os


def parse_args():
	if '--' not in sys.argv:
		argv = []
	else:
		argv = sys.argv[sys.argv.index("--") + 1:]
	
	parser = argparse.ArgumentParser(description='Olle bled')
	parser.add_argument('-f', '--format', dest="format", help='Export format', required=True)
	parser.add_argument('-s', '--source', dest="source", help='Source folder', required=True)
	parser.add_argument('-o', '--output', dest="output", help='Output folder', required=True)
	parser.add_argument('--reset-location', dest="rl", help='Reset object location', action='store_true')

	return parser.parse_args(argv)
def run():
	args = parse_args()

	args.source = os.path.abspath(args.source)
	args.output = os.path.abspath(args.output)

	print('\n\n')

	formats = dir(bpy.ops.export_scene)
	if args.format not in formats:
		print("Method %s not found. Available: %s" % (args.format, ', '.join(formats)))
		return 	

	export_function = getattr(bpy.ops.export_scene, args.format)

	# get all blend files
	for file in glob.glob(os.path.join(args.source, '**', '*.blend'), recursive=True):

		relpath = os.path.relpath(file, start=args.source)
		dirname = os.path.dirname(relpath)
		filename = os.path.basename(relpath)
		name, ext = os.path.splitext(filename)
		outpath = os.path.join(args.output, dirname)

		os.makedirs(outpath, exist_ok=True)

		bpy.ops.wm.open_mainfile(filepath=file)

		for obj in bpy.context.selected_objects:
			obj.select_set(False)

		objects = bpy.context.view_layer.objects
		for ob in objects:
			if ob.type != 'MESH':
				continue

			fp = os.path.join(outpath, '%s_%s.%s' % (name, ob.name, args.format))
			objects.active = ob
			ob.select_set(True)

			if args.rl:
				ob.location = [0.0, 0.0, 0.0]
            
			export_function(filepath=fp, use_selection=True)
			ob.select_set(False)

if __name__ == "__main__":
	run()