import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

video_path = "/home/huawei/Documents/internship/Tasks/yolo_project/videos/cars.mp4"


class VideoPlayer(QWidget):
    def __init__(self, video_source=video_path, display_width=640, display_height=480):

        super().__init__()

        self.cap = None

        self.video_label = QLabel()
        self.inf_label= QLabel("Video Gösterimi")
        self.start_button = QPushButton("Başlat")
        self.stop_button = QPushButton("Durdur")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        layout = QVBoxLayout()
        layout.addWidget(self.inf_label)
        layout.addWidget(self.video_label)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.display_width = display_width

        self.start_button.clicked.connect(self.start_camera)
        self.stop_button.clicked.connect(self.stop_camera)

    def start_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(video_path)
            self.timer.start(30)


    def stop_camera(self):
        if self.cap is not None:
            self.timer.stop()
            self.cap.release()
            self.cap = None
            self.video_label.clear()

    def update_frame(self):
        self.cap is not None
        ret, frame = self.cap.read()
        if  ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            aspect_ratio = width / height
            new_width = self.display_width
            new_height = int(new_width / aspect_ratio)

            resized_frame = cv2.resize(frame, (new_width, new_height))
            bytes_per_line = channel * new_width

            qimg = QImage(resized_frame.data, new_width, new_height, bytes_per_line, QImage.Format_RGB888)
            qmap = QPixmap.fromImage(qimg)
            qimg = qmap.scaled(self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio)
            self.video_label.setPixmap(qimg)

    def closeEvent(self, event):
        self.stop_camera()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.resize(700, 600)
    player.setWindowTitle("PyQt5 Video Player")
    player.show()
    sys.exit(app.exec_())
#     cv2.polylines(annotated_frame, [region_pts], isClosed=True