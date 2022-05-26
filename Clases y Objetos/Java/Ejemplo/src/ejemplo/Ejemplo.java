package ejemplo;

public class Ejemplo {

    public static void main(String[] args) {
        //CREANDO OBJETOS
        Pelicula peli1 = new Pelicula("Venom","Adolescentes", 5.00, 20,1);
        Pelicula peli2 = new Pelicula("Madagascar", "Todos",4.50, 10,2);
        //MOSTRANDO OBJETOS
        System.out.println("NOMBRE: " + peli1.getNombre());
        System.out.println("CANTIDAD: " + peli1.getCantidad());
        System.out.println("CODIGO: " + peli1.getCodigo());
        System.out.println("================================");
        System.out.println("NOMBRE: " + peli2.getNombre());
        System.out.println("PRECIO: " + peli2.getPrecio());
        System.out.println("================================");
        //ACTUALIZANDO OBJETOS
        peli1.setNombre("Venom 2");
        peli1.setPrecio(10.0);
        System.out.println("================================");
        System.out.println("NOMBRE: " + peli1.getNombre());
        System.out.println("CANTIDAD: " + peli1.getCantidad());
        System.out.println("CODIGO: " + peli1.getCodigo());
        System.out.println("PRECIO: " + peli1.getPrecio());
    }
    
}
