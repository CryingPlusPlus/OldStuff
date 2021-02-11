/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package infgurke;

import java.lang.*;
import java.util.*;
public class Infgurke {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        double n = 54;
        double schaetzung = 1.0;
        
        if(n>=0){
            while(Math.abs(n/(schaetzung*schaetzung)-1)>10E-14){
                schaetzung =  n/(2*schaetzung) + schaetzung/2;
            }
        } else {
            System.out.println("nope");
        
        }
        System.out.print(schaetzung);
    }
    } 
  

