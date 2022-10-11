
package ejercicio2;


public class Textos {
    
    
    public  static void parrafo(){
    
      String texto="hola";
      String texto2="tony";
      String texto3="";
      
      texto3 ="Como estas ".concat(texto2);
      System.out.println("texto3"+texto3);
      System.out.println("nro de letras texto1"+texto.length());
      System.out.println("saca 5 letras:" +texto3.substring(5,10));
      System.out.println("saca 5 letras:"+ texto3.toUpperCase());
      String texto4="este es un texto\n texto largo\n largooo";
       System.out.println(texto4);
       
       String s1 ="abc";
       String s2 ="cde";
       
        System.out.println(s1.compareTo(s2));
        System.out.println(s1.equals(s2));
      
      
      
        
    }
    
}
