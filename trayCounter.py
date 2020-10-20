from pystray import Icon
from pystray import Menu as menu
from pystray import MenuItem as item
from PIL import Image, ImageDraw, ImageFont

trayicon = ''
counter = 0
counterStr = '00'


def on_inc(trayIcon):
    global counter
    counter += 1
    refeshTray()
    # print(counter)


def on_dec(trayIcon):
    global counter
    if counter > 0:
        counter -= 1
        refeshTray()
        # print(counter)


def on_reset(trayIcon):
    global counter
    counter = 0
    refeshTray()
    # print(counter)


def on_quit(trayIcon):
    trayIcon.stop()


def counterToStr():
    global counterStr
    if counter < 10:
        counterStr = '0' + str(counter)
    else:
        counterStr = str(counter)


def refeshTray():
    global trayIcon
    img = Image.new('RGB', (72, 72), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 60)
    counterToStr()
    d.text((4, 2), counterStr, font=fnt, fill=(0, 0, 0))
    trayIcon.icon = img
    trayIcon.title = str(counter)


if __name__ == "__main__":
    global trayIcon

    trayMenu = menu(
        item(
            'Inc',
            on_inc,
            default=True),
        item(
            'Dec',
            on_dec),
        item(
            'Reset',
            on_reset),
        menu.SEPARATOR,
        item(
            'Quit',
            on_quit,
        ))

    trayImage = Image.new('RGB', (72, 72), color=(255, 255, 255))
    trayIcon = Icon("tray counter", trayImage, str(counter), trayMenu)
    refeshTray()
    trayIcon.run()
