/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vererbungen;

import java.lang.*;
import java.util.*;

class artikel{
    // Variablen
    final double HANDELSSPANNE = 0.6;
    final double MWST = 0.19;
    int artikelnummer;
    String bezeichnung;
    double einkaufspreis, lagerzeit;
    
    // Konstruktor
    artikel(int artikelnummer, String bezeichnung, double einkaufspreis, double lagerzeit){
        this.artikelnummer = artikelnummer;
        this.bezeichnung = bezeichnung;
        this.einkaufspreis = einkaufspreis;
        this.lagerzeit = lagerzeit;
    }
    
    // Methoden
    
    public void anzeigen(){
        System.out.println(artikelnummer +" "+ bezeichnung +" " +einkaufspreis +" "+ lagerzeit);
    }
    double berechneVerkaufspreis(){
        return einkaufspreis + HANDELSSPANNE*einkaufspreis+MWST*einkaufspreis; 
    }
}
class sonderposten extends artikel{
    //Variablen
    double rabatt;
    
    //Konstruktor
    public sonderposten(int artikelnummer, String bezeichnung, double einkaufspreis, double lagerzeit, double rabatt) {
        super(artikelnummer, bezeichnung, einkaufspreis, lagerzeit);
        this.rabatt = rabatt;
    }
    
    public void anzeigen(){
        super.anzeigen();
        System.out.println(rabatt);
    }
    double berechneVerkaufspreis(){
        return super.berechneVerkaufspreis() * (1-rabatt);
    }
}

public class Vererbungen {
    public static void main(String[] args) {
        artikel a = new artikel(123, "Apfel", 12.3, 2.5);
        artikel b = new artikel(14, "Birnen", 14.0, 5.8);
        sonderposten c = new sonderposten(14, "Birnen", 14.0, 5.8, 0.5);
        
        a.anzeigen();
        b.anzeigen();
        c.anzeigen();
        System.out.println(a.berechneVerkaufspreis() + " "+b.berechneVerkaufspreis()+" "+c.berechneVerkaufspreis());
    }
    } 
  

