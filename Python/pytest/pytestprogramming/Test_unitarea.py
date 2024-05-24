import area

class Testarea:
    def test_circle_area(self):
        assert area.circle(0)==0
        assert area.circle(1)==3.14

    def test_square_area(self):
        assert area.square(2)==4
        assert area.square(4)==16

    def test_rectangle_area(self):
        assert area.rectangle(2,3)==6
        assert area.rectangle(5,6)==30

    def test_parllelogaram_area(self):
        assert area.parllelogram(3,6)==18

    def test_triangle_area(self):
        assert area.triangle(12,5)==30
        assert area.triangle(20,5)==50