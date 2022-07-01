# mr_usbcam

roslaunch mr_usbcam usbcam.launch

Arguments:
* display: (true/false) show the rgb image.
* camera: (default: /camera/rgb/image_raw) rename default topic name.
* usb_port: (default: /dev/ttyUSB0) select the correct usb port number.

roslaunch mr_usbcam usbcam.launch display:=false camera:=/webcam usb_port:=/dev/ttyUSB0
