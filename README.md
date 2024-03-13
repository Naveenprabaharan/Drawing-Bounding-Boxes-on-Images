## Code: Drawing Bounding Boxes on Images

This Python script reads XML annotation files containing bounding box information and draws the bounding boxes on the corresponding images. It uses the OpenCV library for image manipulation.

### Functionality
- **Input**: 
    - Path to an image file.
    - Path to the corresponding XML file containing object annotations.
- **Output**: 
    - Annotated image with bounding boxes drawn around the objects, saved to the specified output directory.
- **Object Detection**: 
    - Parses the XML file to extract object names and bounding box coordinates.
    - Draws bounding boxes and object labels on the image.
- **Customization**:
    - Object names and their corresponding colors are defined in a dictionary.
    - Customize the dictionary according to the specific object classes in your dataset.
- **Error Handling**:
    - The script handles exceptions gracefully and continues processing the remaining images even if an error occurs with one image.

### Usage
1. **Setup**: 
    - Ensure that Python, OpenCV, and the required libraries are installed.
2. **Input Data**:
    - Place your image files (.jpg) and corresponding XML annotation files in the specified directory.
3. **Execution**:
    - Run the script, providing the paths to the image and XML files.
4. **Output**:
    - Annotated images with bounding boxes will be saved in the specified output directory.

### Example Usage
```python
if __name__ == "__main__":
    ouput_parent_path = '/home/cognitica-i7-13thgen/NPS/drawBoundingBox/img_with_BB/'
    folder_datapath = '/home/cognitica-i7-13thgen/Downloads/PPEDEV02.v1i.voc_V9.4/PPEDEV02.v1i.voc/valid/*.xml'
    datas_path = glob.glob(folder_datapath)

    for xml_path in datas_path:
        img_path = xml_path[:-3]+'jpg'
        output_img_name = img_path.split('/')[-1]
        draw_bounding_boxes(img_path, xml_path, output_img_name, ouput_parent_path)
