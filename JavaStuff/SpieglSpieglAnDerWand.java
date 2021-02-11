import java.util.Scanner;


public class SpieglSpieglAnDerWand {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str;
        StringBuffer strb;

        while (true)
        {
            str = scan.nextLine();
            if ( str.equals("quit()") ) 
            {
                break;
            }
            if (str.equals("") )
            {
                str = "Spieglein Spieglein an der Wand";
            }
            strb = new StringBuffer(str);
            System.out.println(strb.reverse());
        }
        scan.close();
    }
}
