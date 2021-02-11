/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Rechteck;

import java.lang.*;
import java.util.*;
public class Rechteck {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double l, b;
        
        System.out.println("Länge: ");
        l = scan.nextDouble();
       
        System.out.println("Breite: ");
        b = scan.nextDouble();
        System.out.println("Umfang: "+(l+l+b+b)+" Fläche: "+(l*b));
    }
    } 
  

