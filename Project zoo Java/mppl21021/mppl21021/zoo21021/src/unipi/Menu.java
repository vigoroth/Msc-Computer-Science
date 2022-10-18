package unipi;
import java.io.*;
import java.util.ListIterator;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;


public class Menu {
    public static void  main(String[] args){

        //Array lit Animals//
        ArrayList<Animals> animals = new ArrayList<>();







        //Load the file if file exists

        File file = new File("listofanimals.txt");
        if(file.exists())
            try {
                FileInputStream fis = new FileInputStream("listofanimals.txt");
                ObjectInputStream ois = new ObjectInputStream(fis);
                animals = (ArrayList) ois.readObject();
                ois.close();
                fis.close();
            }
            catch (IOException ioe)
            {
                ioe.printStackTrace();
                return;
            }
            catch (ClassNotFoundException c)
            {
                System.out.println("Class not found");
                c.printStackTrace();
                return;
            }
        else {

            //create a new file

            try {
                FileOutputStream fos = new FileOutputStream("listofanimals.txt");
                ObjectOutputStream oos = new ObjectOutputStream(fos);
                oos.writeObject(animals);
                oos.close();
                fos.close();
            } catch (IOException ioe) {
                ioe.printStackTrace();
            }
        }
        Scanner input = new Scanner(System.in);
        String choice = null;




        while (!"8".equals(choice)) {

            System.out.println("\n Zoo Menu \n");
            System.out.println("1. Show the animals of the zoo");
            System.out.println("2. Add new animal-animals");
            System.out.println("3. Find an animal with the name");
            System.out.println("4. Find an animla with id");
            System.out.println("5. Delete an animal with id");
            System.out.println("6. Feed the animals");
            System.out.println("7. Save");
            System.out.println("8. Exit\n");
            System.out.println("Select your Choice");
            choice = input.nextLine();
            if ("1".equals(choice)) {

                //show the list -create iterator//

                ListIterator iterator = animals.listIterator();
                System.out.println("List of Animals:");
                if (animals.isEmpty()) {

                    System.out.println("Empty!!\n");
                } else {
                    while (iterator.hasNext()) {
                        System.out.println(iterator.next());
                    }
                }


            }

            else if ("2".equals(choice)) {

                //Add new animal//

                Animals animal = new Animals();
                animal.animalFile();
                animals.add(animal);

            }

            else if ("3".equals(choice)) {
                //find animal with name

                System.out.println("Give animal's name:");
                String findanimal = input.nextLine();
                ListIterator<Animals> iterator = animals.listIterator();
                while (iterator.hasNext()) {
                    Animals animal = iterator.next();
                    if (animal.animal_name().equals(findanimal)) {
                        System.out.println(animal);
                    }


                }


            }

            else if ("4".equals(choice)) {

                //find animal via id
                System.out.println("Give animal's id:");
                String animalid = input.nextLine();
                ListIterator<Animals> iterator = animals.listIterator();
                while (iterator.hasNext()) {
                    Animals animal = iterator.next();
                    if (animal.findid().equals(animalid)) {
                        System.out.println(animal);
                    }
                }
            } else if ("5".equals(choice)) {
                // delete animals from the list
                System.out.println("Give id:");
                String deleteid = input.nextLine();
                ListIterator<Animals> iterator = animals.listIterator();
                while (iterator.hasNext()) {
                    Animals animal = iterator.next();
                    if (animal.findid().equals(deleteid)) {
                        animals.remove(animal);
                        break;
                    }
                }

            } else if ("6".equals(choice)) {
                //feed animals

                System.out.println("Select animal to feed (name)");
                String name = input.nextLine();
                ListIterator<Animals> iterator = animals.listIterator();
                while (iterator.hasNext()) {
                    Animals animal = iterator.next();
                    if (animal.animal_name().equals(name)) {
                        if (animal.animal_type().equals("mammals")) {
                            Mammals mammal = new Mammals();
                            mammal.feed(name);
                            break;

                        }
                        else if (animal.animal_type().equals("reptiles")) {
                            Reptiles reptile = new Reptiles();
                            reptile.feed(name);
                            break;
                        }
                        else if (animal.animal_type().equals("birds")) {
                            Birds bird = new Birds();
                            bird.feed(name);
                            break;
                        }

                        else if (animal.animal_type().equals("fish")) {
                            Fish fish = new Fish();
                            fish.feed(name);
                            break;
                        }


                    }

                }

            }

            else if ("7".equals(choice)) {
                try {
                    FileOutputStream fos = new FileOutputStream("listofanimals.txt");
                    ObjectOutputStream oos = new ObjectOutputStream(fos);
                    oos.writeObject(animals);
                    oos.close();
                    fos.close();
                } catch (IOException ioe) {
                    ioe.printStackTrace();
                }


            }





        }


        input.close();
        System.out.println("Exiting the program\n");



    }
}
