package unipi;
import java.util.Scanner;
public class Fish extends Animals implements Feed{
    String food;

    Fish(){
        System.out.println("This animal is fish and eats  worms and other fish\n");
        Scanner input = new Scanner(System.in);
        System.out.println("With what do you want to feed the fish?");
        this.food = input.nextLine();
    }

    public void feed(String name) {
        System.out.println(name + " has eaten " + food);
    }

}
