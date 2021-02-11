/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ErsteKlassen;

import java.lang.*;
import java.util.*;
class HalloObjekt{
    String str;
    
    HalloObjekt(String str){
        this.str = str;
    }
    void ausgabe(){
        for(int i=0; i<str.length();i++){
            System.out.println(str);
        }
    }
    
        
}

public class ErsteKlassen {

    public static void main(String[] args) {
        HalloObjekt a = new HalloObjekt("Matthias du bist ein sexy Boy 69");
        a.ausgabe();
        
    }
    } 
  

