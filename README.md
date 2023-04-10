# youtube-delete-videos
Delete Youtube videos in batches. Use  [pyautogui][pyautogui_link] to click through Youtube Studio page to delete videos in batches.

![Delete Youtube videos](youtube-delete-videos.gif)

# Prerequisite

1. [Python][python_link] is installed.
1. Install [pyautogui][pyautogui_link]: `pip install pyautogui`

# Run

1. In `youtube-delete-videos.py`, change `img_dirname` path to match the path in your computer.
1. Run: `python youtube-delete-videos.py`.
1. Ensure that **Youtube Studio > Content** page is on the **first** monitor. Otherwise, **pyautogui** can't see it.
1. If it doesn' work, retake the screenshots in `images` directory because you have different screen resolution them mine.

[pyautogui_link]: https://pyautogui.readthedocs.io/en/latest/
[python_link]: https://www.python.org/downloads/
