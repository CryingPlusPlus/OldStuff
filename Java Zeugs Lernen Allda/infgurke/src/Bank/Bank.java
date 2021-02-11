/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Bank;

import java.lang.*;
import java.util.*;

class erstellebank{
    int kontonummer=0,kontostand;
    public List<bankkonto> konto = new ArrayList<bankkonto>();
    String name;
    erstellebank(){}
    void erstellekonto(String name, int kontostand){
    kontonummer++;
    konto.add(new bankkonto(name, kontonummer, kontostand));
    }
    void ausgabe(int i){
        System.out.println(konto.get(i).ausgabename()+"\t"+konto.get(i).ausgabekontonummer()+"\t"+konto.get(i).ausgabekontostand());
    }
    int bankgroesse(){
        return konto.size();
    }
}

class bankkonto {
    int kontonummer, kontostand;
    String name;
    bankkonto(String name, int kontonummer, int kontostand){
        this.name = name;
        this.kontonummer = kontonummer;
        this.kontostand = kontostand;
    }
    int ausgabekontonummer(){
        return kontonummer;
    }
    String ausgabename(){
        return name;
    }
    int ausgabekontostand(){
        return kontostand;
    }
}



        public class Bank {
    public static void main(String[] args) { 
        erstellebank bankA = new erstellebank();
        
        bankA.erstellekonto("Hans", 10350000);
        bankA.erstellekonto("Marie", 2222);
        bankA.erstellekonto("Peter", 25155);
        bankA.erstellekonto("Heinz", 45238);
        bankA.erstellekonto("Ben", 245);
        bankA.erstellekonto("Cora", 100457000);
        bankA.erstellekonto("Niggi", 256);
        bankA.erstellekonto("Felix", 5454);
        bankA.erstellekonto("Jana", 589);
        bankA.erstellekonto("jan", 66);
        bankA.erstellekonto("Nick", 45);
        bankA.erstellekonto("Luke", 42069429);
        bankA.erstellekonto("Lena", 88888888);
        bankA.erstellekonto("Matthias", 420420);
        bankA.erstellekonto("Stefan", 42069);
        bankA.erstellekonto("Raul", 6969);
        bankA.erstellekonto("Marlene", 42096);
        bankA.erstellekonto("Kathi", 420);
        bankA.erstellekonto("Steffanie", 69);
        bankA.erstellekonto("Heinrich", 69420);
        bankA.erstellekonto("Ferdi", 100);
        
        
        for(int i=0; i<bankA.bankgroesse();i++){
            bankA.ausgabe(i);
        }
        
    }
    } 
  

