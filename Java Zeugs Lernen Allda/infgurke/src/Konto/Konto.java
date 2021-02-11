package Konto;

import java.util.*;

class personenkonto{
    private String name;
    private int nummer;
    private double kontostand;
    
    personenkonto(String name, int nummer, double kontostand){
        this.name = name;
        this.nummer = nummer;
        this.kontostand = kontostand;
    };

    personenkonto(personenkonto name, int nummer, double kontostand) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    void einzahlen(double betrag){
            kontostand = kontostand+betrag;
    }
    void abheben(double betrag){
        kontostand = kontostand-betrag;
    }
    double ausgeben(){
        return kontostand;
    }
}
public class Konto {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double kontostand;
        System.out.println("Wieviel Geld haben sie");
        kontostand = scan.nextDouble();
        
        personenkonto hans = new personenkonto("hans", 12, 1000);
        personenkonto felix = new personenkonto("felix", 12, 900);
        
        System.out.println("was wollen sie einzahlen");
        hans.einzahlen(scan.nextDouble());
        System.out.println("Sie haben: "+hans.ausgeben());
        
        System.out.println("was wollen sie abheben");
        hans.abheben(scan.nextDouble());
        System.out.println("Sie haben: "+hans.ausgeben());
        
        System.out.println("Sie haben: "+felix.ausgeben());
    }
    } 
  

