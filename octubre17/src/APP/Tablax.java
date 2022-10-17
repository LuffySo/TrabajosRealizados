
package APP;

public class Tablax {
    
    private int tabla;
    private int terminos;
    
    public Tablax(int ta,int ter){
    
    tabla=ta;
    terminos =ter;
    
    }
    public Tablax(int ta){
    tabla=ta;
    terminos=10;
    
    }
    public void imprimir(){
        System.out.println("tabla de multiplicar del "+tabla);
        
        for(int f=1; f<=terminos;f++){
          int resultado=f*tabla;
            System.out.println(tabla+"x"+f+"="+resultado);
            
         }
    
    }
    public static void main(String[] args) {
        Tablax tabla1 =new Tablax(5);
        tabla1.imprimir();
        Tablax tabla2= new Tablax(3,5);
        tabla2.imprimir();
        
    }
}
