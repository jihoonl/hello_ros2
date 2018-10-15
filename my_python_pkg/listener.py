#!/usr/bin/env python3

import rclpy
from std_msgs.msg import String


def callback(msg):
    print('%s' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('listener')
    subscription = node.create_subscription(String, 'topic', callback)
    subscription
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
