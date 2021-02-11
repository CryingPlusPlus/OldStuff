package discountpreis;

import java.util.*;


public class discountpreis {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wie viel Geld bezahlen Bruder");
        double cent = scan.nextDouble();
        
        if(cent  > 1000){
            System.out.println("bezahlen sie müssen: "+ (cent*0.9));
        }else{
            System.out.println("bezahlen sie müssen: " + cent);
        }
        //-------------------------------------------
        System.out.println("Wie viel tank");
        double liter = scan.nextDouble();
        
        System.out.println("was verbrauch");
        double verbrauch = scan.nextDouble();
        
        double meilen = verbrauch * liter;
        if( meilen<200){
            System.out.println("tanken");
        }else{
            System.out.println("good to go");
        }
        //------------------------------------------------
        System.out.println("Geburtsjahr?");
        int jahr = scan.nextInt();
        System.out.println("Aktuelles Jahr?");
        int aJahr = scan.nextInt();
        
        if(aJahr <= 20 && aJahr >= 0){
            aJahr = aJahr + 2000;
        }else { 
            aJahr = aJahr + 1900;
        }
        if(jahr <= 20 && jahr >= 0){
            jahr = jahr + 2000;
        }else { 
            jahr = jahr + 1900;
        }
        System.out.println(aJahr+" "+jahr);
        int alter = + aJahr- jahr ;
        System.out.println("Alter: " + alter);
    }
    } 
  

