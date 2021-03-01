void setup()
{
  DDRB = DDRB | B10000000; // Data Direction Register B: Inputs 0-6, Output 7
}
void loop()
{
asm (
"inicio: \n\t"
"SBIC 0x03, 6 \n\t"
"call buttonH  \n\t"
"call buttonL  \n\t"
"jmp main \n\t"

"buttonL:"
"sbi 0x05,0x07 \n\t"
"call tiempoLOW \n\t"
"cbi 0x05,0x07 \n\t"
"call tiempoLOW \n\t"
"ret \n\t"

"buttonH:"
"sbi 0x05,0x07 \n\t"
"call tiempoHIGH \n\t"
"cbi 0x05,0x07 \n\t"
"call tiempoHIGH \n\t"
"ret \n\t"

"tiempoLOW: \n\t"
"LDI r22, 40 \n\t"
"LOOP_3: \n\t"
"LDI r21, 255 \n\t"
"LOOP_2: \n\t"
"LDI r20, 255 \n\t"
"LOOP_1: \n\t"
"DEC r20 \n\t"
"BRNE LOOP_1 \n\t"
"DEC r21 \n\t"
"BRNE LOOP_2 \n\t"
"DEC r22 \n\t"
"BRNE LOOP_3 \n\t"
"ret \n\t"

"tiempoHIGH: \n\t"
"LDI r22, 80 \n\t"
"LOOP_3H: \n\t"
"LDI r21, 255 \n\t"
"LOOP_2H: \n\t"
"LDI r20, 255 \n\t"
"LOOP_1H: \n\t"
"DEC r20 \n\t"
"BRNE LOOP_1H \n\t"
"DEC r21 \n\t"
"BRNE LOOP_2H \n\t"
"DEC r22 \n\t"
"BRNE LOOP_3H \n\t"
"ret \n\t"
);
}
