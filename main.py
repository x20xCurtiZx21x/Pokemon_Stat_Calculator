#main.py 

from stat_calc import Stat_Calc

def pokemon_list_create(file_name):

    pokemon_list = []

    temp_file = open(file_name, 'r')

    for line in temp_file:

        new_line = line.strip('\n')

        pokemon_list.append(new_line.split('\t'))

    temp_file.close()

    return pokemon_list

def nature_list_create(file_name):

    nature_list = []

    nature_file = open(file_name, 'r')

    for line in nature_file:

        new_line = line.strip('\n')

        nature_list.append(new_line.split('\t'))

    nature_file.close()

    return nature_list

def nature_mul(nature, nature_list):

    list_count = 0

    for item in nature_list:

        if nature.lower() == item[0]:

            list_count += 1

            nature_nums = [float(item[1]), float(item[2]), float(item[3]), float(item[4]), float(item[5])]

    if list_count == 1:

        return nature_nums

    else:

        raise IndexError

def ev_check(hp, atk, dfn, sp_atk, sp_dfn, spd):

    if hp + atk + dfn + sp_atk + sp_dfn + spd <= 510:

         return True

    else:

        return False

def iv_check(hp, atk, dfn, sp_atk, sp_dfn, spd):

    if 0 < hp <= 31 and 0 < atk <= 31 and 0 < dfn <= 31 and 0 < sp_atk <= 31 and 0 < sp_dfn <= 31 and 0 < spd <= 31:

        return True

    else:

        return False

def main():

    count = 0

    nature_list = nature_list_create('natures.txt')

    pokemon_list = pokemon_list_create('pokemon.txt')

    print("Welcome to Chase's Stat Calculator!")

    while count == 0:

        print('')

        print('Select an option:')

        print('1) Calculate new Pokemon')

        print('2) Retrieve a saved spread')

        print('3) Exit')

        print('')

        try:

            user_choice = int(input('Enter your choice: '))

        except:

            user_choice = 0

        if user_choice == 1:

            print('')

            print('Enter the name the Pokemon you wish to Calculate.')

            print("Whenever you type the Pokemon's name, make sure to include any special characters.")

            print("If you want a specfic form, put a SPACE after the name and put the name of the form")

            name = input('in (): ')

            print('')

            name_count = 0

            for item in pokemon_list:

                if name.lower() == item[0].lower():

                    name_count += 1

                    pokemon_name = item[0]

                    pokemon_selected = Stat_Calc(item[1], item[2], item[3], item[4], item[5], item[6])

            if name_count == 1:

                try:

                    print('Now enter the level and Nature of the Pokemon!(Max level is 100)')

                    lvl = int(input('Enter the Level of the Pokemon: '))

                    nature = input('Enter the nature of the Pokemon: ')

                    nature_buffs = nature_mul(nature, nature_list)

                    if lvl > 0 and lvl <= 100:

                        print('')

                        print('Now enter the EV spread of the Pokemon!(Max is 252 per stat with the total of 510)')

                        hp_ev = int(input('Enter the HP EVs of the Pokemon: '))

                        atk_ev = int(input('Enter the ATTACK EVs of the Pokemon: '))

                        dfn_ev = int(input('Enter the DEFENSE EVs of the Pokemon: '))

                        sp_atk_ev = int(input('Enter the SPECIAL ATTACK EVs of the Pokemon: '))

                        sp_dfn_ev = int(input('Enter the SPECIAL DEFENSE EVs of the Pokemon: '))

                        spd_ev = int(input('Enter the SPEED EVs of the Pokemon: '))

                        print('')

                        print('Finaly, enter the IVs of the Pokemon!(Max is 31 per stat)')

                        hp_iv = int(input('Enter the HP IVs of the Pokemon: '))

                        atk_iv = int(input('Enter the ATTACK IVs of the Pokemon: '))

                        dfn_iv = int(input('Enter the DEFENSE IVs of the Pokemon: '))

                        sp_atk_iv = int(input('Enter the SPECIAL ATTACK IVs of the Pokemon: '))

                        sp_dfn_iv = int(input('Enter the SPECIAL DEFENSE IVs of the Pokemon: '))

                        spd_iv = int(input('Enter the SPEED IVs of the Pokemon: '))

                        print('')

                        if ev_check(hp_ev, atk_ev, dfn_ev, sp_atk_ev, sp_dfn_ev, spd_ev) and iv_check(hp_iv, atk_iv, dfn_iv, sp_atk_iv, sp_dfn_iv, spd_iv):

                            final_hp = pokemon_selected.hp_calc(hp_iv, hp_ev, lvl)

                            final_atk = pokemon_selected.decide_stat('attack', atk_iv, atk_ev, lvl, nature_buffs[0])

                            final_dfn = pokemon_selected.decide_stat('defense', dfn_iv, dfn_ev, lvl, nature_buffs[1])

                            final_sp_atk = pokemon_selected.decide_stat('special attack', sp_atk_iv, sp_atk_ev, lvl, nature_buffs[2])

                            final_sp_dfn = pokemon_selected.decide_stat('special defense', sp_dfn_iv, sp_dfn_ev, lvl, nature_buffs[3])

                            final_spd = pokemon_selected.decide_stat('speed', spd_iv, spd_ev, lvl, nature_buffs[4])

                            print(f'For {pokemon_name} with the Level, Nature, EVs, and IVs given:')

                            print(f'HP: {final_hp}')

                            print(f'Attack: {final_atk}')

                            print(f'Defense: {final_dfn}')

                            print(f'Special Attack: {final_sp_atk}')

                            print(f'Special Defense: {final_sp_dfn}')

                            print(f'Speed: {final_spd}')

                            print('')

                            save = input('Would you like to save this spread?(Y/N): ')

                            if save.upper() == 'Y':

                                save_file = open('stored_setups.txt', 'a')

                                line_count = 0

                                try:

                                    for line in save_file:

                                        line_count += 1

                                except:

                                    line_count = 0

                                line_count += 1

                                save_file.write(f'{name}\t{lvl}\t{nature}\t{hp_ev}\t{atk_ev}\t{dfn_ev}\t{sp_atk_ev}\t{sp_dfn_ev}\t{spd_ev}\t{hp_iv}\t{atk_iv}\t{dfn_iv}\t{sp_atk_iv}\t{sp_dfn_iv}\t{spd_iv}\t{final_hp}\t{final_atk}\t{final_dfn}\t{final_sp_atk}\t{final_sp_dfn}\t{final_spd}\n')

                                save_file.close()

                                print(f'Saved to slot {line_count}')

                        else:

                            print("Sorry, incorrect Evs and Ivs inputted")

                    else:

                        print('Sorry, Invalid level was given') 

                except:

                    print("Sorry, Nature doesn't exist or typed incorrectly")

            else:

                print('Sorry, there is no such Pokemon')

        elif user_choice == 2:

            print('')

            try:

                user_choice = int(input('Which saved slot would you like to retrieve?: '))

                save_file = open('stored_setups.txt', 'r')

                line_count = 0

                for line in save_file:

                    line_count += 1

                save_file.close()

                print('')

                if line_count == 0:

                    print('There are no saved builds!')

                elif user_choice <= line_count and user_choice > 0:

                    save_file = open('stored_setups.txt', 'r')

                    line_count = 0

                    save = []

                    for line in save_file:

                        line_count += 1

                        if line_count == user_choice:

                            discovered_line = line.strip('\n')

                            save.append(discovered_line.split('\t'))

                    save_file.close()

                    print(f'Pokemon: {save[0][0]} Level: {save[0][1]} Nature: {save[0][2]}')

                    print('')

                    print('EVS:')

                    print(f'HP: {save[0][3]} ATK: {save[0][4]} DFN: {save[0][5]} SPATK: {save[0][6]} SPDFN: {save[0][7]} SPD: {save[0][8]}')

                    print('')

                    print('IVS:')

                    print(f'HP: {save[0][9]} ATK: {save[0][10]} DFN: {save[0][11]} SPATK: {save[0][12]} SPDFN: {save[0][13]} SPD: {save[0][14]}')

                    print('')

                    print('Final Stats:')

                    print(f'HP: {save[0][15]} ATK: {save[0][16]} DFN: {save[0][17]} SPATK: {save[0][18]} SPDFN: {save[0][19]} SPD: {save[0][20]}')
                        
                else:

                    print("Sorry, that isn't a valid slot number")

            except:

                print('')

                print('Sorry, not a valid option')

        elif user_choice == 3:

            count = 1

            print('')

            print('See ya!')

        else:

            print('')

            print('Sorry, invalid option')

main()