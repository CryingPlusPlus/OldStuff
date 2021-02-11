package tiere;

import java.util.Scanner;

class tier{
    String color = new String();
    double masse;
    tier(String color, double masse){
        this.color = color;
        this.masse = masse;
    }
    
    void laut(){
    }
    void laufen(){
        System.out.println("Ich bin gelaufen");
    }
    void daten(){
        System.out.println("Meine daten sind: " + color + " " + masse);
    }
}
//--------------------------------------------------------------------------
class hund extends tier{
    
    String laut = new String();
    public hund(String color, double masse) {
        super(color, masse);
        laut = "Wuff";
    }
        
    void laut(){
        super.laut();
        System.out.println(laut);
    }
    void daten(){
        System.out.println("Ich bin Hund");
        super.daten();
    }
}
//--------------------------------------------------------------------------
class katze extends tier{
    
    String laut = new String();
    public katze(String color, double masse) {
        super(color, masse);
        laut = "Miau";
    }
        
    void laut(){
        super.laut();
        System.out.println(laut);
    }
    void daten(){
        System.out.println("Ich bin Katze");
        super.daten();
    }
}
//---------------------------------------------------------------------------
class fisch extends tier{
    
    String laut = new String();
    public fisch(String color, double masse) {
        super(color, masse);
        laut = "Blub";
    }
        
    void laut(){
        super.laut();
        System.out.println(laut);
    }
    void daten(){
        System.out.println("Ich bin Fisch");
        super.daten();
    }
}
//-----------------------------------------------------------------------

public class haustiere {
    public static void main(String[] args) {
        katze katze = new katze("schwarz", 15);
        hund hund = new hund("gold", 50);
        fisch fisch = new fisch("rot", 0.15);
        
        katze.daten();
        hund.daten();
        fisch.daten();
    }
}
