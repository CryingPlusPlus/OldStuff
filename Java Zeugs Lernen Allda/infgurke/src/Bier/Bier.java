package Bier;

import java.lang.*;
import java.util.*;
public class Bier {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int bierliter, fassliter;
        fassliter = 50;
        System.out.println("Liter: ");
        bierliter = scan.nextInt();
        
        if(bierliter%fassliter==0){
            System.out.println("Sie bekommen: " + (bierliter/fassliter)+" Fässer Bier");
        } else{
            System.out.println("Wir können die Menge so nicht Liefern wollen sie: "+(bierliter/fassliter)+" und: "+(bierliter%fassliter) + " zu wenig");
            System.out.println("Oder: " +((bierliter/fassliter)+1)+" und: "+(fassliter-(bierliter%fassliter))+" Zu viel");
        }
        
        
        
    }
    } 
  

