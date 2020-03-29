# Results

### Genes
SPI-1 type III secretion system export apparatus proteins [Salmonella enterica]:

    SpaP
      - 99.55% match: MGNDISLIALLAFSTLLPFIIASGTCFVKFSIVFVMVRNALGLQQIPSNMTLNGVALLLSMFVMWPIMHDAYVYFEDEDVTFNDISSLSKHVDEGLDGYRDYLIKYSDRELVQFFENAQLKRQYGEETETVKRDKDEIEKPSIFALLPAYALSEIKSAFKIGFYLYLPFVVVDLVVSSVLLALGMMMMSPVTISTPIKLVLFVALDGWTLLSKGLILQYMDIAT
      - 100% match: MVRNALGLQQIPSNMTLNGVALLLSMFVMWPIMHDAYVYFEDEDVTFNDISSLSKHVDEGLDGYRDYLIKYSDRELVQFFENAQLKRQYGEETETVKRDKDEIEKPSIFALLPAYALSEIKSAFKIGFYLYLPFVVVDLVVSSVLLALGMMMMSPVTISTPIKLVLFVALDGWTLLSKGLILQYMDIAT
      
    SpaR
      - 99.62% match: MFYALYFEIHHLVASAALGFARVAPIFFFLPFLNSGVLSGAPRNAIIILVALGVWPHALNEAPPFLSVAMIPLVLQEAAVGVMLGCLLSWPFWVMHALGCIIDNQRGATLSSSIDPANGIDTSEMANFLNMFAAVVYLQNGGLVTMVDVLNKSYQLCDPMNECTPSLPPLLTFINQVAQNALVLASPVVLVLLLSEVFLGLLSRFAPQMNAFAISLTVKSGIAVLIMLLYFSPVLPDNVLRLSFQATGLSSWFYERGATHVLE
      
    SpaS
      - 100% match: MGIIKIIIADNFDQSMADYSLAVFGIGLKYLIPFMLLCLVCSALPALLQAGFVLATEALKPNLSALNPVEGAKKLFSMRTVKDTVKTLLYLSSFVVAAIICWKKYKVEIFSQLNGNIVGIAVIWRELLLALVLTCLACALIVLLLDAIAEYFLTMKDMKMDKEEVKREMKEQEGNPEVKSKRREVHMEILSEQVKSDIENSRLIVANPTHITIGIYFKPELMPIPMISVYETNQRALAVRAYAEKVGVPVIVDIKLARSLFKTHRRYDLVSLEEIDEVLRLLVWLEEVENAGKDVIQPQENEVRH
      - 99.72% match: MSSNKTEKPTKKRLEDSAKKGQSFKSKDLIIACLTLGGIAYLVSYGSFNEFMGIIKIIIADNFDQSMADYSLAVFGIGLKYLIPFMLLCLVCSALPALLQAGFVLATEALKPNLSALNPVEGAKKLFSMRTVKDTVKTLLYLSSFVVAAIICWKKYKVEIFSQLNGNIVGIAVIWRELLLALVLTCLACALIVLLLDAIAEYFLTMKDMKMDKEEVKREMKEQEGNPEVKSKRREVHMEILSEQVKSDIENSRLIVANPTHITIGIYFKPELMPIPMISVYETNQRALAVRAYAEKVGVPVIVDIKLARSLFKTHRRYDLVSLEEIDEVLRLLVWLEEVENAGKDVIQPQENEVRH

FliI/YscN family ATPase [Salmonella enterica]

    ATPase
      - 100% match: MGIFASAGCGKTMLMHMLIEQTEADVFVIGLIGERGREVTEFVDMLRASHKKEKCVLVFATSDFPSVDRCNAAQLATTVAEYFRDQGKRVVLFIDSMTRYARALRDVALASGERPARRGYPASVFDNLPRLLERPGATSEGSITAFYTVLLESEEEADPMADEIRSILDGHLYLSRKLAGQGHYPAIDVLKSVSRVFGQVTTPTHAEQASAVRKLMTRLEELQLFIDLGEYRPGENIDNDRAMQMRDSLKAWLCQPVAQYSSFDDTLSGMNAFADQN

### Purpose
From "The Structure and Function of Type III Secretion Systems" by Ryan Q. Notti and C. Erec Stebbins at the National Center of Biotechnology Information (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4804468/):
- "Type III secretion systems (T3SS) afford gram-negative bacteria a most intimate means of altering the biology of their eukaryotic hosts — the direct delivery of effector proteins from the bacterial cytoplasm to that of the eukaryote. This incredible biophysical feat is accomplished by nanosyringe “injectisomes,” which form a conduit across the three plasma membranes, peptidoglycan layer and extracellular space that form a barrier to the direct delivery of proteins from bacterium to host."
- "Interaction of chaperone-substrate complexes with the T3SS ATPase SctN causes the dechaperoning and unfolding of the substrate in an ATP hydrolysis-dependent fashion"

From "Bacterial type III secretion systems: specialized nanomachines for protein delivery into target cells" by Jorge E. Galán, Maria Lara-Tejero, Thomas C. Marlovits, and Samuel Wagner at the National Center of Biotechnology Information (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4388319/):
- "Inner membrane export apparatus: All T3SSs contain five highly conserved inner membrane proteins that are essential for their function (InvA, SpaP, SpaQ, SpaR and SpaS in Salmonella)"

### Summary
The proteins I identified using BLAST were SpaR, SpaP, SpaS, and ATPase which all had top results listed as Salmonella Enterica. I conclude that these genes likely came from Salmonella Enterica bacteria. Also, all three genes describe proteins used by Type III secretion systems (T3SS), with SpaP, SpaR, and SpaS being related to the formation of the inner membrane and ATPase causing the unfolding of proteins.

## Reflection
#### What are some opportunities to use gene finding technology to benefit others?
To sequence the amino acids in order to identify bacteria and viruses and find effective immunizations/medicines to treat them.

#### What are some of the program's limitations?
It does not analyze or interpret the meaning of the proteins found or figure out what organism it came from. Also its' accuracy is probably not as high as commercial technology created by people with degrees in biocomputation or other related topics.

#### What are the downsides of the program's limitations if used beyond what it's explicitly good for?
It could somehow missequence the genes/amino acids/proteins, or someone may not know how to interpret its' output or may interpret it incorrectly.

#### How could you adapt the program to enable more advanced applications?
Make the output more readable by synthesizing how many of each protein were found in the data, excluding any repeat listings. Secondly, having the program reference known protein databases and interpret what organism the genetic sequence came from with percentage match, similar to how BLASTp does, but for multiple proteins in combination.
