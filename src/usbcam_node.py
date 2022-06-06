#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


if __name__ == "__main__":
    rospy.init_node("usbcam")
    rospy.loginfo("usbcam node start!")

    # Get usb port name.
    usb_port = rospy.get_param("~usb_port")
    rospy.loginfo("connecting to %s..." % usb_port)

    # Get image topic name.
    camera = rospy.get_param("~camera")
    rospy.loginfo("rgb frame publish to topic %s" % camera)
    pub_camera = rospy.Publisher(camera, Image, queue_size=10)

    # Display image flag.
    display = rospy.get_param("~display")
    rospy.loginfo("display image %s" % display)

    # MAIN LOOP
    cap = cv2.VideoCapture(usb_port)
    while cap.isOpened():
        rospy.Rate(30).sleep()

        success, frame = cap.read()
        if not success: break

        pub_camera.publish(CvBridge().cv2_to_imgmsg(frame, "bgr8"))

        if display:
            cv2.imshow("mr_usbcam", frame)
            key_code = cv2.waitKey(1)
            if key_code in [27, ord('q')]:
                break
    cap.release()

    rospy.loginfo("usbcam node end!")
