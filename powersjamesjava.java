import java.util.*;
import java.lang.*;

public class powersjamesjava {
  
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter cap: ");
    double cap = input.nextInt();  
    System.out.println("Enter multiple: ");
    double multiple = input.nextInt();
    int i = 0;
    double foo = 0;
    while(foo < cap){
    foo = Math.pow(multiple, i);
    i+= 1;
    System.out.println(foo);  
    }
    
  }
}