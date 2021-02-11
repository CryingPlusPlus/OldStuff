/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Scheckgebuehr;

import java.util.*;

/**
 *
 * @author Ben
 */
public class Scheckgebuehr {
    public static void main(String[] args) {
        Scanner scan =  new Scanner(System.in);
        double kontostand;
        double sparbuch;
        
        System.out.println("Sparbuch Bruder: ");
        sparbuch = scan.nextDouble();
        System.out.println("Konto Bruder: ");
        kontostand = scan.nextDouble();
        
        if(kontostand >= 1000 && sparbuch >= 1500){
            System.out.println("Jaaaa maaaaannn");
        }else{
            System.out.println("NAAAAAAAAA");
        }
        
    }
}
