package Wechselstube;

import java.lang.*;
import java.util.*;
public class Wechselstube {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double euro,ecent,dcent,nur_dcent,dollar;

        
        System.out.println("Euro: ");
        euro = scan.nextDouble();
        ecent = euro*100;
        nur_dcent = ecent*1.11;
        dcent= nur_dcent%100;
        dollar = (nur_dcent-dcent)/100;
        System.out.println("Dollar: "+dollar+" Cent: "+dcent);
        
        
        
    }
    } 
  

