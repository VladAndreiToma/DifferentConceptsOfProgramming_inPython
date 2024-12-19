def printCard( kind , suits ):
    width = 11   # the width in char characters
    height = 9   # the height in char characters
    total_top_border = ""
    total_bottom_border = ""
    total_tag_border = ""
    total_side_border = ""
    total_kind_top = ""
    total_kind_bottom = ""
    for i in range(1,len(kind)+1):   # kind and suits have the same length
        number = kind[i-1]
        card_tag = suits[i-1]
        card_type = ""
        if 2<= number <= 10:
            card_type += str(number)
        elif number == 11:
            card_type += "J"
        elif number == 12:
            card_type += "Q"
        elif number == 13:
            card_type += "K"
        elif number == 1:
            card_type += "A"
        else:
            card_type += " "
        part1_of_border = ""
        part2_of_border = ""
        side_border_with_tag = ""

        top_border = "╔" + "═" * (width - 2) + "╗"  # constructing top border with the special characters
        side_border = "║" + " " * (width - 2) + "║" # constructing side border with the special characters
        side_border_with_symbol = ""   # empty string ---- to be created the symbol with respect to the instructions given to the function
        if card_tag == "club":   # then clubs is wanted for the ACE
            side_border_with_symbol += "║" + " "*((width-2)//2) + "♣" + " "*((width-2)//2) + "║"
        elif card_tag == "diamond":  # diamond is wanted for the ACE
            side_border_with_symbol += "║" + " "*((width-2)//2) + "♦" + " "*((width-2)//2) + "║"
        elif card_tag == "heart":  # heart is wanted for the ACE
            side_border_with_symbol += "║" + " "*((width-2)//2) + "♥" + " "*((width-2)//2) + "║"
        elif card_tag == "spade":   # only spades is left for the ACE
            side_border_with_symbol += "║" + " "*((width-2)//2) + "♠" + " "*((width-2)//2) + "║"
        else:
            side_border_with_symbol += "║" + " "*((width-2)//2) + " " + " "*((width-2)//2) + "║"
        if card_type != "10":
            part1_of_border = "║" + " "
            part2_of_border = " " * (width - 4) + "║"
        else:
            part1_of_border = "║" + " "
            part2_of_border = " " * (width - 5) + "║"
        # reverse it to obtain the bottom one, the above defined string is the upper border tag
        bottom_border = "╚" + "═" * (width - 2) + "╝" # constructing the bottom border with special characters

        # at each step generate the borders with all the cards
        if i != len(kind):
            total_top_border += top_border + " "
            total_bottom_border += bottom_border + " "
            total_kind_top += part1_of_border + card_type + part2_of_border + " "
            total_kind_bottom += part2_of_border[::-1] + card_type + part1_of_border[::-1] + " "
        if i == len(kind):
            total_top_border += top_border
            total_side_border += side_border
            total_tag_border += side_border_with_symbol
            total_bottom_border += bottom_border
            total_kind_top += part1_of_border + card_type + part2_of_border
            total_kind_bottom += part2_of_border[::-1] + card_type + part1_of_border[::-1]
    print( total_top_border )
    print( total_kind_top )
    for _ in range((height-2)//2-1):
        print( total_side_border )
    print( total_tag_border )
    for _ in range((height-2)//2-1):
        print( total_side_border )
    print( total_kind_bottom )
    print( total_bottom_border )

printCard( [9,12,10] , ["diamond" , "spade" ,"club" ] )