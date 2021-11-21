import cv2, os
from PIL import Image

print("Enter path to folder with images (.tif):")
inPath = input().replace('\\', '/')
if not inPath[-1] == '/':
    inPath += '/'
print("Enter path to output folder:")
outPath = input().replace('\\', '/')
if not outPath[-1] == '/':
    outPath += '/'
print("generating jpegs...")
for root, dirs, files in os.walk(inPath, topdown=False):
    for name in files:
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if not os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".png"):
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
                try:
                    im = Image.open(os.path.join(root, name))
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception as e:
                    print (e)
print("jpegs generated")

print("enter video name")
video_name = input()
if not video_name[-4:] == '.avi':
    video_name += '.avi'
print("generating video...")
images = [img for img in os.listdir(inPath) if img.endswith(".png")]
frame = cv2.imread(os.path.join(inPath, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(outPath + video_name, 0, 1, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(inPath, image)))
    os.remove(os.path.join(inPath, image))
video.release()
print("video ready")