void pause(float m_sek){
  float start = millis();
  float ende = m_sek + start;
  while(ende - millis() > 0){}
}
