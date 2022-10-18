package unipi;

import java.io.Serializable;
import java.util.Scanner;

public class Animals implements Serializable{

    private String id ;
    private String name;
    private String type;
    private float weight;
    private int age;



    public void animalFile(){

        Scanner input = new Scanner(System.in);
        System.out.println("Give an id of the animal");
        this.id = input.nextLine();
        System.out.println("Give animal's name");
        this.name = input.nextLine();
        System.out.println("Give animal's class");
        this.type = input.nextLine();
        System.out.println("Give animal's avg weight in kg");
        this.weight = input.nextFloat();
        System.out.println("Give animal's avg max age");
        this.age = input.nextInt();
    }

    public String toString() {
        return "id=" + id + ", name=" + name + ", class=" + type + ", weight=" + weight + ", age=" + age +"";
    }

    public String animal_name(){
        return name;
    }
    public String findid(){
        return id;
    }
    public String animal_type(){
        return type;
    }


}
