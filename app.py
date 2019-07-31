#!/usr/bin/ev python3
# 2019 Fridolin Pokorny

import time
import sys
import os
import tensorflow as tf
from pathlib import Path


def get_tf_build_info() -> None:
    """Get build information for installed TensorFlow."""
    path = os.path.dirname(os.path.dirname(tf.__file__))
    build_info = os.path.join(path, f'tensorflow-{tf.__version__}.dist-info', 'build_info.yaml')

    build_info_content = "!!!! AICoE TensorFlow not detected"
    if os.path.isfile(build_info):
        build_info_content = Path(build_info).read_text()

    print("================================================================================")
    print("===                                                                          ===")
    print("===                       TensorFlow Build Information                       ===")
    print("===                                                                          ===")
    print("================================================================================")
    print(build_info_content)


def main() -> None:
    """Get TensorFlow build information and loop forever."""
    get_tf_build_info()
    while True:
        hello = tf.constant('Hello, Thoth!')
        sess = tf.Session()
        print(sess.run(hello).decode())
        time.sleep(1.0)


if __name__ == "__main__":
    sys.exit(main())
