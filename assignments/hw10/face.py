from graphics import *


class Face:
    def __init__(self, window, center, size):
        self.center = center
        self.eye_size = 0.15 * size
        self.eye_off = size / 3.0
        self.mouth_size = 0.8 * size
        self.mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, self.eye_size)
        self.left_eye.move(-self.eye_off, -self.eye_off)
        self.right_eye = Circle(center, self.eye_size)
        self.right_eye.move(self.eye_off, -self.eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        self.point_1 = center.clone()
        self.point_1.move(-self.mouth_size / 2, self.mouth_off)
        self.point_2 = center.clone()
        self.point_2.move(self.mouth_size / 2, self.mouth_off)
        self.mouth = Line(self.point_1, self.point_2)
        self.mouth.draw(window)

    def smile(self):
        point_3 = self.center.clone
        point_3.move(self.mouth_size, self.mouth_off + 50)
        self.mouth = Polygon(self.point_1, self.point_2, point_3)

    def shock(self):
        self.mouth = Circle(self.center, self.mouth_size)
        self.mouth.move(self.center, self.mouth_off)

    def wink(self):
        eye_point_one = self.center.clone
        eye_point_two = self.center.clone
        eye_point_one.move(-self.eye_size, -self.eye_off)
        eye_point_two.move(-self.eye_size / 2, -self.eye_off)
        self.right_eye = Line(eye_point_one, eye_point_two)

        point_3 = self.center.clone
        point_3.move(self.mouth_size, self.mouth_off + 50)
        self.mouth = Polygon(self.point_1, self.point_2, point_3)
