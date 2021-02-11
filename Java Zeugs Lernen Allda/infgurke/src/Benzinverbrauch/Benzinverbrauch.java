
package Benzinverbrauch;

import java.lang.*;
import java.util.*;
public class Benzinverbrauch {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double kilometer, liter, verbrauch, strecke;
        
        System.out.println("Gefahrene Kilometer");
        kilometer = scan.nextDouble();
        System.out.println("Verbrauchte Liter");
        liter = scan.nextDouble();
        
        verbrauch = liter/kilometer*100;
        strecke = kilometer/liter;
        
        System.out.println("verbrauch: "+verbrauch+" Strecke/liter: "+strecke);
        
    }
    } 
  

