#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gotska_sando
import gladhammar
import malilla
import show_data
import sample
import describe_data
import heatmap
import plots
import linear
import transformation
import residual

def main():
    """
    function data menu
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("Välj ett av alternativen nedan")
        print("1) Hämta ny data från SMHI:s API")
        print("2) Visa urval från data")
        print("3) Visuell representation av data")
        print("4) Beskrivande statistik över data")
        print("5) Heatmap över korrelation")
        print("6) Histogram över normalfördelning")
        print("7) Linjär regression")
        print("8) Transformerad data")
        print("9) Residualanalys")
        print("q) Avsluta.")

        choice_string = input("--> ")
        choice_list = choice_string.split(" ")
        choice = choice_list[0]


        if choice == "q":
            print("Avslutar med statuskod 0")
            break

        elif choice == "1":
            print("Hämtar ny datar från SMHI:s API och uppdaterar CSV-filer...")
            # gotska_sando.gotska_sando_data()
            # malilla.malilla_data()
            # gladhammar.gladhammar_data()
            # print("Data hämtad.")
                    
        elif choice == "2":
            sample.sample_data()
            
        elif choice == "3":
            show_data.visualize_data()
        
        elif choice == "4":
            describe_data.describe_data_csv()
        
        elif choice == "5":
            heatmap.heatmap()
        
        elif choice == "6":
            plots.normal_distribution()
        
        elif choice == "7":
            linear.linear_regression()
        
        elif choice == "8":
            transformation.transformation()
        
        elif choice == "9":
            residual.residual()
        input("\nTryck på enter för att komma vidare...")
        

if __name__ == "__main__":
    main()
