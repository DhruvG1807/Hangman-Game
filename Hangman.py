#Topic: Hangman
#Members: Dhruv Gupta, Rohan Bhandari, Manas Narang, Chayank
import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="pname")
    mycursor = mydb.cursor()
    cursor = mydb.cursor(prepared=True)


    import random

    def playagain():
         
        while True:
            play = input("Do you want to play again?(Y/N) ")
            play.upper()
            
            if play == 'Y':
                print("Your points this round was", points)
                game()
            elif play == 'N':
                print("Thank you for playing! ")
                break
         
    def game():
         
        category = input("""Please select a category, Enter:
1:Pokemon
2:Movies
3:Footballers
""")
        
        while True:
            if category == '1':
                pokemon=["bulbasaur","ivysaur","venusaur","charmander","charmeleon","charizard","squirtle","wartortle","blastoise",
                "caterpie","metapod","butterfree","weedle","kakuna","beedrill","pidgey","pidgeotto","pidgeot","rattata",
                "raticate","spearow","fearow","ekans","arbok","pikachu","raichu","sandshrew","sandslash","nidoran","nidorina",
                "nidoqueen","nidoran","nidorino","nidoking","clefairy","clefable","vulpix","ninetales","jigglypuff",
                "wigglytuff","zubat","golbat","oddish","gloom","vileplume","paras","parasect","venonat","venomoth","diglett",
                "dugtrio","meowth","persian","psyduck","golduck","mankey","primeape","growlithe","arcanine","poliwag",
                "poliwhirl","poliwrath","abra","kadabra","alakazam","machop","machoke","machamp","bellsprout","weepinbell",
                "victreebel","tentacool","tentacruel","geodude","graveler","golem","ponyta","rapidash","slowpoke","slowbro",
                "magnemite","magneton","farfetch'd","doduo","dodrio","seel","dewgong","grimer","muk","shellder","cloyster",
                "gastly","haunter","gengar","onix","drowzee","hypno","krabby","kingler","voltorb","electrode","exeggcute",
                "exeggutor","cubone","marowak","hitmonlee","hitmonchan","lickitung","koffing","weezing","rhyhorn","rhydon",
                "chansey","tangela","kangaskhan","horsea","seadra","goldeen","seaking","staryu","starmie","mr mime","scyther",
                "jynx","electabuzz","magmar","pinsir","tauros","magikarp","gyarados","lapras","ditto","eevee","vaporeon",
                "jolteon","flareon","porygon","omanyte","omastar","kabuto","kabutops","aerodactyl","snorlax","articuno",
                "zapdos","moltres","dratini","dragonair","dragonite","mewtwo","mew"]
                break
              
            elif category =='2':
                pokemon = ["the dark knight rises", "batman begins", "avengers endgame", "iron man", "inception", "interstellar", "capain america civil war",
                  "oblivion", "ant man", "catch me if you can", "thor", "shawshank redemption", "pulp fiction", "deadpool", "the martian", "titanic",
                  "the departed", "the incredibles", "social network", "the founder", "fifty shades of grey", "men in black", "casino royale", "fast and furious",
                  "lord of the rings", "harry potter and the half blood prince", "star wars", "hunger games", "room", "f9", "top gun maverick", "avatar",
                  "the godfather", "aquaman", "wonder woman" ,"shazam", "captain marvel", "forrest gump", "guardians of the galaxy", "jurassic park",
                  "rush hour", "drunken master", "shaolin soccer", "jumanji", "the incredible hulk", "black panther" ]
                break

            elif category == '3':
                pokemon = ["andrea pirlo","diego maradona","ronaldo","ronaldinho","lionel messi","cristiano ronaldo","pele","zinedine zidane","johan cryuff",
                           "andres iniesta","gianluigi buffon","luka modric","george best","xavi","franz beckenbauer","roberto carlos","thierry henry",
                           "zlatan ibrahimovic","neymar jr","ryan giggs","david beckham","raul","carles puyol","didier drogba","steven gerrard","sergio ramos",
                           "manuel neuer","gareth bale","cafu","francesco totti","gerd muller","lev yashin","samuel eto'o","ferenc puskas","roberto baggio",
                           "romario","luis suarez","kaka","toni kroos","alfredo di stefano","phillip lahm","iker casillas","robert lewandowski","luis figo",
                           "dennis bergkamp","eusebio","thiago silva","zico","wayne rooney","arjen robben"]
                break
              
            else:
                category = input("""INVALID!Please select a category, Enter:
1:Pokemon
2:Movies
3:Footballers
""")
                
        global points
        wronguess=""
        list1 = []
        lives=3
        points=0
        
        while True:
             x=random.randint(1,len(pokemon)-1)
             if x in list1:
                 continue
             else:
                list1.append(x)
                a=pokemon[x]
                pkmn=[]
                
                for i in a:
                    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                        pkmn+=i
                    elif i==" ":
                        pkmn+=" "
                    else:
                        pkmn+="-"
                        
             print("".join(pkmn))
             count=0
             
             while count<7:
                x=0
                n = input("Enter a letter: ")
                n = n.lower()
                
                if n in wronguess and n!= " ":
                    print("You already guessed this letter!")
                    continue
                   
                if len(n)>1:
                    print("Please enter 1 letter at a time")
                    continue

                if n in ("a", "e", "i", "o", "u"):
                    print("Vowels are already given!")
                    x=2
                
                for i in range(len(a)):
                    if a[i] == n:
                        pkmn[i] = n
                        x=1
                print("".join(pkmn))
                
                if x==0:
                    wronguess = wronguess+" "+n
                    count+=1
                    print("Wrong guesses:",wronguess)
                    if 7-count!=1:
                        print("Wrong guess, You have",7-count,"guesses left")
                    elif 7-count==1:
                        print("Wrong guess, You have",7-count,"guess left")
                        
                if "".join(pkmn)==a:
                    print("You win")
                    points+=1
                    break
                   
                if count==7:
                    print("You Lose, the correct word was", a)
                    lives-=1
                    print("You have", lives,"lives left")
                    break
                
             if lives==0:
                 
                 if category == '1':
                     mysql_insert_query = """INSERT INTO leaderboard(player_name, score) values(%s, %s)"""
                 elif category == '2':
                     mysql_insert_query = """INSERT INTO mvs(player_name, score) values(%s, %s)"""
                 else:
                     mysql_insert_query = """INSERT INTO ftbl(player_name, score) values(%s, %s)"""
                 insert_tuple = (name_of_player, points)
                 mycursor.execute(mysql_insert_query, insert_tuple)

                 if category =='1':
                     mycursor.execute("""select * from leaderboard
where score >= (select max(score) from leaderboard
where score < (select max(score) from leaderboard
where score < (select max(score) from leaderboard)))
order by score desc;""")
                     myresult=mycursor.fetchall()
                     for x in myresult:
                         print(x)

                 elif category == '2':
                     mycursor.execute("""select * from mvs
where score >= (select max(score) from mvs
where score < (select max(score) from mvs
where score < (select max(score) from mvs)))
order by score desc;""")
                     myresult=mycursor.fetchall()
                     for x in myresult:
                         print (x)

                 else:
                     mycursor.execute("""select * from ftbl
where score >= (select max(score) from ftbl
where score < (select max(score) from ftbl
where score < (select max(score) from ftbl)))
order by score desc;""")
                     myresult=mycursor.fetchall()
                     for x in myresult:
                         print (x)
                                      
                 mydb.commit()
                 playagain()
                 break
              
             ifcont = input("Do you want to continue?(Y/N) ")
             ifcont = ifcont.upper()
             
             if ifcont == 'N':
                 mysql_insert_query = """INSERT INTO leaderboard(player_name, score) values(%s, %s)"""
                 insert_tuple = (name_of_player, points)
                 mycursor.execute(mysql_insert_query, insert_tuple)
                 mydb.commit()
                 break
             wronguess = ""

                 
    print ("You have 3 lives to score as many points as possible by guessing 1 alphabet at a time.\n"
           "All the vowels of the word are given and you have 7 chances to guess the word correctly")

    global name_of_player
    name_of_player=input("Enter your Name: ")
    game()

    print ("GAME OVER")
    print ("Your overall points is", points)

except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


