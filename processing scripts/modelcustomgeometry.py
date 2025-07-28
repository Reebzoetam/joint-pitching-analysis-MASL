from lxml import etree
import os

#USER INPUT
custom_geometry_folder = "/Users/...."  # <- change to absolute path to geometry ULB folder
input_osim_file = "/Users/....."  # <- change to ULB .osim file path
output_folder = "/Users/......" # <- change to desired output folder path

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"📁 Created output folder: {output_folder}")

# Collect all .vtp filenames from the folder
geometry_files = {
    f for f in os.listdir(custom_geometry_folder)
}

# Parse the .osim file
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(input_osim_file, parser)
root = tree.getroot()

#Search for any XML element whose text matches a .vtp filename and update it
updated_count = 0

for elem in root.iter():
    if elem.text:
        text = elem.text.strip()
        base = os.path.basename(text)  # get just the filename
        if base in geometry_files:
            elem.text = os.path.join(custom_geometry_folder, base)
            updated_count += 1

print(f"✅ Updated {updated_count} XML element(s) that referenced .vtp geometry files.")

#Save the updated model
output_osim_file = os.path.join(output_folder, "customgeometry_ULBmodel.osim") # <- change to desired output filename as needed
tree.write(output_osim_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
print(f" Saved updated model to: {output_osim_file}")
