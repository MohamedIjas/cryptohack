# Importing the required libraries
from sympy.ntheory.modular import crt  # For solving the Chinese Remainder Theorem (CRT)
from itertools import combinations     # To generate combinations of moduli and ciphertexts
from gmpy2 import iroot               # To compute integer cube roots

# Input: List of RSA moduli (N) and corresponding ciphertexts (C)
N = [
    14528915758150659907677315938876872514853653132820394367681510019000469589767908107293777996420037715293478868775354645306536953789897501630398061779084810058931494642860729799059325051840331449914529594113593835549493208246333437945551639983056810855435396444978249093419290651847764073607607794045076386643023306458718171574989185213684263628336385268818202054811378810216623440644076846464902798568705083282619513191855087399010760232112434412274701034094429954231366422968991322244343038458681255035356984900384509158858007713047428143658924970374944616430311056440919114824023838380098825914755712289724493770021,
    20463913454649855046677206889944639231694511458416906994298079596685813354570085475890888433776403011296145408951323816323011550738170573801417972453504044678801608709931200059967157605416809387753258251914788761202456830940944486915292626560515250805017229876565916349963923702612584484875113691057716315466239062005206014542088484387389725058070917118549621598629964819596412564094627030747720659155558690124005400257685883230881015636066183743516494701900125788836869358634031031172536767950943858472257519195392986989232477630794600444813136409000056443035171453870906346401936687214432176829528484662373633624123,
    19402640770593345339726386104915705450969517850985511418263141255686982818547710008822417349818201858549321868878490314025136645036980129976820137486252202687238348587398336652955435182090722844668488842986318211649569593089444781595159045372322540131250208258093613844753021272389255069398553523848975530563989367082896404719544411946864594527708058887475595056033713361893808330341623804367785721774271084389159493974946320359512776328984487126583015777989991635428744050868653379191842998345721260216953918203248167079072442948732000084754225272238189439501737066178901505257566388862947536332343196537495085729147,
    12005639978012754274325188681720834222130605634919280945697102906256738419912110187245315232437501890545637047506165123606573171374281507075652554737014979927883759915891863646221205835211640845714836927373844277878562666545230876640830141637371729405545509920889968046268135809999117856968692236742804637929866632908329522087977077849045608566911654234541526643235586433065170392920102840518192803854740398478305598092197183671292154743153130012885747243219372709669879863098708318993844005566984491622761795349455404952285937152423145150066181043576492305166964448141091092142224906843816547235826717179687198833961,
    17795451956221451086587651307408104001363221003775928432650752466563818944480119932209305765249625841644339021308118433529490162294175590972336954199870002456682453215153111182451526643055812311071588382409549045943806869173323058059908678022558101041630272658592291327387549001621625757585079662873501990182250368909302040015518454068699267914137675644695523752851229148887052774845777699287718342916530122031495267122700912518207571821367123013164125109174399486158717604851125244356586369921144640969262427220828940652994276084225196272504355264547588369516271460361233556643313911651916709471353368924621122725823,
    25252721057733555082592677470459355315816761410478159901637469821096129654501579313856822193168570733800370301193041607236223065376987811309968760580864569059669890823406084313841678888031103461972888346942160731039637326224716901940943571445217827960353637825523862324133203094843228068077462983941899571736153227764822122334838436875488289162659100652956252427378476004164698656662333892963348126931771536472674447932268282205545229907715893139346941832367885319597198474180888087658441880346681594927881517150425610145518942545293750127300041942766820911120196262215703079164895767115681864075574707999253396530263,
    19833203629283018227011925157509157967003736370320129764863076831617271290326613531892600790037451229326924414757856123643351635022817441101879725227161178559229328259469472961665857650693413215087493448372860837806619850188734619829580286541292997729705909899738951228555834773273676515143550091710004139734080727392121405772911510746025807070635102249154615454505080376920778703360178295901552323611120184737429513669167641846902598281621408629883487079110172218735807477275590367110861255756289520114719860000347219161944020067099398239199863252349401303744451903546571864062825485984573414652422054433066179558897
]

C = [
    6965891612987861726975066977377253961837139691220763821370036576350605576485706330714192837336331493653283305241193883593410988132245791554283874785871849223291134571366093850082919285063130119121338290718389659761443563666214229749009468327825320914097376664888912663806925746474243439550004354390822079954583102082178617110721589392875875474288168921403550415531707419931040583019529612270482482718035497554779733578411057633524971870399893851589345476307695799567919550426417015815455141863703835142223300228230547255523815097431420381177861163863791690147876158039619438793849367921927840731088518955045807722225,
    5109363605089618816120178319361171115590171352048506021650539639521356666986308721062843132905170261025772850941702085683855336653472949146012700116070022531926476625467538166881085235022484711752960666438445574269179358850309578627747024264968893862296953506803423930414569834210215223172069261612934281834174103316403670168299182121939323001232617718327977313659290755318972603958579000300780685344728301503641583806648227416781898538367971983562236770576174308965929275267929379934367736694110684569576575266348020800723535121638175505282145714117112442582416208209171027273743686645470434557028336357172288865172,
    5603386396458228314230975500760833991383866638504216400766044200173576179323437058101562931430558738148852367292802918725271632845889728711316688681080762762324367273332764959495900563756768440309595248691744845766607436966468714038018108912467618638117493367675937079141350328486149333053000366933205635396038539236203203489974033629281145427277222568989469994178084357460160310598260365030056631222346691527861696116334946201074529417984624304973747653407317290664224507485684421999527164122395674469650155851869651072847303136621932989550786722041915603539800197077294166881952724017065404825258494318993054344153,
    1522280741383024774933280198410525846833410931417064479278161088248621390305797210285777845359812715909342595804742710152832168365433905718629465545306028275498667935929180318276445229415104842407145880223983428713335709038026249381363564625791656631137936935477777236936508600353416079028339774876425198789629900265348122040413865209592074731028757972968635601695468594123523892918747882221891834598896483393711851510479989203644477972694520237262271530260496342247355761992646827057846109181410462131875377404309983072358313960427035348425800940661373272947647516867525052504539561289941374722179778872627956360577,
    8752507806125480063647081749506966428026005464325535765874589376572431101816084498482064083887400646438977437273700004934257274516197148448425455243811009944321764771392044345410680448204581679548854193081394891841223548418812679441816502910830861271884276608891963388657558218620911858230760629700918375750796354647493524576614017731938584618983084762612414591830024113057983483156974095503392359946722756364412399187910604029583464521617256125933111786441852765229820406911991809039519015434793656710199153380699319616440732856921112392626811356277121265923912898431838658040297041857870273880843644826094799257485,
    2392253124263445297958454066428821648055709393681945336597584425066248906101869343484340385727352545127082358183603107990127782666115838238410132680930808760286469243590858874400877122255620312674049874631742743285866044541358834237265147232438537304138679722142679152506111177317338825961206647402362655809938235666354501456756806144645762485929678875941313799707418726119322635146352050622380670670341920860545284606813740912854793336014395790975727723744289906562571197217219017164674820056100902944817873155263023701017386302013229300129927745182618842822457444118942162087958093398430977368081367164812169313469,
    3186036562282656235094763004964014854034580701778941663421693774937395865796763256339396879613520718256189307351163270443705989292369292774891477813192637270154907955370725771963252575068042564414083544025027498973634874002074007751892242060160831431495295122563794779421165713577828962120041034841041232245508760132519312519878823251121824774379929908615510841612953374118334998414923481262432051594348893663306055366393902619842372071738059708552534919223113883356702495703341253991027065721696047401880521425987594528914733170185997368105641741984773135530354783986267273875573889789308323663350859166433114379141
]

# Iterating over all combinations of 3 moduli and their corresponding ciphertexts
for n in combinations(range(7), 3):  # Select indices of three moduli and ciphertexts
    # Extract the corresponding moduli and ciphertexts for the current combination
    n1, n2, n3 = N[n[0]], N[n[1]], N[n[2]]
    c1, c2, c3 = C[n[0]], C[n[1]], C[n[2]]

    # Solve the Chinese Remainder Theorem for the three selected systems
    x, _ = crt([n1, n2, n3], [c1, c2, c3])

    # Extract the integer cube root of x
    m, exact = iroot(x, 3)  # Returns the cube root and whether the root is exact

    # If the cube root is valid (exact), check the decoded message
    if exact:
        try:
            # Decode the integer message as bytes and convert to a string
            decoded_message = bytes.fromhex(hex(m)[2:]).decode()

            # Check if the decoded message contains the target substring
            if 'crypto' in decoded_message:
                print("Decoded Message:", decoded_message)
                break  # Exit the loop if the message is successfully decoded
        except Exception:
            # Handle potential decoding errors (e.g., invalid UTF-8 sequences)
            continue