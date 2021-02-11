/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package schleifen;

import java.util.Scanner;

/**
 *
 * @author Ben
 */
public class wort {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Geben sie ein leckeres Wort ein nohomo");
        String wort = scan.nextLine();
        
        System.out.println("");
        for(int i = 0; i<wort.length(); i++){
            System.out.println(wort);
        }
        
        
    
    }
}
