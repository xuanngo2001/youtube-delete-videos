# youtube-delete-videos
Delete Youtube videos in batch. Use  [pyautogui][pyautogui_link] to click through Youtub studio to delete videos in batches.

![Delete Youtube videos](youtube-delete-videos.gif)

# Prerequisite

1. Python is installed.
1. Install `pyautogui`: `pip install pyautogui`

# Run

1. In `youtube-delete-videos.py`, change `img_dirname` path to match the path in your computer.
1. Run: `python youtube-delete-videos.py`.
1. Ensure that **Youtube Studio > Content** page is on the **first** monitor. Otherwise, **pyautogui** can't see it.
1. If it doesn' work, retake the screenshots in `images` directory because you have different screen resolution them mine.

[pyautogui_link]: https://pyautogui.readthedocs.io/en/latest/
