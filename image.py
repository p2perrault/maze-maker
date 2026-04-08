from manim import *
from city_text import *
import os, sys
import numpy as np

def one_hot_encode(matrix, num_classes=4):
    matrix = np.array(matrix)
    h, w = matrix.shape
    one_hot = np.zeros((h, w, num_classes), dtype=int)
    
    for i in range(h):
        for j in range(w):
            val = matrix[i, j]
            if val < num_classes:
                one_hot[i, j, val] = 1
    return one_hot

def maze1():
    layer0 = one_hot_encode([
        [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [4,0,4,0,0,4,4,0,0,0,0,4,4,0,0,0,0,0,4,4],
        [4,4,4,4,4,0,0,4,0,0,0,4,4,4,0,0,0,0,0,4],
        [4,4,0,0,0,4,4,4,4,4,4,0,0,4,0,0,4,4,4,4],
        [4,4,4,0,4,0,0,0,0,0,0,0,4,0,4,0,0,4,4,4],
        [4,4,0,4,4,4,4,4,4,0,0,0,0,0,0,4,0,0,4,4],
        [0,4,0,4,0,0,4,4,4,4,4,4,4,4,4,4,4,0,0,4],
        [4,4,4,4,4,0,0,4,4,0,0,0,0,0,0,4,0,0,4,4],
        [4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,4,4,0,0,4],
        [0,4,0,4,4,4,4,0,0,0,4,4,0,0,0,0,0,0,0,0],
        [4,4,4,0,0,0,0,0,0,4,4,0,0,0,0,0,4,0,0,0],
        [4,0,0,4,4,4,0,4,0,4,0,0,4,4,0,0,0,4,0,4],
        [4,4,4,4,4,4,0,0,0,4,4,4,4,0,0,0,4,0,0,4],
        [4,4,4,4,4,4,0,0,4,4,4,4,0,0,4,4,4,4,4,4],
        [4,0,0,4,0,0,0,0,4,4,0,0,0,0,4,0,0,0,4,4],
        [0,0,4,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4],
        [4,0,0,4,0,0,4,4,4,4,0,0,0,0,0,0,0,4,0,4],
        [4,4,4,4,0,0,0,4,4,4,0,4,0,0,0,0,0,0,0,0],
        [4,4,4,0,0,0,0,4,4,0,4,4,0,4,4,4,4,4,4,4],
    ])
    layer1 = one_hot_encode([
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4],
    ])
    layer2 = one_hot_encode([
        [1,1,4,4,4,4,1,4,4,4,4,4,1,4,4,4,4,4,4,3],
        [1,4,4,4,4,1,4,1,4,4,4,1,1,1,4,4,4,4,3,3],
        [1,4,4,4,4,4,4,4,4,4,4,1,4,1,4,4,4,1,1,3],
        [1,1,1,4,4,4,4,4,4,4,4,3,4,3,4,4,3,3,3,3],
        [1,1,1,4,1,1,1,1,4,4,4,4,3,4,4,4,4,3,3,3],
        [1,1,4,4,1,4,1,1,1,1,4,4,4,4,4,4,1,4,3,3],
        [1,4,4,1,1,4,4,1,1,1,4,4,4,4,4,4,1,4,3,3],
        [1,4,4,1,1,1,1,1,1,4,4,4,4,4,4,1,1,3,3,3],
        [1,4,4,1,1,1,1,1,4,4,4,1,4,4,4,4,1,4,4,3],
        [1,1,1,4,4,4,1,4,4,4,1,1,4,4,4,4,4,4,4,3],
        [1,4,1,4,1,1,4,4,4,1,1,4,4,1,4,4,4,1,4,3],
        [1,1,4,4,1,1,1,4,1,4,1,4,1,1,4,4,4,1,3,3],
        [1,1,4,4,1,1,1,4,4,1,1,1,1,4,4,1,4,4,3,3],
        [1,1,4,4,1,4,4,4,4,1,1,1,4,4,4,1,4,4,3,3],
        [1,4,4,1,4,4,4,4,1,1,1,4,4,4,4,4,4,3,3,3],
        [1,4,1,1,4,4,4,4,1,4,1,4,4,4,4,4,4,3,3,3],
        [1,1,4,1,4,4,4,1,4,1,1,4,4,4,4,4,4,3,3,3],
        [1,4,4,1,1,4,4,1,1,1,4,4,4,4,4,4,4,4,4,3],
        [1,4,4,1,4,4,4,4,1,1,1,1,1,4,4,4,4,4,4,4],
        [1,4,4,4,4,4,4,4,1,4,4,1,4,4,4,4,4,4,4,4],
    ])
    return layer0 + layer1 + layer2

class MazeScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rows, cols = 20, 20
        cell_size = 0.6
        wall_width = 6
        overlap = -0.012

        matrix = maze1()

        maze_group = VGroup()

        def cell_corner(i, j):
            return np.array([
                j * cell_size,
                -i * cell_size,
                0
            ])

        for i in range(rows):
            for j in range(cols):
                x, y, _ = cell_corner(i, j)

                top, left, bottom, right = matrix[i][j]

                # TOP wall
                if top:
                    p1 = np.array([x - overlap, y, 0])
                    p2 = np.array([x + cell_size + overlap, y, 0])
                    maze_group.add(Line(
                        p1, p2,
                        stroke_width=wall_width,
                        color=BLACK,
                        joint_type=LineJointType.ROUND,
                        cap_style=CapStyleType.ROUND
                    ))

                # BOTTOM wall
                if bottom:
                    p1 = np.array([x - overlap, y - cell_size, 0])
                    p2 = np.array([x + cell_size + overlap, y - cell_size, 0])
                    maze_group.add(Line(
                        p1, p2,
                        stroke_width=wall_width,
                        color=BLACK,
                        joint_type=LineJointType.ROUND,
                        cap_style=CapStyleType.ROUND
                    ))

                # LEFT wall
                if left:
                    p1 = np.array([x, y + overlap, 0])
                    p2 = np.array([x, y - cell_size - overlap, 0])
                    maze_group.add(Line(
                        p1, p2,
                        stroke_width=wall_width,
                        color=BLACK,
                        joint_type=LineJointType.ROUND,
                        cap_style=CapStyleType.ROUND
                    ))

                # RIGHT wall
                if right:
                    p1 = np.array([x + cell_size, y + overlap, 0])
                    p2 = np.array([x + cell_size, y - cell_size - overlap, 0])
                    maze_group.add(Line(
                        p1, p2,
                        stroke_width=wall_width,
                        color=BLACK,
                        joint_type=LineJointType.ROUND,
                        cap_style=CapStyleType.ROUND
                    ))

        maze_group.move_to(ORIGIN)
        self.add(maze_group)

        start_x, start_y = -10 * cell_size, 10 * cell_size
        end_x, end_y = 2 * cell_size, -9 * cell_size
        start_center = np.array([start_x + cell_size / 2, start_y - cell_size / 2, 0])
        end_center = np.array([end_x + cell_size / 2, end_y - cell_size / 2, 0])
        start_arrow = Arrow(
            start=start_center + UP*0.24,
            end=start_center + DOWN*0.24,
            color=GREEN,
            max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=.4,
        )
        end_arrow = Arrow(
            start=end_center + LEFT*0.24,
            end=end_center + RIGHT*0.24,
            color=RED,
            max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=.4,
        )
        self.add(start_arrow)
        self.add(end_arrow)
        self.add(*st_denis_en_val())

if __name__ == "__main__":
    os.system(f'{os.path.dirname(sys.executable)}/python -m manim -p -r 1024,1024 image.py -o {os.getcwd()}/image.png')
    os.system(f'rm -r {os.getcwd()}/media')