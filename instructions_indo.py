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

        self.ate['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be the aspects which have an associated opinion that are extracted from the input text. In cases where the aspect term is implicit, the output should be null.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar .
        output: null
        Positive example -
        input: kamarnya bersih, saya check-in malam hari. 
        output: kamarnya
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala .
        output: kamar mandi, showernya
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman .
        output: suasana, suasana
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel .
        output: bau kamar, lemari, wastafel
        Now complete the following example-
        input: """

        self.ate['delim_instruct'] = ''
        self.ate['eos_instruct'] = ' \noutput:'

        ################################# ATSC #################################

        self.atsc['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be 'positive' if the aspect identified in the sentence contains a positive sentiment. If the sentiment of the identified aspect in the input is negative the answer will be 'negative'. For aspects which are classified as null, it means that the aspect is implicit.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar . The aspect is null.
        output: negative
        Positive example -
        input: kamarnya bersih, saya check-in malam hari. The aspect is kamarnya.
        output: positive
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala . The aspect is kamar mandi.
        output: negative
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman . The aspect is suasana.
        output: positive
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel . The aspect is lemari.
        output: negative
        Now complete the following example-
        input: """

        self.atsc['delim_instruct'] = ' The aspect is '
        self.atsc['eos_instruct'] = '.\noutput:'

        ################################# ASPE #################################

        self.aspe['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be the aspects and the aspects sentiment polarity. In cases where the aspect term is implicit, the output should be null:<polarity> where <polarity> is the sentiment polarity of the implicit aspect.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar .
        output: null:negative
        Positive example -
        input: kamarnya bersih, saya check-in malam hari.
        output: kamarnya:positive
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala .
        output: kamar mandi:negative, showernya:negative
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman .
        output: suasana:positive, suasana:positive
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel .
        output: bau kamar:negative, lemari:negative, wastafel:negative
        Now complete the following example-
        input: """
        self.aspe['delim_instruct'] = ''
        self.aspe['eos_instruct'] = ' \noutput:'

        ################################# AOOE #################################

        self.aooe['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be the opinion/describing word of the aspect terms in the sentence. In cases where the aspect is implicit, find the opinion relating to this implicit aspect.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar . The aspect is null.
        output: tidak sesuai yang ada di gambar
        Positive example -
        input: kamarnya bersih, saya check-in malam hari. The aspect is kamarnya.
        output: bersih
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala . The aspect is kamar mandi.
        output: perlu ditingkatkan lagi
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman . The aspect is suasana.
        output: tenang
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel . The aspect is lemari.
        output: kurang wangi
        Now complete the following example-
        input: """
        self.aooe['delim_instruct'] = ' The aspect is '
        self.aooe['eos_instruct'] = '.\noutput:'

        ################################# AOPE #################################

        self.aope['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be the aspects and the corresponding opinion/describing terms. In cases where the aspect term is implicit, the output should be null:<opinion> where <opinion> is the opinion/describing word of the implicit aspect.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar .
        output: null:tidak sesuai yang ada di gambar
        Positive example -
        input: kamarnya bersih, saya check-in malam hari.
        output: kamarnya:bersih
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala .
        output: kamar mandi:perlu ditingkatkan lagi, showernya:kurang nyala
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman .
        output: suasana:tenang, suasana:nyaman
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel .
        output: bau kamar:kurang wangi, lemari:kurang wangi, wastafel:kurang wangi
        Now complete the following example-
        input: """
        self.aope['delim_instruct'] = ''
        self.aope['eos_instruct'] = ' \noutput:'

        ################################# AOSTE #################################

        self.aoste['bos_instruct1'] = """Definition: You will be given an Indonesian sentence. The output will be the aspects the corresponding opinion/describing terms and the sentiment polarity (positive and negative) of the opinion term . In cases where the aspect is implicit, the output should be null:<opinion>:<polarity> with <opinion> representing the opinion term and <polarity> representing the sentiment polarity.
        Implicit aspect example -
        input: tidak sesuai yang ada di gambar .
        output: null:tidak sesuai yang ada di gambar:negative
        Positive example -
        input: kamarnya bersih, saya check-in malam hari.
        output: kamarnya:bersih:positive
        Negative example -
        input: kamar mandi perlu ditingkatkan lagi , showernya kurang nyala .
        output: kamar mandi:perlu ditingkatkan lagi:negative, showernya:kurang nyala:positive
        One aspect multiple opinions example -
        input: suasana tenang dan nyaman .
        output: suasana:tenang:positive, suasana:nyaman:positive
        One opinion multiple aspects example -
        input: bau kamar kurang wangi terutama bagian lemari sama wastafel .
        output: bau kamar:kurang wangi:negative, lemari:kurang wangi:negative, wastafel:kurang wangi:negative
        Now complete the following example-
        input: """
        self.aoste['delim_instruct'] = ''
        self.aoste['eos_instruct'] = ' \noutput:'