package unipi;

import java.util.Scanner;

public class Birds extends Animals implements Feed{

    String food;

    Birds(){
        System.out.println("This animal is bird and eats seeds.\n");
        Scanner input = new Scanner(System.in);
        System.out.println("With what do you want to feed the bird?");
        this.food = input.nextLine();
    }

    public void feed(String name){
        System.out.println(name + " has eaten " + food);
    }
}
