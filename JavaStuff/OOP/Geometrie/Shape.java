package Geometrie;

import Geometrie.Point2d;

public abstract class Shape {
    private double area;
    private double umfang;
    private Point2d pivot;

    abstract public void calc_area();
    abstract public void calc_umfang();
}