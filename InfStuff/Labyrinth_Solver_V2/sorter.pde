ArrayList<Feld> sort(ArrayList<Feld> drehFelder) {
  ArrayList<Feld> end = new ArrayList<Feld>();
  Feld kleinstes = drehFelder.get(0);
  int i = 0;
  int smol, big;
  
  while(drehFelder.size() > 1){
      smol = kleinstes.pos_x + kleinstes.pos_y;
      big = drehFelder.get(i).pos_x + drehFelder.get(i).pos_y;
      print(kleinstes);
      
      if(smol < big){
        i++;
        if(i == drehFelder.size() - 1){
          end.add(kleinstes);
          i = 0;
        }
      }else
      if(smol == big){
        drehFelder.remove(i);
        i = 0;
      }else if(smol > big){
        kleinstes = drehFelder.get(i);
        i++;
      }
  }
  
  return end;
}
