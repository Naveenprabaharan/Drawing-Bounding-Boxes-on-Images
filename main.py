import cv2
import glob
import xml.etree.ElementTree as ET

def draw_bounding_boxes(image_path, xml_path, output_path,ouput_parent_path):
    # Read the image
    image = cv2.imread(image_path)

    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Define a dictionary to map class IDs to object names
    color_names = {"Goggle": (255, 0, 0), "Helmet": (0, 255, 0), "Person": (0, 0, 255),"Shoe":(255, 255, 0),"Vest":(128, 0, 128)}  # Customize as needed

    # Loop through all object tags in the XML file
    for obj in root.findall('object'):
        # Extract object name and bounding box coordinates
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # Draw the bounding box on the image
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color_names[name], 2)

        # Put text label with object name
        label = f"{name}: {xmin}, {ymin}, {xmax}, {ymax}"
        cv2.putText(image, label, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_names[name], 1, cv2.LINE_AA)

    op_path = f'{ouput_parent_path}{output_path}'
    print(op_path)
    # Save the annotated image
    cv2.imwrite(op_path, image)

# Example usage
if __name__ == "__main__":
    ouput_parent_path = '/home/cognitica-i7-13thgen/NPS/drawBoundingBox/img_with_BB/'
    folder_datapath = '/home/cognitica-i7-13thgen/Downloads/PPEDEV02.v1i.voc_V9.4/PPEDEV02.v1i.voc/valid/*.xml'
    datas_path = glob.glob(folder_datapath)


    for xml_path in datas_path:
        img_path = xml_path[:-3]+'jpg'
        output_img_name = img_path.split('/')[-1]
        print(img_path)
        print(xml_path)
        print(output_img_name)
        # try:
        draw_bounding_boxes(img_path, xml_path, output_img_name,ouput_parent_path)
        # except Exception as error:
            # print(error)
