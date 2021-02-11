/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MountainBikeTageBuch;

import java.time.*;
import java.util.*;

/**
 *
 * @author Ben und der Weidi
 */
class Strecke{
    String name;
    double distanz;
    double hoehenmeter;
    LocalTime dauer;
    LocalDateTime datum;

    Strecke(String name, double distanz, double hoehenmeter, LocalTime dauer, LocalDateTime datum){
        this.name = name;
        this.distanz = distanz;
        this.hoehenmeter = hoehenmeter;
        this.dauer = dauer;
        this.datum = datum;
    }
    public void getInfo(){
        System.out.println(this.name);
        System.out.println(this.distanz);
        System.out.println(this.hoehenmeter);
        System.out.println(this.dauer);
        System.out.println(this.datum);
    }
}

class AlleStrecken{
    List<Strecke> Strecken;
    double gesamtDistanz;
    double gesamtHoehenmeter;
    
    AlleStrecken() {
        this.Strecken = new ArrayList<Strecke>();
    }
    
    void newStrecke(String name, double distanz, double hoehenmeter, LocalTime dauer, LocalDateTime datum){
        Strecke neueStrecke = new Strecke(name, distanz, hoehenmeter, dauer, datum);
        Strecken.add(neueStrecke);
        
        this.setGesamt();
    }
    void setGesamt(){
        this.gesamtHoehenmeter = 0;
        this.gesamtDistanz = 0;
        
        for(int i = 0; i < this.Strecken.size(); i++){
            this.gesamtDistanz += Strecken.get(i).distanz;
            this.gesamtHoehenmeter += Strecken.get(i).hoehenmeter;
        }
    }
    
    void getInfo(){
        for(int i = 0; i < this.Strecken.size(); i++){
            Strecken.get(i).getInfo();
        }
    }
    
    void output(){
        System.out.println("Gesamte Distanz: ");
        System.out.println(this.gesamtDistanz);
        System.out.println("Gesamte Höhenmeter: ");
        System.out.println(this.gesamtHoehenmeter);
    }
}



class Fahrer{
    int alter;
    String name;
    String bike;
    AlleStrecken Strecken;
    
    Fahrer(int alter, String name, String bike){
        this.alter = alter;
        this.name = name;
        this.bike = bike;
    }
    
    void setNewBike(String bike){
        this.bike = bike;
    }
    
    void birthday(){
        this.alter++;
    }
    public void getInfo(){
        this.Strecken.getInfo();
    }
    
    void Gefahren(String name, double distanz, double hoehenmeter, LocalTime dauer, LocalDateTime datum){
        Strecken.newStrecke(name, distanz, hoehenmeter, dauer, datum);
    }
    
    void output(){
        Strecken.output();
    }
}

public class MountainBikeTageBuch {
    public static void main(String[] args) {
    
    }
}

