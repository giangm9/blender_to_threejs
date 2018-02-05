import IPython, hmi_exporter, bpy, os
#hmi_exporter.export_no_animation("output/cubeC.json")
file_name = bpy.path.basename(bpy.context.blend_data.filepath)
file_name = os.path.splitext(file_name)[0]

hmi_exporter.export_no_animation("output/" + file_name + ".json")
# IPython.embed()