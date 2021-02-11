/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Mittelwert;

import java.lang.*;
import java.util.*;
public class Mittelwert {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double x, y=0;
        for(int i=0; i<=4; i++){
            System.out.println("Zahl: ");
            x = scan.nextDouble();
            y=y+x;
        }
        System.out.println("Mittelwert: "+(y/5));
    }
    } 
  

