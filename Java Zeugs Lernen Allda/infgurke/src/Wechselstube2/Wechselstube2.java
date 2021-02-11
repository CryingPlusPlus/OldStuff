package Wechselstube2;

import java.lang.*;
import java.util.*;
public class Wechselstube2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double euro,ecent,dcent,nur_dcent,dollar;

        
        System.out.println("Euro: ");
        euro = scan.nextDouble();
        System.out.println("Cent: ");
        ecent = scan.nextDouble();
        
        ecent = euro*100+ecent;
        nur_dcent = ecent*1.11;
        dcent= nur_dcent%100;
        dollar = (nur_dcent-dcent)/100;
        System.out.println("Dollar: "+dollar+" Cent: "+dcent);
        
        
        
    }
    } 
  

