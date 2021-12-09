# need pyusb and python binding for opencv
# also need libusb installed
import cv2
import usb.core
cam=cv2.VideoCapture(0)

dev = usb.core.find(idVendor=0x18e3, idProduct=0x5031)
reattach = False
if dev.is_kernel_driver_active(0):
    reattach = True
    dev.detach_kernel_driver(0)

# simulate the SET_CUR sequence
dev.ctrl_transfer(0x21,0x01,0x0800,0x0600,[0x50,0xff])
dev.ctrl_transfer(0x21,0x01,0x0f00,0x0600,[0x00,0xf6])
dev.ctrl_transfer(0x21,0x01,0x0800,0x0600,[0x25,0x00])
dev.ctrl_transfer(0x21,0x01,0x0800,0x0600,[0x5f,0xfe])
dev.ctrl_transfer(0x21,0x01,0x0f00,0x0600,[0x00,0x03])
dev.ctrl_transfer(0x21,0x01,0x0f00,0x0600,[0x00,0x02])
dev.ctrl_transfer(0x21,0x01,0x0f00,0x0600,[0x00,0x12])
dev.ctrl_transfer(0x21,0x01,0x0f00,0x0600,[0x00,0x04])
dev.ctrl_transfer(0x21,0x01,0x0800,0x0600,[0x76,0xc3])

while(True):
    ret,frame=cam.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(100) & 0xff==ord('q'):
        break    

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()

# This is needed to release interface, otherwise attach_kernel_driver fails
# due to "Resource busy"
usb.util.dispose_resources(dev)

# # It may raise USBError if there's e.g. no kernel driver loaded at all
# if reattach:
#     dev.attach_kernel_driver(0)
