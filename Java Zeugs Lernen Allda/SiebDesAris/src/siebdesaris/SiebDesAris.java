/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package siebdesaris;

/**
 *
 * @author Ben
 */
public class SiebDesAris {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n=1000000;
        int ausgeben = 1;
        int pz = 1;
        
        int a_laenge = n+1;
        int[] a = new int[a_laenge];
        int[] p = new int[a_laenge];
        
        //array a füllen
        for(int i=1; i<a_laenge; i++){
            a[i]=i;
        }
        //array durchlaufen und alles durch elementarprimzahlen ersetzen
        for(int pt=2; pt<a_laenge; pt++){
            for(int i=0; i<a_laenge; i=i+pt){
                if(a[i]%pt==0){
                    a[i]=pt;
                }
            }
        }
        for(int i=0; i<a_laenge; i++){
            if(a[i]==i){
                p[pz]=i;
                pz=pz+1;
            }
        }
        
        
        if(ausgeben == 0){
            for(int i=1; i<pz; i++){
                System.out.print(p[i]+", ");
            }
        }
    System.out.println("done");
    }
    
}
