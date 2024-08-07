letter =''' Dear <|Name|>,
           You are selected!
           <|Date|> '''

print(letter.replace("|Name|>" , "Arshoo ").replace("<|Date|>", "7 August 2024"))