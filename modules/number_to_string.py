def nepali_number_to_devnagari(num='०', returnNumberList=True, returnValue=True):
    if not returnNumberList and not returnValue:
        return "Nothing to be done!"
    #Create number list from 0 - 99
    nepaliNumeralsList = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
    if returnNumberList and not returnValue:
        return nepaliNumeralsList
    numbers = []
    for i in range(1, len(nepaliNumeralsList)):
        for j in range(0, len(nepaliNumeralsList)):
            numbers.append(nepaliNumeralsList[i]+nepaliNumeralsList[j])
    nepaliNumerals = nepaliNumeralsList + numbers

    # Create devanagari number list from 0 - 99
    nepaliNumeralString = [
        "शुन्य", "एक", "दुई", "तीन", "चार", "पाँच", "छ", "सात", "आठ", "नौ", 
        "दश", "एघार","बाह्र", "तेह्र", 'चौध', 'पन्ध्र', 'सोह्र', 'सत्र', 'अठार', 'उन्नाइस', 
        'विस', 'एक्काइस', 'बाइस', 'तेईस', 'चौविस', 'पच्चिस', 'छब्बिस', 'सत्ताइस', 'अठ्ठाईस', 'उनन्तिस', 
        'तिस', 'एकत्तिस', 'बत्तिस', 'तेत्तिस', 'चौँतिस', 'पैँतिस', 'छत्तिस', 'सैँतीस', 'अठतीस', 'उनन्चालीस', 
        'चालीस', 'एकचालीस', 'बयालीस', 'त्रियालीस', 'चवालीस', 'पैँतालीस', 'छयालीस', 'सच्चालीस', 'अठचालीस', 'उनन्चास', 
        'पचास', 'एकाउन्न', 'बाउन्न', 'त्रिपन्न', 'चउन्न', 'पचपन्न', 'छपन्न', 'सन्ताउन्न', 'अन्ठाउन्न', 'उनन्साठी', 
        'साठी', 'एकसट्ठी', 'बयसट्ठी', 'त्रिसट्ठी', 'चौंसट्ठी', 'पैंसट्ठी', 'छयसट्ठी', 'सतसट्ठी', 'अठसट्ठी', 'उनन्सत्तरी', 
        'सत्तरी', 'एकहत्तर', 'बहत्तर', 'त्रिहत्तर', 'चौहत्तर', 'पचहत्तर', 'छयहत्तर', 'सतहत्तर', 'अठहत्तर', 'उनासी', 
        'असी', 'एकासी', 'बयासी', 'त्रियासी', 'चौरासी', 'पचासी', 'छयासी', 'सतासी', 'अठासी', 'उनान्नब्बे', 
        'नब्बे', 'एकान्नब्बे', 'बयानब्बे', 'त्रियान्नब्बे', 'चौरान्नब्बे', 'पन्चानब्बे', 'छयान्नब्बे', 'सन्तान्नब्बे', 'अन्ठान्नब्बे', 'उनान्सय'
        ]

    # Create dict using numbers to devnagarari
    numberToDevnagariTo99 = {}
    for i in range(0,len(nepaliNumeralString)):
        numberToDevnagariTo99[nepaliNumerals[i]] = nepaliNumeralString[i]

    # postion of 1 in 100, 1000,... places
    TensPlaces = ["सय", "हजार", "लाख", "करोड", "अर्ब", "खर्ब", "नील", "पद्म", "शंख"]
    tensplace = {}
    a=3 # starts from 00
    for i in range(0, len(TensPlaces)):
        if a>4:
            # removing 10 thousand and similar
            a = a + 1
        tensplace[a] = TensPlaces[i]
        a = a + 1
    
    # Start of conversion
    number_list = list(num)
    while number_list[0] == '०' and len(number_list)> 1:
        number_list.pop(0)
    num = "".join(number_list)
    length = len(number_list)
    name = []
    i = 0
    while(i<length):
        # loop starts
        position = length - i
        if position == 1:
            # if in first position
            name.append(numberToDevnagariTo99[num[i]])
            break
        elif position not in tensplace:
            # if not exactly on     100, 1000, place
            
            if numberToDevnagariTo99[num[i]] == "शुन्य":
                if numberToDevnagariTo99[num[i+1]] == "शुन्य":
                    # If there is no value is tens and ones part of any i.e thousanth part ie. 10 thousand
                    i = i + 2
                    continue
                # If there is no value is tens part but there is in ones part
                name.append(numberToDevnagariTo99[num[i+1]])
            else:
                # If there is value in both tens and onces part
                name.append(numberToDevnagariTo99[num[i]+num[i+1]])
            i = i + 1
            if position == 2:
                # If onces and tens of whole number is done then end execution
                break
            position = length - i
        else:
            if not numberToDevnagariTo99[num[i]] == "शुन्य":
                # In 100's place
                name.append(numberToDevnagariTo99[num[i]])   
                name.append(tensplace[position])
                i=i+1
                continue
        if position > 3:
            # for above 100's place
            name.append(tensplace[position])
        i = i + 1
    if returnNumberList and returnValue:
        return nepaliNumeralsList, " ".join(name)   # Join array as a string
    if not returnNumberList and returnValue:
        return " ".join(name)