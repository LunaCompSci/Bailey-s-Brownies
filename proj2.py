#Christina Nguyen, 1/9/2021, calculates how much food a baker needs based on # of costumers
costumerNum = int(input("How many people many to be served? "))
batchNumUnround = costumerNum / 12
batchNum = int(batchNumUnround + 0.99) #Rounds up batches

cocoa_Recipe_Amount = 106 #Define amount of ingredients for one recipe as variables
salt_Recipe_Amount = 6
bake_Recipe_Amount = 5
espresso_Recipe_Amount = 2
sugar_Recipe_Amount = 447
flour_Recipe_Amount = 180
chip_Recipe_Amount = 340
butter_Recipe_Amount = 0.5
vanilla_Recipe_Amount = 1
egg_Recipe_Amount = 4

cocoa_Total_Amount = cocoa_Recipe_Amount * batchNum #(x ingredient) total is still in the recipe's units 
salt_Total_Amount = salt_Recipe_Amount * batchNum 
bake_Total_Amount = bake_Recipe_Amount * batchNum
espresso_Total_Amount = espresso_Recipe_Amount * batchNum
sugar_Total_Amount = sugar_Recipe_Amount * batchNum
flour_Total_Amount = flour_Recipe_Amount * batchNum
chip_Total_Amount = chip_Recipe_Amount * batchNum
butter_Total_Amount = butter_Recipe_Amount * batchNum
vanilla_Total_Amount = vanilla_Recipe_Amount * batchNum
egg_Total_Amount = egg_Recipe_Amount * batchNum

cocoa_Required_Containers = cocoa_Total_Amount / (8 * 28.3495231) #convert units used in the recipe to units used in the containers 
salt_Required_Containers = salt_Total_Amount / (26 * 28.3495231)
bake_Required_Containers = bake_Total_Amount / (8.1 * 28.3495231)
espresso_Required_Containers = espresso_Total_Amount / (7.05 * 28.3495231)
sugar_Required_Containers = sugar_Total_Amount / (28.3495231 * 16 * 4)
flour_Required_Containers = flour_Total_Amount / (28.3495231 * 16 * 4)
chip_Required_Containers = chip_Total_Amount / (12 * 28.3495231)
butter_Required_Containers = butter_Total_Amount / 1 #same units don't need unit conversation but they need container conversation 
vanilla_Required_Containers = (vanilla_Total_Amount * 3 /48 * 8) /2
egg_Required_Containers = egg_Total_Amount / 18 #same units don't need unit conversation but they need container conversation

cocoa_Required_Containers_Roundup = cocoa_Required_Containers + 0.999999999999999  #These lines will round up the leftover container needed 
salt_Required_Containers_Roundup = salt_Required_Containers + 0.99999999999999999
bake_Required_Containers_Roundup = bake_Required_Containers + 0.9999999999999999
espresso_Required_Containers_Roundup = espresso_Required_Containers + 0.9999999999999
sugar_Required_Containers_Roundup = sugar_Required_Containers + 0.99999999999999
flour_Required_Containers_Roundup = flour_Required_Containers + 0.99999999999999
chip_Required_Containers_Roundup = chip_Required_Containers  + 0.9999999999999999
butter_Required_Containers_Roundup = butter_Required_Containers + 0.9999999999999 
vanilla_Required_Containers_Roundup = vanilla_Required_Containers + 0.999999999999
egg_Required_Containers_Roundup = egg_Required_Containers + 0.999999999999999 

copowTruncate = int(cocoa_Required_Containers_Roundup) #These lines will truncate
saltTruncate = int(salt_Required_Containers_Roundup)
bakpowTruncate = int(bake_Required_Containers_Roundup)
esppowTruncate = int(espresso_Required_Containers_Roundup)
sugarTruncate = int(sugar_Required_Containers_Roundup)
flourTruncate = int(flour_Required_Containers_Roundup)
chipTruncate = int(chip_Required_Containers_Roundup)
butterTruncate = int(butter_Required_Containers_Roundup)
vanillaTruncate = int(vanilla_Required_Containers_Roundup)
eggTruncate = int(egg_Required_Containers_Roundup)


copowPrice = copowTruncate * 1.99 #These lines will get you the price
saltPrice = saltTruncate * 0.49
bakpowPrice = bakpowTruncate * 1.89
esppowPrice = esppowTruncate * 5.39
sugarPrice = sugarTruncate * 1.99
flourPrice = flourTruncate * 1.99
chipPrice = chipTruncate * 1.99
butterPrice = butterTruncate * 2.99
vanillaPrice = vanillaTruncate* 10.59
eggPrice = eggTruncate * 1.99

totalPrice = copowPrice + saltPrice + bakpowPrice + esppowPrice + sugarPrice + flourPrice + chipPrice + butterPrice + vanillaPrice + eggPrice 
totalPriceTruncate = format(totalPrice,'0,.2f')

print("\nTo serve", costumerNum, "make", batchNum, "batches") #These lines of code align 
print("-"*30,"\n\tGrocery List\n","-"*30, sep='')
print(format("Cocoa", "19s"), copowTruncate)
print(format("\nSalt", "20s"), saltTruncate)
print(format("\nBaking Powder",'20s'),bakpowTruncate)
print(format("\nEspresso Powder",'20s'), esppowTruncate)
print(format("\nSugar",'20s'), sugarTruncate)
print(format("\nFlour",'20s'), flourTruncate)
print(format("\nChocolate Chips",'20s'), chipTruncate)
print(format("\nVanilla", '20s'), vanillaTruncate)
print(format("\nEggs", '20s'), eggTruncate)
print(format("\nButter", '20s'), butterTruncate)
print(format("\n\nTotal price $",'20s'), totalPriceTruncate)

#Testing:
#Things that I did to test were, compare outputs of 100 and 96 people with my classmates. If they were the same, I felt confident.
#One time I had the wrong amount of vanilla because I used a direct conversion factor I found on the internet instead of the ones given.
#Another time, I thought because butter and eggs didn't need any unit conversions that meant they didn't need any conversions at all so I forgot 18!  
#and converted the "2D" math of my unit conversations to "1D" math that I wrote in the code.
#I found this method helped me best keep track of my units.
#Summary:
#I learned how to use the format function and format function specifiers, what truncate means, how to roundup and how important good variable names are.
#Next time I think of better variable names earlier so I don't feel like changing them midway through.
#A place where I got stuck was unit conversations because I'm so used to converting units in "2D" it felt jaring to turn them into "1D" math.
#I got stuck on the rounding up bit but then you went over it in class. I didn't know how the format function worked but I had a friend explain the concept to me.
#I wish I made it so when the number's digits increased, they move the right instead of the left.



