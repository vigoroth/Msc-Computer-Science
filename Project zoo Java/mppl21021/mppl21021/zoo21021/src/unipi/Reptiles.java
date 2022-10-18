package unipi;

import java.util.Scanner;

public class Reptiles extends Animals implements Feed {


    String food;


    Reptiles(){
        System.out.println("This animal is reptile and eats plants and mammals\n");
        Scanner input = new Scanner(System.in);
        System.out.println("With what do you want to feed the reptile?");
        this.food = input.nextLine();
    }
    public void feed(String name) {
        System.out.println(name + " has eaten " + food);
    }
}
