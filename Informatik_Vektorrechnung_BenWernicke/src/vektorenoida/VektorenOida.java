/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vektorenoida;

import Vector2D.Vector2D;
import Vector3D.Vector3D;

/**
 *
 * @author Ben
 */
public class VektorenOida {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //dieser Code wurde nicht getestet - benutzen auf eigene Gefahr
        Vector2D myVec2D = new Vector2D("Oida1", 2, 5);
        Vector3D myVec3D = new Vector3D("Oida1", 2, 5, 10);
        
        System.out.println("2D Vector: " + myVec2D.toString());
        System.out.println("3D Vector: " + myVec3D.toString());
        
        System.out.println("2D Vector addieren: " + myVec2D.add(new Vector2D("", 2, 5)).toString());
        System.out.println("2D Vector subtrahieren: " + myVec2D.sub(new Vector2D("", 2, 5)).toString());
        System.out.println("2D Vector multiplizieren mit Skalar: " + myVec2D.mult(3).toString());
        System.out.println("2D Vector Skalarprodukt: " + String.valueOf(myVec2D.scalarProdukt(new Vector2D("", 2, 5))));
        
        System.out.println("3D Vector addieren: " + myVec3D.add(new Vector3D("", 2, 5, 2)).toString());
        System.out.println("3D Vector subtrahiren: " + myVec3D.sub(new Vector3D("", 2, 5, 2)).toString());
        System.out.println("3D Vector multiplizieren mit Skalar: " + myVec3D.mult(3).toString());
        System.out.println("3D Vector Skalarprodukt: " + String.valueOf(myVec3D.scalarProdukt(new Vector3D("", 2, 5, 2))));
        System.out.println("3D Vector CrossProdukt: " + myVec3D.crossProduct(new Vector3D("", 2, 5, 2)).toString());
        
        System.out.println("2D Length: " + String.valueOf(myVec2D.Length()));
        myVec2D.Normalize();
        System.out.println("2D Normalize: " + myVec2D.toString());
        System.out.println("2D Length: " + String.valueOf(myVec2D.Length()));
        
        System.out.println("3D Length: " + String.valueOf(myVec3D.Length()));
        myVec3D.Normalize();
        System.out.println("3D Normalize: " + myVec3D.toString());
        System.out.println("3D Length: " + String.valueOf(myVec3D.Length()));
    }
    
}
