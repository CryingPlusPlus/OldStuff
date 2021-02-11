/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package schleifen;

import java.util.Scanner;

class weib{
    
    void schreien(){
        System.out.println("\nIch Staubsauge, in meiner Küche");
    }
    void kochen(){
        System.out.println("Ich koche in meiner Küche");
    }
    void putzen(){
        System.out.println("Putze Putze ich Putze");
    }
}

public class schleifen {
    public static void main(String[] args) {
        weib frau = new weib();
        Scanner scan = new Scanner(System.in);
        int start, ende;
        do{
            System.out.println("Hello geben sie mir nummer Start");
            start = scan.nextInt();
        
            System.out.println("Hello geben sie mir nummer Ende");
            ende = scan.nextInt();
        
            if(start >= ende){
                System.out.println("Alarm! Alarm! Alarm!");
            }
        
        }while(start >= ende);
        System.out.println("");
        
        
        if(start < ende){
            for(int i = start; i <= ende; i++){
                System.out.println(i);
            }
        }
        
        
        frau.schreien();
        frau.kochen();
    
    }
}

