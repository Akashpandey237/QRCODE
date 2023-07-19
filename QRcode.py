import qrcode

img = qrcode.make("https://github.com/Akashpandey237?tab=repositories")
img.save("git.jpg")
