
package octubre17;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class trabajo17 {
    
    public static void eje1(){
    
        try {
            String cadena;
            FileReader leer= new FileReader("D:\\proyectosJava\\octubre17\\src\\octubre17\\nota1.txt");
            
            BufferedReader b= new BufferedReader(leer);
            
            while ((cadena=b.readLine()) !=null) {                
                System.out.println(cadena);
            }
            b.close();
            
        } catch (Exception e) {
            System.out.println("archivo no encontrado");
        }
        
        
    
    }
    public static void eje2(){
    
    Scanner lectura= new Scanner(System.in);
    
    double num1,num2,resultado;
    
        try {
            num1=Double.parseDouble(JOptionPane.showInputDialog(null,"ingrese un numero"));

             num2=Double.parseDouble(JOptionPane.showInputDialog(null,"ingrese un segundo numero"));
            resultado=num1/num2;

            JOptionPane.showMessageDialog(null,"el resultado es :"+resultado);
            
            
          }
       
        catch (ArithmeticException e) {

            JOptionPane.showMessageDialog(null,"No se puede dividir entre 0");
          }
        catch(Exception e){
            JOptionPane.showMessageDialog(null,"ocurrio un error");
          
          }
        finally{
            lectura.close();}
    
        
    }
}
