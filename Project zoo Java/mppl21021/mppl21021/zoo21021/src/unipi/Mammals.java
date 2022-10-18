package unipi;
import java.util.Scanner;


public class Mammals extends Animals implements Feed{

    String food;


    Mammals(){
        System.out.println("This animal is mammal and eats plants\n");
        Scanner input = new Scanner(System.in);
        System.out.println("With what do you want to feed the mammal?");
        this.food = input.nextLine();
    }
    public void feed(String name) {
        System.out.println(name + " has eaten " + food);
    }

}
