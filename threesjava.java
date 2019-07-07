import java.util.*;
public class threesjava {
  
  public static void main(String[] args) {
    
     Scanner myObj = new Scanner(System.in);
    System.out.println("Enter cap");
    int cap = myObj.nextInt();
    int n=0;
    for(int i=0; i < cap; i++){
      n=n+1;
      if(myObj.hasNext("3")){
        System.out.println("ouch");  
      }
      else{
        System.out.println(n);
      }
     
     
    }
  }
     
      }      
  
  
