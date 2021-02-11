package reverseString;

import java.lang.*;
import java.util.*;

public class reverseString {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String name = new String("Frauengasse");
        String reverse = new String();
        for (int i = name.length() - 1; i >= 0; i--) {
            reverse = reverse + name.charAt(i);
        }
        System.out.println("Reversed string is:");
        System.out.println(reverse);
    }
}


 
