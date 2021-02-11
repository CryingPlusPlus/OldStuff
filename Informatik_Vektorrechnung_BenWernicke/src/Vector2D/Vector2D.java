/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vector2D;

import Vector.Vector;
import java.lang.Math;
/**
 *
 * @author Ben
 */
public class Vector2D extends Vector{
    
    public Vector2D(String name, double x, double y){
        this.coords = new double[2];
        this.name = name;
        this.setX(x);
        this.setY(y);
    }
    @Override
    public double Length() {
        return Math.sqrt((Math.pow(this.getX(), 2) + Math.pow(this.getY(), 2)));
    }

    @Override
    public void Normalize() {
        double fucktor = 1/this.Length();
        this.setX(fucktor * this.getX());
        this.setY(fucktor * this.getY());
    }

    @Override
    public String toString() {
        String end = new String();
        end += "(" + String.valueOf(this.coords[0]) + " " + String.valueOf(this.coords[1]) + ")";
        return end;
    }
    
    //Rechenoperationen
    
    public Vector2D add(Vector2D v){
        return new Vector2D("neuer Vector", this.getX() + v.getX(), this.getY() + v.getY());
    }
    
    public Vector2D sub(Vector2D v){
        return new Vector2D("neuer Vector", this.getX() - v.getX(), this.getY() - v.getY());
    }
    
    public Vector2D mult(double scal){
        return new Vector2D("neuer Vector", this.getX() * scal, this.getY() * scal);
    }
    
    public double scalarProdukt(Vector2D v){
        return this.getX() * v.getX() + this.getY() * v.getY();
    }
}
