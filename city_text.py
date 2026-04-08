from manim import *

def st_denis_en_val(char_space=.35*RIGHT, line_space=.6*DOWN):
    text = [['S', '^t', ' ', 'D', 'E', 'N', 'I', 'S'], ['_-', '_e', '_n', '_-', 'V', 'A', 'L']]
    out = []
    box_width = 0
    for e, line in enumerate(text):
        count = 0
        out.append([])
        previous = 1
        for char in line:
            font_size=40
            if char[0] == '^':
                font_size=25
                count += .7
                previous = .7
            elif char[0] == '_':
                font_size=25
                count += .5
                previous = .7
            elif char[0] == ' ':
                count += .7
                previous = .7
            else:
                count += min(1, previous)
                previous = 1
            position = count*char_space

            if char[0] == '^':
                position += .083*UP
            elif char[0] == '_':
                position += .083*DOWN
                
            out[-1].append(Text(
                char[-1],
                font_size=font_size,
                font="Caracteres L2",
                color=BLACK
            ).shift(position))

        box_width = max(box_width, count*.35)
        out[-1] = VGroup(out[-1]).move_to(ORIGIN).shift(e*line_space)
    
    box_height = len(out)*.6
    
    box = RoundedRectangle(
        width=box_width+.3,
        height=box_height+.3,
        corner_radius=0.05,
        stroke_color="#E72130",
        stroke_width=10,
        fill_color=WHITE,
        fill_opacity=1
    )

    return [box, VGroup(*out).move_to(ORIGIN)]
            
            
    


    line1 = VGroup([
    Text(
        'S',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ),
    Text(
        'T',
        font_size=20,
        font="Caracteres L2",
        color=BLACK
    ).shift(1*space/2+UP*.1),
    Text(
        'D',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(1.5*space),
    Text(
        'E',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(4*space),
    Text(
        'N',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(5*space),
    Text(
        'I',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(6*space),
    Text(
        'S',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(7*space),
    ])

    line2 = VGroup([
    Text(
        '-',
        font_size=20,
        font="Caracteres L2",
        color=BLACK
    ).shift(DOWN*.1),
    Text(
        'E',
        font_size=20,
        font="Caracteres L2",
        color=BLACK
    ).shift(1*space/2+DOWN*.1),
    Text(
        'N',
        font_size=20,
        font="Caracteres L2",
        color=BLACK
    ).shift(2*space/2+DOWN*.1),
    Text(
        '-',
        font_size=20,
        font="Caracteres L2",
        color=BLACK
    ).shift(3*space/2+DOWN*.1),
    Text(
        ' ',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(4*space),
    Text(
        'V',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(5*space),
    Text(
        'A',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(6*space),
    Text(
        'L',
        font_size=40,
        font="Caracteres L2",
        color=BLACK
    ).shift(7*space),
    ])



    return [line1.move_to(ORIGIN), line2.move_to(ORIGIN).shift(line)]


def city_label(text, position, width=.3, height=0.8):
    # Rectangle arrondi rouge
    box = RoundedRectangle(
        width=width*len(text),
        height=height,
        corner_radius=0.05,
        stroke_color="#E72130",
        stroke_width=10,
        fill_color=WHITE,
        fill_opacity=1
    )
    
    # Texte
    label = Text(
        text,
        font_size=28,
        font="Caracteres L2",
        color=BLACK
    )

    label.move_to(box.get_center())

    return VGroup(box, label).move_to(position)








        # city_positions = {
        #     "Orléans": (0, 0),
        #     "St-Jean-le-Blanc": (2, 1),
        #     "St-Denis-en-Val": (4, 3),
        #     "CHU": (6, 1),
        #     "Sandillon": (6, 6),
        #     "Saint-Cyr-en-Val": (8, 5),
        #     "Ardon": (9, 0),
        # }

        # for city, (i, j) in city_positions.items():
        #     x, y, _ = cell_corner(i, j)

        #     label = city_label(
        #         city,
        #         [x + cell_size/2, y - cell_size/2, 0]
        #     )

        #     self.add(label)


