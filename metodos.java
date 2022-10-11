
package ejercicio2;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class metodos {
    
    public static void hola(){
    
        System.out.println("hola mundo");
      }
    
    public static void numeroImpar(){
    
        int numero;
        
        numero=Integer.parseInt(JOptionPane.showInputDialog(null,"ingrese un numero"));
        
        if(numero %2==0){
        JOptionPane.showMessageDialog(null, "El numero es par");
        }else{
        JOptionPane.showMessageDialog(null, "el numero es impar");
           }
    }
       public static void datos(){
        
        
        int a = 2;
        double b = 3.0;
        float c = (float) (20000*a/b + 5);
        System.out.println("Valor en formato float: " + c);
        System.out.println("Valor en formato double: " + (double) c);
        System.out.println("Valor en formato byte: " + (byte) c);
        System.out.println("Valor en formato short: " + (short) c);
        System.out.println("Valor en formato int: " + (int) c);
        System.out.println("Valor en formato long: " + (long) c);
        
        
        if (a>b) {
                   System.out.println("a es mayor que b");
        }else {
                 System.out.println("a no es mayor que b");}      
    } 
    
    public static void aplicacion2(){
            
     char v1,v2;
     
     int i=-3;
     byte b=5;
     float f=1e-10f;
     double d=3.14;
     boolean b1=i>b;
     boolean b2=i<b;
     boolean b3= b<=f;
     boolean b4=f>=d;
     boolean b5=d!=0;
     boolean b6=1==f;
     
     v1= 'a';
     v2= 'b';
     
        System.out.println("b1 :"+i+">"+i+"= "+b1);
        System.out.println("b2 :"+i+">"+i+"= "+b2);
        System.out.println("b3 :"+b+">"+i+"= "+b3);
        System.out.println("b4 :"+f+">"+i+"= "+b4);
        System.out.println("b5 :"+d+">"+i+"= "+b5);
        System.out.println("b1 :"+1+"=="+f+"="+b6);
        
        boolean v3= v1>v2;
        
        System.out.println("v1 es mayor que v2: "+v3);
        
        
   }
   
   public static void promedio(){
     Scanner entrada=new Scanner(System.in);
   int nota1,nota2,nota3;
   
       System.out.println("ingrese nota 1");
       nota1=entrada.nextInt();
       System.out.println("ingrese nota 2");
       nota2=entrada.nextInt();
       
       System.out.println("ingrese nota 3");
       nota3=entrada.nextInt();
   
   
   
   int promedio =(nota1+nota2+nota3)/3;
       System.out.println("Promedio: "+promedio);
       
       if(promedio>10.5){
           System.out.println("Aprobado");
       }else{
           System.out.println("Desaprobado");
       }
   
   }
      
}
