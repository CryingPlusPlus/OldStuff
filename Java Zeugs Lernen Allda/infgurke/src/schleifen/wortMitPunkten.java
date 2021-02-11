package schleifen;

import java.util.Scanner;

class frau{
    
    void schreien(){
        System.out.println("\nIch Staubsauge, in meiner Küche");
    }
    void kochen(){
        System.out.println("Ich koche in meiner Küche");
    }
}


public class wortMitPunkten {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String w1, w2;
        int l;
        
        frau frau = new frau();
        
        System.out.println("Wort  1");
        w1 = scan.nextLine();
        
        System.out.println("Wort  2");
        w2 = scan.nextLine();
        
        l = 30 - (w1.length() + w2.length());
        
        System.out.println("");
        
        System.out.print(w1);
        
        for(int i = 0; i<l; i++){
            System.out.print(".");
        }
        System.out.print(w2);
        
        frau.schreien();
        frau.kochen();
    }
}

