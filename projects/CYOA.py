x_axis = 0
y_axis = 0
z_axis = 0
f_option = 0
w_option = 0
k_option = 0
m_option = 0
s_option = 0
str_option = 0
slh_option = 0
dis_option = 0
Weapon = []
Jennifer_Dead = False
Jennifer_Body = False
Goblin_Village = True
GoblinK_Maim = False
GoblinP_Maim = False
GoblinP_Dead = False
GoblinK_Dead = False
room2 = False
Dead_Village = False
Gold = 0
Honor = 0
Infamy = 0
Strength = 0
Stealth = 0
Finese = 0
Justice = 0
Bloodlust = 0


while True:
	if x_axis == 0 and y_axis == 0 and len(Weapon) == 0:
		answer = input("You wake up in a dark forest. You can remember nothing. As you start to get up, two strange beasts approach. They resemble wolves, but they are twice as large. Around you, there is a rusty sword, a small wooden bow with a few arrows, and two small knives. You only have time to grab one. What do you grab. Choices: sword, bow, or knives. ")
		if answer == "sword" or answer == "rusty sword":
			Weapon.append("Sword")
			Strength = 5
			print("As -athe left beast leaps at you with it's enormous teeth, you grab the rusty sword and swing. The sword bursts into flames and cuts through the poor creature in one fell swoop. As the flames disappear, you see the rusty sword as transformed into a glowing steel sword with a small red gem implanted in the grey hilt. The sword is about 4.5 feet long and 4 inches wide. A brown leather sheathe has appeared on your back. The steel sword shines in the bright sunlight as you ready it. As you prepare to charge at the remaining beast, it growls and wanders off. As you look around, you see that the bow and knives have disappeared.")
		if answer == "bow" or answer == "wooden bow":
			Weapon.append("Bow")
			Finese = 5
			print("As the left beast leaps at you with, baring it's unnaturally shape teeth, you grab the small bow. As you pull an arrow back, the bow and arrow is engulfed in flame. You release the flaming arrow. The arrow pierces the beast body, killing it instantly. The wooden bow has transformed into a solid steel bow with a brown, leather handle. There is a red gem above the handle. A quiver with steel tipped arrows with a small red gem right below the tip. The bow is about 4 feet long and the arrows are 1.5 feet long. You grab another arrow from the brown, leather quiver that has appeared on your back. You hear the bow creak back as you ready another arrow, the remaining beast simply growls and and wanders off. As you look around,you see that the sword and knives have disappeared.")
		if answer == "knives" or answer == "small knives":
			Weapon.append("Knives")
			Stealth = 5
			print("You leap for the two small knives as the left beast leaps at you with it's impossibly large claws outstretched. Once you grab the knives, who throw one, as soon as the knife is thrown, it bursts into flames. The burning knife hits the right leg of the beast. It collapses as soon as it hits the ground. As you swing, aiming for its throat, the knife bursts into flames. As the montrous beast falls, the flames disappear, leaving a steel, curved dagger. The other knife has also transformed. It turned into a similiar curved dagger. Two brown, leather sheathes have appeared on your hips. As you prepare to fight the other beast. The beast growled and left. As you look around, the sword and bow have both disappeared.")

#------------------------------------------------------------------------------------------------------------------------------------------------

	if len(Weapon) >= 1 and x_axis == 0 and y_axis == 0 and z_axis == 0 and Goblin_Village == True: 
		answer = input("Looking around, you observe that you are in a strange forest. The only thing that you can see besides trees and the mountains to the north. There is a tree that extends beyond the forest canopy. After climbing a tree and looking around, you discover a village to the east, a desert to the west, and a dark forest to the south. Choices: go west, go south, go east. ")
		if answer == "north" or answer == "go north":
			y_axis = y_axis + 1
		if answer == "east" or answer == "go east":
			x_axis = x_axis + 1
		if answer == "south" or answer == "go south":
			y_axis = y_axis - 1
		if answer == "west" or answer == "go west":
			x_axis = x_axis - 1

#-----------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 0 and w_option == 0 and room2 == False:
		answer = input("As you walk toward the village, you hear some gibberish. As you quietly creep up on the speaker, you see 2 small, green goblins and 1 person tied up. The goblins are small, humaniod creatures with green skin. Their ears are so long that they droop to the side of there face. The captive appears to wear a snow white gown or dress. One goblin gestures toward the victim voilently with a long, curved dagger, while the other goblin puts himself in between the captive and the knife wielding goblin. The goblin in between the captive and the other goblin holds his hands up. While the knife wielding goblin yells angrily at the second goblin. What will you do? Go back, fight, or wait?" )
		if answer == "go back" or answer == "back" or answer == "Go Back" or answer == "Back":
			x_axis = x_axis - 1
			Jennifer_Dead = True
			Goblin_Village = False
		if answer == "fight" or answer == "fight goblins" or answer == "Fight" or answer == "Fight Goblins":
			f_option = f_option + 1
		if answer == "wait" or answer == "Wait":
			w_option = w_option + 1

#-----------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and w_option == 1:
		answer = input("The knife wielding goblin pushes the other goblin out of the way. He raises his knife preparing to kill the hostage. The knife comes down on the victim's body. As the knife pierces the heart, the victim falls limp. The goblin yanks the knife from the corpse and grabs something from the body. Will you extract revenge or wait? ")
		if answer == "revenge" or answer == "Revenge" or answer == "extract revenge" or answer == "Extract Revenge":
			f_option = f_option + 1
			GoblinK_Dead = True
			Jennifer_Dead = True
		if answer == "move" or answer == "move on" or answer == "wait" or answer == "Wait":
			w_option = w_option + 1
			Goblin_Village = False
			Jennifer_Dead = True

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == False and GoblinP_Dead == False and w_option == 2:
		answer = input("As the goblins move on, they leave the corpse. Her snow white dress is tainted by her bright red blood. The goblins appear to have taken all her jewelry and gold. Will you take the body to the village or leave? ")
		if answer == "take body" or answer == "Take Body" or answer == "take the body to village" or answer == "Take the Body to Village" or answer == "Take The Body To Village":
			Jennifer_Body = True
			w_option = w_option - 2
			x_axis = x_axis + 1
			room2 = True
		if answer == "Leave" or answer == "leave":
			x_axis = x_axis + 1
			w_option = w_option - 2
			room2 = True

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Sword" in Weapon:
		answer = input("You dash out, sword ready to swing. The sword bursts into flames as you swing it. However, the flames are a bright red. The goblin with the knife tries to block your brutal slash, but the knife and its wielder is cut in half. The other goblin looks at you, its hideous, green face is full of fear. A small part of you craves his blood. You begin to tread toward him, sword prepared to run him through. However, a small flashback of him protecting the girl appears. Will you kill him, or spare him? ")
		if answer == "Kill" or answer == "kill" or answer == "Kill Him" or answer == "kill him":
			Bloodlust = Bloodlust + 5
			Infamy = Infamy + 5
			GoblinK_Dead = True
			GoblinP_Dead = True
			Jennifer_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True
		if answer == "Spare" or answer == "spare" or answer == "spare him" or answer == "Spare Him":
			Justice = Justice + 5
			Honor = Honor + 5
			GoblinK_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Bow" in Weapon:
		answer = input("You raise your bow and pull back a flaming arrow. The fire, however, is a bright red. You shoot it at the goblin with the knife. You yells in pain as the arrow imbeds itself in his arm. You then put an arrow in his forhead. You pull back another arrow as you aim it at the other goblin. His face is full of fear and surprise. A small voice urges you to kill him, while you remember that he tried to defend the girl. Will you kill or spare. ")
		if answer == "Kill" or answer == "kill" or answer == "Kill Him" or answer == "kill him":
			Bloodlust = Bloodlust + 5
			Infamy = Infamy + 5
			GoblinK_Dead = True
			GoblinP_Dead = True
			Jennifer_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True
		if answer == "Spare" or answer == "spare" or answer == "spare him" or answer == "Spare Him":
			Justice = Justice + 5
			Honor = Honor + 5
			GoblinK_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True
			
#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Knife" in Weapon:
		answer = input("You throw a knife at the knife wielding goblin. The knife bursts into flames as it rolls through the air. As the goblin yells in pain, you dash at him. He tries to defend himself, but your flaming knives swiftly cut his arm off. You then proceed to finish him. You look over to the stunned goblin, he looks afraid. ")
		if answer == "Kill" or answer == "kill" or answer == "Kill Him" or answer == "kill him":
			Bloodlust = Bloodlust + 5
			Infamy = Infamy + 5
			GoblinK_Dead = True
			GoblinP_Dead = True
			Jennifer_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True
		if answer == "Spare" or answer == "spare" or answer == "spare him" or answer == "Spare Him":
			Justice = Justice + 5
			Honor = Honor + 5
			GoblinK_Dead = True
			Goblin_Village = False
			Strength = Strength + 5
			room2 = True

#----------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == True and w_option == 1 and f_option == 1 and "Knife" in Weapon:
		print("You swiftly dash toward him, your fire now a blood red. You jab your blade deep into his stomach. He doubles over in pain. You then proceed to brutally end the poor creature. You smile cruelly when you finish your \"Masterpiece\". You then smile as you move toward the village.")
		x_axis = x_axis + 1
		w_option = 0
		f_option = 0
		continue
		
#---------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Knife" in Weapon and room2 == True:
		print("You gently lower your knives and walk toward the girl's corpse. You gently pick her up  body. A small nagging tells you that you could've saved her. You could have killed the goblins before she died. Why did you just stand there?")
		Jennifer_Body = True
		Weapon.append("Goblin Knife")
		w_option = 0
		f_option = 0
		x_axis = x_axis + 1
		continue

#----------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == True and w_option == 1 and f_option == 1 and "Bow" in Weapon:
		print("You drop your bow and grip the blazing arrow. You lunge at him impaling his arm like it was a pillow. He screams in pain as you continue your assault. As you finish your bloody work. You smile at the bright red liquid that stains the ground. You pick up your bow and walk to the village. Smiling and humming a happy tune.")
		x_axis = x_axis + 1
		w_option = 0
		f_option = 0
		continue
		
#---------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Bow" in Weapon and room2 == True:
		print("You put down the bow and put the arrow back in the quiver. You walk toward the girl's lifeless body. You untie her and pick her up. You fill guilty looking at her pale face. You could have saved her. But, you chose to wait. Why?")
		Jennifer_Body = True
		Weapon.append("Goblin Knife")
		w_option = 0
		f_option = 0
		x_axis = x_axis + 1
		continue

#----------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == True and w_option == 1 and f_option == 1 and "Sword" in Weapon:
		print("You dash at the frightened goblin. Your sword cuts off his arm like it was air. You let loose a laugh as you rip apart his body. The scene is hiddeous. You smile cruelly at your bloody masterpiece. You start toward the village, your fire turning a blood red with a hint of black.")
		x_axis = x_axis + 1
		w_option = 0
		f_option = 0
		continue
		
#---------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == True and Goblin_Village == False and GoblinK_Dead == True and GoblinP_Dead == False and w_option == 1 and f_option == 1 and "Sword" in Weapon and room2 == True:
		print("You walk away from the frightened goblin. You take the knife from the dead goblin and pick up the girl's corpse. You look back and find the goblin gone. You frown at the girl's corpse and remember that you chose to wait instead of take action. Guilt fills your head as you start toward the village. Why didn't you take action.")
		Jennifer_Body = True
		Weapon.append("Goblin Knife")
		w_option = 0
		f_option = 0
		x_axis = x_axis + 1
		continue

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and "Sword" in Weapon and str_option == 0 and slh_option == 0 and dis_option == 0:
		answer = input("How will you attack? Choices: Charge, Stealth, or Distract ")
		if answer == "Charge" or answer == "charge":
			str_option = str_option + 1
		if answer == "Stealth" or answer == "stealth":
			slh_option = slh_option + 1
		if answer == "Distract" or answer == "distract":
			dis_option = dis_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Sword" in Weapon:
		answer = input("You jump out of the bushes at full charge. Your sword is raised behind you as you prepare to swing. The sword ignites in a fiery arua only matched by your intent to kill. The knife wielding goblin tries to block your sword, but your sword cuts through it with no resistance. The goblin falls to the ground as you raise your sword to kill him. His face fills with fear as his friend runs toward him. Choice: Kill, Maim, or Spare ")
		if answer == "Kill" or answer == "kill":
			Strength = Strength + 5
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			GoblinK_Dead = True
			k_option = k_option + 1
		if answer == "Maim" or answer == "maim":
			Strength = Strength + 5
			m_option = m_option + 1
			Justice = Justice + 5
			GoblinK_Maim = True
		if answer == "Spare" or answer == "spare":
			Strength = Strength + 5
			Honor = Honor + 1
			s_option = s_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Sword" in Weapon and Stealth < 5:
		answer = input("You quietly crawl around the goblins. But, you weren't quiet enough. The knife wielding goblin cautiously creeps toward you hiding place. Will you kill him or injure him? ")
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Stealth = Stealth + 5
			Bloodlust = Bloodlust + 5
			k_option = k_option + 1
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinF_Maim = True
			Honor = Honor + 1
			Justice = Justice + 5
			Stealth = Stealth + 5
			m_option = m_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Sword" in Weapon and Finese < 5:
		answer = input("You quietly pick up a rock from near by and throw it into a bush. But, your throw was too clumsy. The goblins quickly identify you. The one with a knife runs toward you. How will you defend yourself. Will you kill or injure him?" )
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			Finese = Finese + 5
			k_option = k_option + 1
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinK_Maim = True
			Honor = Honor + 1
			Justice = Justice + 5
			Finese = Finese + 5
			m_option = m_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and "Bow" in Weapon and str_option == 0 and slh_option == 0 and dis_option == 0:
		answer = input("How will you attack? Choices: Charge, Stealth, or Distract ")
		if answer == "Charge" or answer == "charge":
			str_option = str_option + 1
		if answer == "Stealth" or answer == "stealth":
			slh_option = slh_option + 1
		if answer == "Distract" or answer == "distract":
			dis_option = dis_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Bow" in Weapon:
		answer = input("You gently pull an arrow back and launch it into a bush. The goblins stare transfixed at where your arrow went. The goblin with the knife slowly walks forward to investigate. Immediantely you jump out, pulling an arrow back. The arrow disables the knife-wielding goblin. He stands there stunned and in pain. Will you kill, maim, your spare. ")
		if answer == "Kill" or answer == "kill":
			Finese = Finese + 5
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			k_option = k_option + 1
			GoblinK_Dead = True
		if answer == "Maim" or answer == "maim":
			Justice = Justice + 5
			Finese = Finese + 5
			m_option = m_option + 1
			GoblinK_Maim = True
		if answer == "Spare" or answer == "spare":
			str_option = str_option + 1
			Finese = Finese + 5
			Honor = Honor + 1
			s_option = s_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Bow" in Weapon and Stealth < 5:
		answer = input("You quietly crawl around the goblins. But, you weren't quiet enough. The knife wielding goblin cautiously creeps toward you hiding place. Will you kill him or injure him? ")
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			Stealth = Stealth + 1
			k_option = k_option + 1
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinF_Maim = True
			Honor = Honor + 1
			Justice = Justice + 5
			Stealth = Stealth + 1
			m_option = m_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Bow" in Weapon and Strength < 5:
		answer = input("You jump out of the bushes, shooting a fiery arrow at the knife wielding goblin. The arrow pierces his arm. But he endures the pain and runs at you full sprint. You can't get out in time. Your only choice is to either kill him or maim him. " )
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			Strength = Strength + 5
			k_option = k_option + 1
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinF_Maim = True
			Honor = Honor + 1
			Justice = Justice + 5
			Strength = Strength + 5
			m_option = m_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and "Knives" in Weapon and str_option == 0 and slh_option == 0 and dis_option == 0:
		answer = input("How will you attack? Choices: Charge, Stealth, or Distract ")
		if answer == "Charge" or answer == "charge":
			str_option = str_option + 1
		if answer == "Stealth" or answer == "stealth":
			slh_option = slh_option + 1
		if answer == "Distract" or answer == "distract":
			dis_option = dis_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Knives" in Weapon:
		answer = input("You quietly go around the goblins until you are right beside them. You jump out of the bushes and grab the goblin with the knife. You toss him to the ground. Your knives burst into flames as you prepare to strike. His friend is frozen from fear. A small voice in your head demands his blood. Will you kill, spare, or injure him. ")
		if answer == "Kill" or answer == "kill":
			Stealth = Stealth + 5
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 5
			k_option = k_option + 1
			GoblinK_Dead = True
		if answer == "Maim" or answer == "maim":
			Justice = Justice + 5
			Stealth = Stealth + 5
			m_option = m_option + 1
			GoblinK_Maim = True
		if answer == "Spare" or answer == "spare":
			str_option = str_option + 1
			Stealth = Stealth + 5
			Honor = Honor + 1
			s_option = s_option + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Knives" in Weapon and Finese < 5:
		answer = input("You gently grip a couple rocks and throw them at a few bushes across from the field, but your throw is a off, and hits a goblin. The goblin immediantely identifies you and starts charging. He's too fast you must either kill or maim him. ")
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Finese = Finese + 1
			k_option = k_option + 1
			Bloodlust = Bloodlust + 5
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinF_Maim = True
			Honor = Honor + 1
			Finese = Finese + 1
			m_option = m_option + 1
			Justice = Justice + 5

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Knives" in Weapon and Strength < 5:
		answer = input("You charge out knives bursting into flames. As you dash forward, the knives leave a trail of smoke behind. The goblin with the knife turns around just in time to dodge your fatal swing. He prepares to lunge at you. You can't dodge, you must kill or disable him. " )
		if answer == "kill" or answer == "Kill" or answer == "kill him" or answer == "Kill Him":
			GoblinK_Dead = True
			Infamy = Infamy + 1
			Strength = Strength + 5
			k_option = k_option + 1
			Bloodlust = Bloodlust + 5
		if answer == "injure" or answer == "Injure" or answer == "Injure Him" or answer == "injure him":
			GoblinF_Maim = True
			Honor = Honor + 1
			Justice = Justice + 5
			m_option = m_option + 1
			Strength = Strength + 5

#------------------------------------------------------------------------------------------------------------------------------------------------
	
	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Sword" in Weapon and k_option == 1:
		answer = input("You bring the sword down upon the poor goblin. As the sword rips through his flesh, he cries in pain, but his cry is cut short. His friend stands stunned. A simple swing of his sword, and he will fall. A small voice at the back of your head urges you to kill him. Will you kill him, injure him, or spare him? ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Justice = Justice + 1
			Honor = Honor + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Maim == True and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Sword" in Weapon and m_option == 1:
		answer = input("You swing your sword, aiming for the shoulder. The sword bites into the arm, severing it from the body. The goblin screams in pain. The other goblin stands stunned. You look at him, deciding what to do. Will you kill him, injure, or spare him? ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Infamy = Infamy + 1
			Bloodlust = Bloodlust + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Justice = Justice + 1
			Honor = Honor + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Maim == True and GoblinP_Dead == False and f_option == 1 and str_option == 1 and "Sword" in Weapon and m_option == 1:
		print("You lower your sword, putting it in it's sheathe. You then knock out the goblin with a quick blow to the head with your foot. The other goblin rushes to his comrad to check if he's hurt. The goblin picks up his friend and takes him away. You untie the girl. She immediantely hugs you and starts crying. You pick her up and start toward the village. ")
		Goblin_Village = False
		f_option = 0
		str_option = 0
		m_option = 0
		x_axis = x_axis + 1
		room2 = True
		continue

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Bow" in Weapon and k_option == 1:
		answer = input("You release the flaming arrow, killing the defenseless goblin. The arrow pierces the goblin's skull, instantly killing the goblin. The other goblin runs to his fallen comrad. You instinctively pull back an arrow to kill the defenseless goblin ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Bloodlust = Bloodlust + 1
			Infamy = Infamy + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Honor = Honor + 1
			Justice = Justice + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Maim == True and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Bow" in Weapon and m_option == 1:
		answer = input("You let loose a single flaming arrow. The arrow pierces the goblin's shoulder, while the flames burn apart the flesh and tendons. The severed arm falls to the ground as the goblin collapses and screams in pain. The other goblin rushes to his friend's aid. \"Kill him\" says a small voice. Will you kill, injure, or spare him. ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Bloodlust = Bloodlust + 1
			Infamy = Infamy + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Honor = Honor + 1
			Justice = Justice + 1

#--------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and dis_option == 1 and "Bow" in Weapon and s_option == 1:
		print("You slowly tread toward their captive. Your bow is trained on the goblins. Neither is brave enough to try and stop you. Eventually, they wonder off. You untie the girl and immediantely she jumps into your arms and starts to cry. You gather pick up the weeping girl and start towards the nearby village.")
		Goblin_Village = False
		f_option = 0
		dis_option = 0
		s_option = 0
		x_axis = x_axis + 1
		room2 = True
		continue

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == True and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Knives" in Weapon and k_option == 1:
		answer = input("You bring your knife down on his throat. Blood coats your knife as you yank it free. The other goblin begins to back up. A small part of you yearns for his blood. Will you kill, injure, or spare him? ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Bloodlust = Bloodlust + 1
			Infamy = Infamy + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Honor = Honor + 1
			Justice = Justice + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Maim == True and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Knives" in Weapon and m_option == 1:
		answer = input("You bring your knife down in an arc, aimed for his right shoulder. The blazing knife cuts through his flesh and bone with ease. He screams in agony as he grips his bloody shoulder. You turn toward his friend. A small urge appears, it urges for his blood. Will you kill, injure, or spare him? ")
		if answer == "Kill Him" or answer == "kill Him" or answer == "kill" or answer == "Kill":
			GoblinP_Dead = True
			k_option = k_option + 1
			Bloodlust = Bloodlust + 1
			Infamy = Infamy + 1
		if answer == "injure" or answer == "Answer" or answer == "Injure Him" or answer == "injure him":
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare Him" or answer == "spare him" or answer == "spare" or answer == "Spare":
			s_option = s_option + 1
			Honor = Honor + 1
			Justice = Justice + 1

#--------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Knives" in Weapon and s_option == 1:
		print("You flip your knife in your hand as you bring it down. The brunt hilt knocks out the violent goblin. You keep an eye on the other goblin as you approach the girl. The other goblin picks up his unconcious friend and hurries away. As soon as you untie the girl, she jumps in your arms and starts to cry. You pick up the sobbing girl and starts toward the village to the east.")
		Goblin_Village = False
		f_option = 0
		dis_option = 0
		s_option = 0
		x_axis = x_axis + 1
		room2 = True
		continue

#------------------------------------------------------------------------------------------------------------------------------------------------

	if x_axis == 1 and y_axis == 0 and z_axis == 0 and Jennifer_Dead == False and Goblin_Village == True and GoblinK_Dead == False and GoblinP_Dead == False and f_option == 1 and slh_option == 1 and "Sword" in Weapon and k_option == 1:
		answer = input("You jump out of the bushes swinging your sword in a horizontal arc. The sword bursts into flames, the flames a bright red. The burning sword cuts the goblin in half right above the stomach. His companion looks on in horror as his friend lie there. Then looks at you and freezes in fear. A tiny voice at the back of your head urges you to kill him. Will you kill, injure, or spare him? ")
		if answer == "Kill" or answer == "kill" or answer == "Kill Him" or answer == "kill him":
			Goblin_Village = False
			GoblinP_Dead = True
			k_option = k_option + 1
			Bloodlust = Bloodlust + 1
		if answer == "Injure" or answer == "injure" or answer == "Injure Him" or answer == "injure him":
			Goblin_Village = False
			GoblinP_Maim = True
			m_option = m_option + 1
		if answer == "Spare" or answer == "spare" or answer == "Spare Him" or answer == "spare him":
			Goblin_Village = False
			s_option = s_option + 1
			Honor = Honor + 1
			Justice = Justice + 1

#------------------------------------------------------------------------------------------------------------------------------------------------
