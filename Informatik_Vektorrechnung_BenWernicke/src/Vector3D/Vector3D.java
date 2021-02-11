/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vector3D;

import Vector.Vector;

/**
 *
 * @author Ben
 */
public class Vector3D extends Vector{
    
    double getZ(){
        return this.coords[2];
    }
    
    void setZ(double z){
        this.coords[2] = z;
    }
    
    public Vector3D(String name, double x, double y, double z){
        this.coords = new double[3];
        this.name = name;
        this.setX(x);
        this.setY(y);
        this.setZ(z);
    }
    
    @Override
    public double Length() {
        return Math.sqrt((Math.pow(this.getX(), 2) + Math.pow(this.getY(), 2) + Math.pow(this.getZ(), 2)));
    }

    @Override
    public void Normalize() {
        double fucktor = 1/this.Length();
        this.setX(fucktor * this.getX());
        this.setY(fucktor * this.getY());
        this.setZ(fucktor * this.getZ());
    }

    @Override
    public String toString() {
        String end = new String();
        end += "(" + String.valueOf(this.coords[0]) + " " + String.valueOf(this.coords[1]) + " " + String.valueOf(this.getZ()) + ")";
        return end;
    }
    
    //Rechenoperationen
    
    public Vector3D add(Vector3D v){
        return new Vector3D("neuer Vector", this.getX() + v.getX(), this.getY() + v.getY(), this.getZ() + v.getZ());
    }
    
    public Vector3D sub(Vector3D v){
        return new Vector3D("neuer Vector", this.getX() - v.getX(), this.getY() - v.getY(), this.getZ() - v.getZ());
    }
    
    public Vector3D mult(double scal){
        return new Vector3D("neuer Vector", this.getX() * scal, this.getY() * scal, this.getZ() * scal);
    }
    
    public double scalarProdukt(Vector3D v){
        return this.getX() * v.getX() + this.getY() * v.getY() + this.getZ() * v.getZ();
    }
    
    public Vector3D crossProduct(Vector3D v){
        return new Vector3D(
                "neuer Vector",
                this.getY() * v.getZ() - this.getZ() * v.getY(),
                -this.getX() * v.getZ() + this.getZ() * v.getX(),
                this.getX() * v.getY() - this.getY() * v.getX()
        );
    }
    
}
