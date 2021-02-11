package TortenEssen;

import java.util.Scanner;


public class TortenEssen {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double m;
        
        System.out.println("Gewicht?");
        m = scan.nextDouble();
        
        if(m >= 235 && m <= 265){
            System.out.println("JAAAAS");
        }else{
            System.out.println("NAAAAAA");
        }
    }
    
}
