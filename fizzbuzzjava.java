import java.util.*;
public class fizzbuzzjava {
  
  public static void main(String[] args) {
    int n = 0;
    //int stop = 100;
    Scanner input = new Scanner(System.in);
    System.out.println("Enter cap");
    int cap = input.nextInt();
    for (int i = 0; i < cap; i++){
      n++;
      //System.out.println(n);
      if (n%3 == 0 && n%5 ==0){
        System.out.println("FizzBuzz " + (n));
      }
      if (n%3 == 0){
        System.out.println("Fizz " + (n));
      }
      if (n%5 == 0){
        System.out.println("Buzz " + (n));
        
      }
    }
  }
}