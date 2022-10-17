
package octubre17;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Alumno {
    
    private Scanner teclado;
    private String nombre;
    private float edad;
    
  public Alumno(){
     
    teclado= new Scanner(System.in);
    
    nombre=JOptionPane.showInputDialog(null,"ingrese su nombre");
    edad=Float.parseFloat(JOptionPane.showInputDialog(null,"ingrese su edad"));
       
    }
  public void imprimir(){
 
    JOptionPane.showMessageDialog(null,"su nombre es :"+nombre);
    JOptionPane.showMessageDialog(null,"su edad es :"+edad);

  }
  public void esMayorEdad(){

     if(edad>=18){
     JOptionPane.showMessageDialog(null,"es mayor de edad");
     }else
         JOptionPane.showMessageDialog(null,"es menor de edad");
         
    }
    
}
