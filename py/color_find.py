import pyautogui as agui

find_color = (255, 255, 255)

def main():
    screen = agui.screenshot()
    screen_width = screen.width
    screen_height = screen.height

    for x in range(screen_width):
        for y in range(screen_height):
            if screen.getpixel((x, y)) == find_color:
                print(f"Color found at screen position {x}, {y}")

if __name__ == "__main__":
    main()