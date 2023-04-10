# Description: Delete videos in batches.
#   pyautogui only check on the 1st monitor.
#   pip install pyautogui
#   From Youtube Studio > Content page, set it to show 50 videos per page.
# pip install Pillow --upgrade

import pyautogui
import time

img_dirname = "C:\\xuan\\vbox-shared\\github-projects\\youtube-delete-videos\\images\\"

def main():
    while True:
        # Select all videos
        (x, y) = wait_for_image(img_dirname+"video-checkbox.png")
        print(x, y)
        x2 = x - 30
        y2 = y

        pyautogui.moveTo(x2, y2)
        pyautogui.click()

        # Clicks to delete videos.
        find_image_n_click(img_dirname+"more-actions.png")
        find_image_n_click(img_dirname+"delete-forever.png")
        find_image_n_click(img_dirname+"i-understand.png")
        find_image_n_click(img_dirname+"delete-forever-button.png")




# ====================== HELPER functions ===================
WAIT_TIME_SEC = 1
def wait_for_image(image_name):
    image_position = None
    while image_position is None:
        time.sleep(WAIT_TIME_SEC)
        localTime = time.ctime(time.time())
        print(f"   {localTime}: Waiting for {image_name}")
        image_position = pyautogui.locateCenterOnScreen(image_name, grayscale=True)
    if image_position is not None:
        return image_position

def find_image_n_click(image_name):
    wait_for_image(image_name)
    image_position = pyautogui.locateCenterOnScreen(image_name)
    if image_position is None:
        print("   Error: {0} not found!".format(image_name))
    else:
        pyautogui.moveTo(image_position)
        pyautogui.click()
        time.sleep(WAIT_TIME_SEC)
    
if __name__ == '__main__':
    main()

