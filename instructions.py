class InstructionsHandler:
    def __init__(self):
        self.ate = {}
        self.atsc = {}
        self.aspe = {}
        self.aooe = {}
        self.aope = {}
        self.aoste = {}

    def load_instruction_set1(self, ):

        ################################# ATE #################################

        self.ate['bos_instruct1'] = """Definition: The output will be the aspects which have an associated opinion that are extracted from the input text. In cases where the aspects are implicit, the output should be null.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features, iChat, Photobooth, garage band
        Now complete the following example-
        input: """

        self.ate['bos_instruct2'] = """Definition: The output will be the aspects which have an associated opinion that are extracted from the input text. In cases where the aspects are implicit, the output should be null.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food, menu, service, setting
        Now complete the following example-
        input: """
        self.ate['delim_instruct'] = ''
        self.ate['eos_instruct'] = ' \noutput:'

        ################################# ATSC #################################

        self.atsc['bos_instruct1'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. 
        For aspects which are classified as null, you need to find the sentiment for the implicit aspect.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life. The aspect is battery life.
        output: positive
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!. The aspect is garage band.
        output: positive
        Now complete the following example-
        input: """
        
        self.atsc['bos_instruct2'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. 
        For aspects which are classified as null, you need to find the sentiment for the implicit aspect.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored. The aspect is menu.
        output: positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting. The aspect is food.
        output: positive
        Now complete the following example-
        input: """
        self.atsc['delim_instruct'] = ' The aspect is '
        self.atsc['eos_instruct'] = '.\noutput:'

        ################################# ASPE #################################

        self.aspe['bos_instruct1'] = """Definition: The output will be the aspects and the aspects sentiment polarity. In cases where the aspect is implicit, the output should be null:<polarity> where <polarity> represents the sentiment polarity.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:positive, 
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features:positive, iChat:positive, Photobooth:positive, garage band:positive
        Now complete the following example-
        input: """
        
        self.aspe['bos_instruct2'] = """Definition: The output will be the aspects and the aspects sentiment polarity. In cases where the aspect is implicit, the output should be null:<polarity> where <polarity> represents the sentiment polarity.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu:positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food:positive, menu:positive, service:positive, setting:positive
        Now complete the following example-
        input: """
        self.aspe['delim_instruct'] = ''
        self.aspe['eos_instruct'] = ' \noutput:'

        ################################# AOOE #################################

        self.aooe['bos_instruct1'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. The opinion term might be "null" for the implicit opinion. For aspects which are classified as null, you need to find the opinion term for the implicit aspect.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Now complete the following example-
        input: """
        
        self.aooe['bos_instruct2'] = """Definition: The output will be the opinion/describing word for the aspect term in the sentence. The opinion term might be "null" for the implicit opinion. For aspects which are classified as null, you need to find the opinion term for the implicit aspect.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery . The aspect term is delivery.
        output: rough
        Positive example 2- 
        input: At the end you 're left with a mild broth with noodles that you can slurp out of a cup . The aspect term is broth with noodles.
        output: mild
        Now complete the following example-
        input: """
        self.aooe['delim_instruct'] = ' The aspect is '
        self.aooe['eos_instruct'] = '.\noutput:'

        ################################# AOPE #################################

        self.aope['bos_instruct1'] = """Definition: The output will be the aspects and the corresponding opinion/describing terms. The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output should be null:<opinion> with <opinion> representing the opinion term.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high, GUI:killer, applications:good, use:easy 
        Now complete the following example-
        input: """
        
        self.aope['bos_instruct2'] = """Definition: The output will be the aspects and the aspects sentiment polarity. The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output should be null:<opinion> with <opinion> representing the opinion term.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious, money:little
        Now complete the following example-
        input: """
        self.aope['delim_instruct'] = ''
        self.aope['eos_instruct'] = ' \noutput:'

        ################################# AOSTE #################################

        self.aoste['bos_instruct1'] = """Definition: The output will be the aspects the corresponding opinion/describing terms and the sentiment polarity (positive, negative) of the opinion term . The opinion term might be "null" for the implicit opinion. In cases where there are no aspects the output should be null:<opinion>:<polarity> with <opinion> representing the opinion term and <polarity> representing the sentiment polarity.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good:positive 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high:positive, GUI:killer:positive, applications:good:positive, use:easy:positive 
        Now complete the following example-
        input: """
        
        self.aoste['bos_instruct2'] = """Definition: The output will be the aspects the corresponding opinion/describing terms and the sentiment polarity (positive, negative) of the opinion term . The opinion term might be "null" for the implicit opinion. In cases where there are no aspects the output should be null:<opinion>:<polarity> with <opinion> representing the opinion term and <polarity> representing the sentiment polarity.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough:positive
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious:positive, money:little:positive
        Now complete the following example-
        input: """
        self.aoste['delim_instruct'] = ''
        self.aoste['eos_instruct'] = ' \noutput:'


    def load_instruction_set2(self, ):

        ################################# ATE #################################

        self.ate['bos_instruct1'] = """Definition: The output will be the aspects which have an associated opinion that are extracted from the input text. In cases where the aspect term is implicit, the output should be null.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features, iChat, Photobooth, garage band
        Negative example 1-
        input: Speaking of the browser, it too has problems.
        output: browser
        Negative example 2-
        input: The keyboard is too slick.
        output: keyboard
        Now complete the following example-
        input: """
        
        self.ate['bos_instruct2'] = """Definition: The output will be the aspects which have an associated opinion that are extracted from the input text. In cases where the aspect term is implicit, the output should be null.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food, menu, service, setting
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it.
        output: toast, mayonnaise, bacon, ingredients, plate
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches.
        output: seats
        Now complete the following example-
        input: """
        self.ate['delim_instruct'] = ''
        self.ate['eos_instruct'] = ' \noutput:'

        ################################# ATSC #################################

        self.atsc['bos_instruct1'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. For aspects which are classified as null, it means that the aspect is implicit.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life. The aspect is battery life.
        output: positive
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!. The aspect is garage band.
        output: positive
        Negative example 1-
        input: Speaking of the browser, it too has problems. The aspect is browser.
        output: negative
        Negative example 2-
        input: The keyboard is too slick. The aspect is keyboard.
        output: negative
        Now complete the following example-
        input: """
        
        self.atsc['bos_instruct2'] = """Definition: The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. For aspects which are classified as null, it means that the aspect is implicit.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored. The aspect is menu.
        output: positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting. The aspect is food.
        output: positive
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it. The aspect is toast.
        output: negative
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches. The aspect is seats.
        output: negative
        Now complete the following example-
        input: """
        self.atsc['delim_instruct'] = ' The aspect is '
        self.atsc['eos_instruct'] = '.\noutput:'

        ################################# ASPE #################################

        self.aspe['bos_instruct1'] = """Definition: The output will be the aspects and the aspects sentiment polarity. In cases where the aspect term is implicit, the output should be null:<polarity> where <polarity> is the sentiment polarity of the implicit aspect.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:positive, 
        Positive example 2-
        input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
        output: features:positive, iChat:positive, Photobooth:positive, garage band:positive
        Negative example 1-
        input: Speaking of the browser, it too has problems.
        output: browser:negative
        Negative example 2-
        input: The keyboard is too slick.
        output: keyboard:negative
        Now complete the following example-
        input: """
        
        self.aspe['bos_instruct2'] = """Definition: The output will be the aspects and the aspects sentiment polarity. In cases where the aspect term is implicit, the output should be null:<polarity> where <polarity> is the sentiment polarity of the implicit aspect.
        Positive example 1-
        input: With the great variety on the menu , I eat here often and never get bored.
        output: menu:positive
        Positive example 2- 
        input: Great food, good size menu, great service and an unpretensious setting.
        output: food:positive, menu:positive, service:positive, setting:positive
        Negative example 1-
        input: They did not have mayonnaise, forgot our toast, left out ingredients (ie cheese in an omelet), below hot temperatures and the bacon was so over cooked it crumbled on the plate when you touched it.
        output: toast:negative, mayonnaise:negative, bacon:negative, ingredients:negative, plate:negative
        Negative example 2-
        input: The seats are uncomfortable if you are sitting against the wall on wooden benches.
        output: seats:negative
        Now complete the following example-
        input: """
        self.aspe['delim_instruct'] = ''
        self.aspe['eos_instruct'] = ' \noutput:'

        ################################# AOOE #################################

        self.aooe['bos_instruct1'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output is null.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Negative example 1-
        input: One night I turned the freaking thing off after using it , the next day I turn it on , no GUI , screen all dark , power light steady , hard drive light steady and not flashing as it usually does . The aspect is GUI.
        output: no
        Negative example 2-
        input: I can barely use any usb devices because they will not stay connected properly . The aspect is usb devices.
        output: not stay connected properly
        Now complete the following example-
        input: """

        self.aooe['bos_instruct2'] = """Definition: The output will be the opinion/describing word of the aspect terms in the sentence. The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output is null.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life . The aspect is battery life.
        output: good
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous. The aspect is GUI.
        output: killer
        Negative example 1-
        input: The menu is very limited - i think we counted 4 or 5 entrees . The aspect is menu.
        output: limited
        Negative example 2-
        input: The strong scents coming from the left and right of me negatively affected my taste buds . The aspect is scents.
        output: strong
        Now complete the following example-
        input: """
        self.aooe['delim_instruct'] = ' The aspect is '
        self.aooe['eos_instruct'] = '.\noutput:'

        ################################# AOPE #################################

        self.aope['bos_instruct1'] = """Definition: The output will be the aspects and the corresponding opinion/describing terms. In cases where the aspect term is implicit, the output should be null:<opinion> where <opinion> is the opinion/describing word of the implicit aspect.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high, GUI:killer, applications:good, use:easy
        Negative example 1-
        input: A month or so ago , the freaking motherboard just died .
        output: motherboard:freaking, motherboard:freaking
        Negative example 2-
        input: I had always used PCs and been constantly frustrated by the crashing and the poorly designed operating systems that were never very intuitive .
        output: operating systems:poorly designed, operating systems:intuitive
        Now complete the following example-
        input: """
        
        self.aope['bos_instruct2'] = """Definition: The output will be the aspects and the aspects sentiment polarity. In cases where the aspect term is implicit, the output should be null:<opinion> where <opinion> is the opinion/describing word of the implicit aspect.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious, money:little
        Negative example 1-
        input: From the terrible service , to the bland food , not to mention the unaccommodating managers , the overall experience was horrible .
        output: service:terrible, food:bland, managers:unaccommodating
        Negative example 2- 
        input: I had the Pad Thai and the noodles were sticky .
        output: Pad Thai:sticky, noodles:sticky
        Now complete the following example-
        input: """
        self.aope['delim_instruct'] = ''
        self.aope['eos_instruct'] = ' \noutput:'

        ################################# AOSTE #################################

        self.aoste['bos_instruct1'] = """Definition: The output will be the aspects the corresponding opinion/describing terms and the sentiment polarity (positive, negative) of the opinion term . The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output should be null:<opinion>:<polarity> with <opinion> representing the opinion term and <polarity> representing the sentiment polarity.
        Positive example 1-
        input: I charge it at night and skip taking the cord with me because of the good battery life.
        output: battery life:good:positive 
        Positive example 2-
        input: it is of high quality , has a killer GUI , is extremely stable , is highly expandable , is bundled with lots of very good applications , is easy to use , and is absolutely gorgeous.
        output: quality:high:positive, GUI:killer:positive, applications:good:positive, use:easy:positive
        Negative example 1-
        input: A month or so ago , the freaking motherboard just died .
        output: motherboard:freaking:negative, motherboard:freaking:negative
        Negative example 2-
        input: I had always used PCs and been constantly frustrated by the crashing and the poorly designed operating systems that were never very intuitive .
        output: operating systems:poorly designed, operating systems:intuitive
        Now complete the following example-
        input: """
        
        self.aoste['bos_instruct2'] = """Definition: The output will be the aspects the corresponding opinion/describing terms and the sentiment polarity (positive, negative) of the opinion term . The opinion term might be "null" for the implicit opinion. In cases where the aspect is implicit, the output should be null:<opinion>:<polarity> with <opinion> representing the opinion term and <polarity> representing the sentiment polarity.
        Positive example 1-
        input: Faan 's got a great concept but a little rough on the delivery .
        output: delivery:rough:positive
        Positive example 2- 
        input: I just wonder how you can have such a delicious meal for such little money .
        output: meal:delicious:positive, money:little:positive
        Negative example 1-
        input: From the terrible service , to the bland food , not to mention the unaccommodating managers , the overall experience was horrible .
        output: service:terrible:negative, food:bland:negative, managers:unaccommodating:negative
        Negative example 2- 
        input: I had the Pad Thai and the noodles were sticky .
        output: Pad Thai:sticky:negative, noodles:sticky:negative
        Now complete the following example-
        input: """
        self.aoste['delim_instruct'] = ''
        self.aoste['eos_instruct'] = ' \noutput:'