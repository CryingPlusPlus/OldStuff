package ratespiel;

import java.util.Random;
import java.util.Scanner;

public class ratespiel {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        int zahl, guess, i = 0, max, ver = 0;
        //-------------------------------------
        System.out.println("Welches Zahlenmax wollen sie haben");
        max = scan.nextInt() + 1;
        zahl = rand.nextInt(max);
        do{
            ver++;
            System.out.println("Raten sie die Zahl: ");
            guess = scan.nextInt();
            i++;
            if(guess < zahl){
                System.out.println("Zu Niedrig");
            }else if(guess > zahl){
                System.out.println("Zu hoch");
            }
        }while(guess != zahl);
        
        
        if(guess == zahl){
            System.out.println("Sie haben gewonnen; Sie haben " + ver + " Versuche gebraucht");
        }else{
            System.out.println("Sie haben verloren");
        }
        
    }
}
