/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ObjektArray;

import java.lang.*;
import java.util.*;
public class ObjektArray {
    public static void main(String[] args) {
        List<String> einearrayliste = new ArrayList<String>();
        einearrayliste.add("hallo");
        einearrayliste.add("Welt");
        einearrayliste.add("wwrr");
        einearrayliste.add("wfw");
        einearrayliste.add("mama");
        einearrayliste.add("kaka");
        einearrayliste.add("klnkelgbjkeggewb");
        einearrayliste.add("afe");
        einearrayliste.add("jabf");
        String[] simpleArray = new String[ einearrayliste.size() ];
        einearrayliste.toArray( simpleArray );
        
        for(int i=0;i<simpleArray.length;i++){
            System.out.println(simpleArray[i]);
        
        }
    }
    } 
  

