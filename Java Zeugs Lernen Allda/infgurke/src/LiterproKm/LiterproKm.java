
package LiterproKm;
import java.util.*;
class auto{
    double anf, end, liter;
    auto(double anf, double end, double liter){
        this.anf = anf;
        this.end = end;
        this.liter = liter;
    }
    double MPG(){
        
        return liter/(end-anf);
    }   
}
public class LiterproKm {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        auto auto = new auto(10, 20, 10);
        
        System.out.println(auto.MPG());
        
    }
    } 
  

