from setuptools import setup, find_packages

setup(
    name="RemoveCamBackground",
    version="0.1",
    packages=find_packages(),
    scripts=["remove_cam_bg/removeCamBg.py"],
    author="Maximilian Matthe",
    description="Mask out a face detected from webcam video stream and replace the rest with a background image.",
    keywords="webcam replace v4l2loopback fake background mask video opencv",
    url="https://github.com/mmatthe/webcamremovebg",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        "opencv-python==4.2.0.34",
        "pyfakewebcam==0.1.0"
    ],
    include_package_data=True,
    package_data={"": ["*.xml"]}
)