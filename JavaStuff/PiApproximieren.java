import java.util.Scanner;
import java.lang.Math;

public class PiApproximieren {

    static public double Wurzel_Ding(double wurzel, int index)
    {
        if ( index == 0 )
        {
            return wurzel;
        }
        else
        {
            return Wurzel_Ding(Math.sqrt(2 + wurzel), index - 1);
        }
    }
    
    static public double PiViete(int iter)
    {
        double produkt = 1;
        for ( int i = 0; i < iter; i++ )
        {
            produkt *= 2.0 / Wurzel_Ding(Math.sqrt(2), i);
        }

        return 2 * produkt;
    }

    static public double PiWallis(int iter)
    {
        double produkt = 1;
        for (double i = 2; i < iter; i += 2)
        {
            produkt *= i / (i-1) * i / (i + 1);
        }
        return 2 * produkt;
    }

    static public double PiLeibnitz(int iter)
    {
        double summe = 0;
        int vor = -1;
        for (int i = 1; i < 2 * iter; i += 2)
        {
            vor *= -1.0;
            summe += vor * 4.0 / i; 
        }
        return summe;
    }

    static public double PiNilakantha(int iter)
    {
        double summe = 3;
        int vor = -1;
        for (int i = 4; i < 2 * (iter + 4); i += 2)
        {
            vor *= -1;
            summe += vor * ( 4.0 / ( (i - 2) * (i - 1) * i ) );
        }
        return summe;
    }


    static public void eval(int iter)
    {

        long uno, dos, tres, quattro, temp;
        double piUno, piDos, piTres, piQuattro;

        temp = System.nanoTime();
        piUno = PiViete(iter);
        uno = System.nanoTime() - temp;

        temp = System.nanoTime();
        piDos = PiWallis(iter);
        dos = System.nanoTime() - temp;

        temp = System.nanoTime();
        piTres = PiLeibnitz(iter);
        tres = System.nanoTime() - temp;

        temp = System.nanoTime();
        piQuattro = PiNilakantha(iter);
        quattro = System.nanoTime() - temp;

       System.out.println(Format_Output("Viete", piUno, uno));
       System.out.println(Format_Output("Wallis", piDos, dos));
       System.out.println(Format_Output("Leibniz", piTres, tres));
       System.out.println(Format_Output("Nilakantha", piQuattro, quattro));
    }
    static public String Format_Output(String name, double piSome, long time)
    {
        return name + ": " + String.valueOf(piSome) + " Time: " + String.valueOf(time) + " Nanosekunden\n";
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int iter;

        System.out.println("Wie viele Iterationen: ");
        iter = scan.nextInt();
        System.out.println("\nOutput:");
        scan.close();
        eval(iter);
    }
}