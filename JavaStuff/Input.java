import java.util.Scanner;

public class Input 
{

static void print(String msg) 
{
    System.out.println(msg);
}

    public static void main(String[] args) 
    {
    Scanner scan = new Scanner(System.in);
    int zahl;
    do 
    {
        print("Bitte eine Zahl zwischen 1 und 10:");    
        zahl =  scan.nextInt();
    }
    while (!(0 < zahl && zahl <= 10));

    print("Deine Zahl ist: " + String.valueOf(zahl) + ".");
    scan.close();

    }
}
