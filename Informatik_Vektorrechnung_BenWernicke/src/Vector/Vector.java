/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vector;

/**
 *
 * @author Ben
 */
public abstract class Vector {
    protected String name;
    protected double[] coords;
    
    public double getX(){
        return this.coords[0];
    }
    public double getY(){
        return this.coords[1];
    }
    
    public void setX(double x){
        this.coords[0] = x;
    }
    public void setY(double y){
        this.coords[1] = y;
    }
    
    public abstract double Length();
    public abstract void Normalize();
    public abstract String toString();
}
