/* created by Jenny Trac
Created on nov 30 2017
program translates sentences into Pig-latin*/

import java.util.Scanner;

public class PigLatinConverter {
  
    public static String word_converter(String english_word)
    {
    String[] english_word_array = english_word.split("");
    String first_letter = english_word_array[1];
    String new_word = "";    
    for (int counter = 2; counter < english_word_array.length; counter++)
        {
        new_word = new_word + english_word_array[counter];
        }
    new_word = new_word + first_letter + "ay";
    
    return new_word;
    }
    
    public static void main(String[] args)
    {
    // instructions
    System.out.println("Enter a sentence to be translated into Pig Latin:");
    
    // input
    Scanner problem = new Scanner(System.in);
    String[] english_sentence = (problem.nextLine()).split(" ");
    
    //process
    String pig_latin_sentence = "Pig Latin sentence: ";
    for (int count = 0; count < english_sentence.length; count++)
        {
        String pig_latin_word = PigLatinConverter.word_converter(english_sentence[count]);
        pig_latin_sentence = pig_latin_sentence + " " + pig_latin_word;
        }
    
    // output
    System.out.println(pig_latin_sentence);
    }

}
