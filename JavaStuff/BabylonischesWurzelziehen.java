import java.util.*;

public class BabylonischesWurzelziehen {
    
    static void print(String s) {
        System.out.println(s);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        print("Welche Zahl soll wurzeiliert werden?");
        double a = scan.nextDouble();
        print("Wie soll der Anfangswer sein?");
        double x = scan.nextDouble();
        print("Wie viele Iterationen?");
        int n = scan.nextInt();
        scan.close();

        for(int i = 0; i < n; i++){
            print(String.valueOf(i) + "\t\t" + String.valueOf(x));
            x = 1/2.0 * (x + a / x);
        }


    }
}