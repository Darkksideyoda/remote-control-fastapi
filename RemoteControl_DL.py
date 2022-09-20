from imageai.Detection import ObjectDetection
import PIL.Image


imgSrc = "data/myImageData/img5.jpg"

obj_detect  = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()


obj_detect.setModelPath("yolo.h5")
obj_detect.loadModel()


obj_detect.CustomObjects(remote=True)


detected_obj = obj_detect.detectObjectsFromImage(
    input_image=imgSrc,
    output_image_path="test_image_output.jpg",
    minimum_percentage_probability=20,
    
)


for obj in detected_obj:
    if obj["name"] == "remote":
        print("Remote Control Detected !\n")
        print(obj["percentage_probability"])
        print(obj["box_points"])
        outputImgOpen =  PIL.Image.open(imgSrc)
        croppedImg = outputImgOpen.crop((obj["box_points"]))
        croppedImg.save("test_image_output.jpg")        
        

    else:
        print("We Can't Find Remote Try Again !")

im = PIL.Image.open("test_image_output.jpg")
im.show()
