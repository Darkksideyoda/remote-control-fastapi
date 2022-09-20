from imageai.Detection import ObjectDetection
import os

imgOutput = "image_output.jpg"

def get_img_src(src):
    return src


def config_remote_detection(img, probability):
    obj_detect = ObjectDetection()
    obj_detect.setModelTypeAsYOLOv3()

    obj_detect.setModelPath("yolo.h5")
    obj_detect.loadModel()

    obj_detect.CustomObjects(remote=True)

    detected_obj = obj_detect.detectObjectsFromImage(
        input_image=get_img_src(img),
        output_image_path=imgOutput,
        minimum_percentage_probability=probability,
    )
    os.remove(imgOutput)
    os.remove(img)
    return detected_obj


def find_remote(img, probability):
    remote_detected = config_remote_detection(img, probability)
    for obj in remote_detected:
        if obj["name"] == "remote":
            return 1
        else:
            return 0


# im = PIL.Image.open("test_image_output.jpg")
# im.show()
