import cv2
import time
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import Canvas

multiplier = 6
Video = "Apple\Badapple1.mp4"

cap = cv2.VideoCapture(Video)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(frames)

# Define the quality
Size = (60, 60)

# Set up tkinter window and canvas
root = tk.Tk()
root.title("Bad Apple - Vinh")
canvas = Canvas(root, width=420, height=310, bg="black")
canvas.pack()

# Loop through the frames of the video
for Frame in range(0, frames, 2):
    cap.set(1, Frame)
    ret, frame = cap.read()
    im = Image.fromarray(frame)
    im = im.resize(Size)
    im_gray = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(im_gray, 300, 300)

    # Extract the positions of the edges, Modify the code so that the output frames are in the middle of the GUI
    positions = []
    for row in range(0, Size[1]):
        for pixel in range(0, Size[0]):
            if edges[row][pixel] == 255:
                # positions.append((pixel + 35, row - 45))
                positions.append((pixel + 25, row -30))
    

                

    coords = list(positions)

    # Clear the canvas for the next frame
    canvas.delete("all")

    start = time.time()
    for pos in coords:
        x = (pos[0] * multiplier) - 100
        y = -(pos[1] * multiplier) + 100
        canvas.create_oval(x, y, x + 4, y + 4, fill="green", outline="")
    
    end = time.time()

    # Calculate the sleep time more accurately
    sleep_time = max(0.035 - (end - start), 0)
    time.sleep(sleep_time)

    # Update the canvas
    canvas.update()

    # Print the progress
    print(f"--{int((Frame / frames) * 100)}--%")

root.mainloop()


