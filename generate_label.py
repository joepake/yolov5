TemplateLabel = "<annotation><folder>labeled</folder><filename>$filename</filename><path>$path</path><size><width>$width</width><height>$height</height><depth>3</depth></size><segmented>0</segmented><object><name>$label</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox><xmin>$xmin</xmin><ymin>$ymin</ymin><xmax>$xmax</xmax><ymax>$ymax</ymax></bndbox></object></annotation>"

def generateLabel(root, filename, path, width, height, label, xmin, ymin, xmax, ymax):
    content = TemplateLabel.replace('$filename', filename).replace('$path', path).replace('$width', width).replace('$height', height).replace('$label', label).replace('$xmin', xmin).replace('$ymin', ymin).replace('$xmax', xmax).replace('$ymax', ymax)
    
    with open(f"{root}/{filename.split('.')[0]}.xml", "w") as outfile:
        outfile.write(content)