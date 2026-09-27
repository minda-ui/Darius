# SmartCabinet online manual — captured text of the CN/tool chain, 2026-09-27

**What this is.** The extracted text of the four pages of the SmartCabinet online manual that
`Wiki/Software/smartcabinet-online-manual.md` rests its findings on, captured so the findings survive the
vendor changing or removing the site. **It is a vendor document, not this KB's work, and it is in
Italian** — reproduced here for citation only.

**How it was taken.** Fetched over HTTPS on **2026-09-27**, each returning **HTTP 200**; the stored HTML
was converted to text by script (tags stripped, entities unescaped, blank lines collapsed) — *not
retyped, and not a model's summary of the page.* The `sha256` below is of the **HTML as served**, so a
future session can re-fetch and tell at once whether the vendor has changed the page.

*The HTML itself is not kept: 230 KB of vendor markup that can be re-fetched at will, and the hash is
what makes re-fetching checkable. Six further pages were read and are cited in the article without being
captured here; their hashes are in the article's own provenance table.*

| Page | URL | HTML bytes | sha256 of the HTML as served |
|---|---|---|---|
| `cn.html` | `https://www.smartcabinet.eu/manuale/mainit/smartcabinet/cn.html` | 46,271 | `be19a6481ce9e5667f0a9d1e4e6d62b4f175a17bf93f3b178dc2ea94ad7b2979` |
| `cnc.html` | `https://www.smartcabinet.eu/manuale/mainit/smartcabinet/cnc.html` | 6,382 | `2f146991afe3a5c0236d523dd003f8d161cf9da09dc7ef7834575a3a0e002cb3` |
| `tabelle_cam_accessori_utensili.html` | `https://www.smartcabinet.eu/manuale/mainit/smartcabinet/tabelle_cam_accessori_utensili.html` | 7,180 | `113fb21f3567c1dc81d0acc817debf10ce7884c784a51d9d544b820bd324f367` |
| `lavorazioni.html` | `https://www.smartcabinet.eu/manuale/mainit/smartcabinet/lavorazioni.html` | 5,430 | `83ca5e731a08db15cf54cb2435889b18b260f93cc8889f5ff260732d598a9f90` |

## `cn.html` — Configurazione CN - the machine-configuration page: postprocessor, origins, tools for cuts/trim/finishing, 5ax, inclined cuts, inclined drilling, nesting

*46,271 B of HTML, sha256 `be19a6481ce9e566`. Text exactly as extracted:*

```text
La finestra seguente contiene invece i parametri relativi allo Schienale , la parte più in alto di questo paragrafo è relativa alla lavorazione per lo schienale a incastro , vediamo ora le opzioni disponibili.
Per prima cosa troviamo l'utensile principale ➊ da utilizzare nelle varie parti della struttura per alloggiare lo schienale, con l'opzione per l'esecuzione di una seconda passata ➋ , inoltre è possibile impostare una leggera maggiorazione nello spessore del canale ➌ , o "aria" in modo da alloggiare più agevolmente lo schienale.
Per le lavorarazioni dello schienale è possibile utilizzare una fresa ➍ , una lama ➎ o anche un'impostazione ibrida con lama + fresa ➏ , in quest'ultimo caso la fresa viene utilizzata per realizzare il canale nelle parti a vista, mentre per le parti in cui il canale non è visibile viene utilizzata la lama,
E' possibile impostare utensili differenti per le lavorazioni sull'asse X ➐ , sull'asse Y ➑ così come pure per le lavorazioni oblique ➒ possibili con una macchina a 5 assi, per ciascuno degli utensili impostati va impostato il relativo spessore.
Sono possibili eventuali estensioni delle fresate ➓ , magari in presenza di dimensioni maggiori di quanto specificato ⓫ , con la possibilità anche di impostare un numero di passate aggiuntive ⓬ , ed è anche possibile accorciare o allungare le lamate ⓭ , il consiglio è di provare inizialmente a lavorare con questi parametri impostati a 0 ed eventualmente fare aggiustamenti successivamente se si rivelano necessari.
I parametri nella parte sottostante sono relativi alla lavorazione dello schienale con battuta , abbiamo gli utensili da impostare per le lavorazioni nella struttura ⓮ e per quelle nello schienale ⓯ stesso, con la possibilità di impostare la correzione ⓰ laterale dell'utensile. Più in basso è possibile impostare se necessario un'eventuale estensione delle fresate nella struttura ⓱ e nello schienale ⓲ . Per questi ultimi due parametri vale quanto detto per il punto sopra, conviene provare a lavorare con questi impostati a 0 e fare eventuali aggiustamenti solo se se ne sente la necessità. Per finire abbiamo in basso la scelta della fresa per realizzare l'antischeggia ⓳ sulle parti della struttura, nel caso si utilizzi per lo schienale una battuta a L.
Questa pagina divisa in paragrafi contiene i parametri per la configurazione della macchina in uso, qui troviamo le impostazioni per svariati utensili, tipicamente frese e lame in quanto le punte a forare vengono normalmente selezionate automaticamente, questi utensili devono essere stati preventivamente inseriti in Tabelle CAM Accessori sotto Utensili .
N.B. : In questa pagina è possibile impostare la configurazione CN di default , oppure modificarla solo per il cabinet correntemente aperto a seconda che questa pagina venga aperta utilizzando il pulsante CAM in alto a destra, oppure utilizzando il pulsante CN (fulmine) accessibile a sinistra dal menu Settaggi cabinet , quest'ultimo consente di effettuare modifiche alla configurazione CN solo relativamente al cabinet correntemente aperto lasciando invariata la configurazione di default. Se dovesse emergere l'esigenza ricorrente di modifiche alla configurazione CN di default il consiglio è di creare nella pagina CAM una copia della configurazione CN in uso e modificare quindi i parametri in questa.
A sinistra in alto troviamo raggruppate in un menu a tendina la selezione del postprocessor da utilizzare con SmartCabinet, va selezionato quello che corrisponde alla macchina in uso, se nella lista è presente solo la voce Gen 1 il modulo CN non è attivo in SmartCabinet.
Immediatamente a destra troviamo il pulsante Origini , cliccando su questo pulsante appariranno alcune impostazioni che la macchina utilizzerà per determinare il punto di partenza delle lavorazioni. Oltre all'origine predefinita ➊ si può impostare anche un'origine alternativa ➋ per i pezzi più larghi di quanto impostato ➌ e un'ulteriore origine alternativa ➍ per i pezzi più alti di quanto impostato ➎ . Sia per l'origine predefinita che per quella alternativa è possibile scegliere la modalità " a spingere " ➏ oppure quella " a tirare " ➐ . E' disponibile inoltre per il postprocessor Biesse l'opzione Pendular ➑ che consente la lavorazione bidirezionale, anche in questo caso oltre all'origine predifinita ➒ è disponibile un'origine alternativa ➓ . Selezionando l'ultima opzione ⓫ è possibile evitare la specchiatura a destra per le origini 2, 4, 8, 12 e 16.
Per una corretta impostazione di questi parametri è in ogni caso opportuno consultare il produttore della macchina.
N.B. : Quando è attivata l'opzione Pendular ➑ viene generato per ciascun pezzo un file CN aggiuntivo che presenta la desinenza _DX alla fine del nome.
Proseguendo verso destra troviamo infine la selezione del Riferimento che la macchina utilizzerà per lavorare i pezzi, anche in questo caso è opportuno consultare il produttore della nostra macchina perchè ci consigli la corretta impostazione.
Back to the Top
A seguire troviamo una finestra ricca di opzioni relative al Rifilo . Accanto al titolo della finestra troviamo una casella che possiamo eventualmente deselezionare se non siamo interessati a rifilare i pezzi con la nostra macchina. Esaminiamo ora una per una le opzioni disponibili.
E' possibile generare per ciascun pezzo singoli file CN che includano il rifilo e tutte le altre lavorazioni ➊ , oppure generare per ciascun pezzo un file CN per il rifilo e un secondo file CN per tutte le altre lavorazioni ➋ , questa scelta può essere differenziata per la struttura a , per le ante b e per i frontali dei cassetti c .
Va quindi specificato lo spessore del rifilo ➌ , specificando anche se desideriamo che a questo venga sommato lo spessore di eventuali bordi ➍ .
E' possibile quindi attivare le lavorazioni interne ➎ , specificando eventualmente gli utensili da utilizzare per i due lati di entrata nei pezzi a , con il relativo numero di passate b , se qui non viene specificato alcun utensile questo viene selezionato automaticamente. E' eventualmente possibile che in fase di taglio le parti tagliate non vengano completamente separate c , opzione particolarmente utile per le macchine verticali.
Proseguendo troviamo la selezione degli utensili per il rifilo della struttura ➏ e delle ante / cassetti ➐ , è eventualmente possibile impostare lo stesso utensile per entrambi, per ciascuno è possibile impostare un offset di profondità aggiuntiva ➑ , sono consentiti anche offset negativi se vengono inseriti valori negativi.
E' possibile differenziare l'utensile anche per dimensione del pezzo da rifilare spuntando la relativa casella ➒ , verrà quindi selezionato un utensile a nel caso di dimensioni maggiori del numero impostato c e un altro utensile b nel caso che la dimensione sia inferiore a quanto impostato c , oltre al numero di passate da eseguire d . Poco più a destra è possibile in ogni caso impostare un particolare numero di passate ➓ da eseguire nel caso che le dimensioni siano inferiori a quanto specificato ⓫ .
Di seguito si possono impostare gli utensili per eseguire la finitura dei pezzi, se ne possono impostare due per la struttura ⓬ e due per le ante / cassetti ⓭ , per ciascuno è possibile impostare un offset di profondità aggiuntiva a e anche una raggiatura b per evitare gli spigoli vivi.
Va poi impostato il punto di entrata dell'utensile ⓮ , angolare o centrale, la correzione laterale ⓯ e un'eventuale raggiatura ⓰ per evitare gli spigoli vivi.
E' poi possibile impostare una dimensione minima ⓱ al di sotto della quale le parti dello Zoccolo a , le Traverse b , o le catene c per il Cielo e il Fondo non devono essere rifilati, oppure semplicemente nella parte destra possiamo disattivare il rifilo ⓲ per i Top a , per gli Schienali b , per le Cornici c , per i Telai d , per la scatola e e per il fondo dei Cassetti f .
Se alcuni pezzi hanno una dimensione verticale eccessivamente maggiore della dimensione orizzontale è possibile che vengano automaticamente ruotati ⓳ per consentirne una lavorazione più agevole in macchina, questa opzione è attivabile per le parti della struttura a , per le ante e i frontali dei cassetti b e per gli Schienali c .
Successivamente troviamo le impostazioni relative agli utensili che devono esegire i tagli ⓴ , se si desidera che tutti i tagli lineari vengano eseguiti con una lama va spuntata la relativa casella a , attivando questa opzione qualsiasi altra selezione di frese per i tagli verrà ignorata nel caso di tagli lineari.
Quindi troviamo la selezione dell'utensile per i tagli lungo gli assi X b , Y c e obliqui d , oltre all'impostazione della correzione laterale e e il numero di passate g da eseguire qualora la dimensione del pezzo sia maggiore di quanto specificato f .
Tagli fuori squadro
Le opzioni che seguono riguardano l'impostazione degli utensili per i tagli ad angoli diversi da 90°, risultano visibili solo per alcuni postprocessor . Va selezionata una fresa a o una lama b , se nulla viene selezionato viene utilizzata automaticamente una lama. Nel caso sia selezionata una fresa è possibile impostare il numero delle passate aggiuntive c , queste verranno eseguite a condizione che lo spessore del pezzo da tagliare sia maggiore di quanto specificato nell'apposita casella d .
5ax
Se la nostra macchina non è una 5 assi dobbiamo spuntare questa casella ➊ , se la casella è spuntata e quindi la macchina non ha 5 assi i parametri nei due riquadri successivi non hanno effetto.
Tagli Inclinati
Qui possiamo indicare il nome dell'utensile ➋ per i tagli inclinati, il suo diametro ➌ e il suo spessore ➍ , se si tratta di una lama ➎ dobbiamo spuntare la casella in basso.
Fresa per forature inclinate
Qui invece indichiamo l'utensile di tipo fresa da utilizzare per le forature inclinate, a parte il nome ➏ dell'utensile l'unico parametro da specificare qui è il suo diametro ➐ .
Successivamente possiamo indicare la massima profondità di ogni singolo step di foratura ➊ , se un foro sarà più profondo di questo valore verrà eseguito in più steps. Subito a destra possiamo specificare che per i fori meno profondi del valore indicato verrà utilizzata una punta a V (lancia) ➋ .
Il menu ➌ e il relativo pulsante che raffigura una ruota dentata ➍ compaiono solo quando vengono selezionate alcune particolari configurazioni cn in cui è necessario specificare gli utensili per le forature, cliccando sul pulsante ➍ compare la finestra per la configurazione di questi utensili, le configurazioni salvate sono poi selezionabili dal menu a tendina ➌ .
Se è necessario specificare un nuovo utensile basta cliccare in basso sul pulsante + ➎ e poi dal menu a tendina Tool ➏ selezionare l'utensile, che dev'essere stato preventivamente inserito in Tabelle CAM Accessori sotto Utensili . Oltre al diametro ➐ sono da selezionare poi la direzione ➑ della foratura, il tipo ➒ di foro che l'utensile dovrà praticare e se si tratta di una punta o di una fresa ➓ . Le singole righe inserite si possono poi eventualmente cancellare utilizzando il pulsante in basso ⓫ .
Infine se è attivo il modulo per il Nesting/Ottimizzazione in questa finestra troviamo le impostazioni che la macchina utilizzerà per la lavorazione dei pezzi, l'utensile principale ➊ da utilizzare per il taglio è la prima selezione in alto. Subito sotto possiamo eventualmente impostare un utensile ➋ per spessori maggiori di quanto indicato ➌ , il numero di passate ➍ va indicato a destra nel campo con le frecce arancioni. Immediatamente sotto possiamo impostare il numero di passate ➎ nel caso di dimensioni dei pannelli minori di quanto indicato ➏ .
Più in basso possiamo impostare la profondità a cui la fresa dovrà scendere ➐ per lavorare il pezzo e subito sotto lo spessore del pannello "martire" ➑ , cioé quel pannello che sta tra le ventose e il pezzo da lavorare.
Le caselle più in basso corrispondenti ai pallini nero e verde indicano che in fase di nestig desideriamo che vengano anche eseguite lavorazioni verticali, la spunta nel pallino nero indica le forature ➒ e quello verde indica le fresature ➓ , come mostrato nel disegno a sinistra. Queste lavorazioni ⓫ possono anche seguire una sequenza preimpostata, selezionandole possono essere spostate utilizzando le frecce in basso in modo che vengano eseguite prima ⓬ o dopo ⓭ di altre.
» Configurazione CAM » Configurazione CN
Indietro
```

## `cnc.html` — CNC - the button that generates the CN files, and where they are written

*6,382 B of HTML, sha256 `2f146991afe3a5c0`. Text exactly as extracted:*

```text
Questo pulsante ➊ presente nella barra degli strumenti a sinistra avvia la generazione dei file CN per la lavorazione in macchina dei pezzi del cabinet. A generazione avvenuta si apre una finestra ➋ con la richiesta di apertura della cartella in cui i file sono stati memorizzati. Per ogni pezzo viene generato un file ➌ , se è attivo il modulo Ottimizzatore/Nesting vengono generati anche i file relativi al taglio ottimizzato dei pannelli necessari ➍ . Questa funzione è presente anche nell'ambiente Render , in questo caso vengono generati i file CN per tutti i pezzi di tutti i cabinet presenti nella scena.
N.B.1 : I file CN vengono memorizzate in sottocartelle all'interno del percorso \Kosmosoft\SmartCabinet\CNC\ , le sottocartelle avranno nomi inerenti al postprocessor CN in uso, la configurazione di questo è accessibile dal menu CAM in Configurazione CN , oppure in Settaggi Cabinet sotto Configurazione CN Cabinet se relativo al solo cabinet correntemente aperto.
N.B.2 : E' possibile nei Settaggi impostare un percorso locale o di rete per la generazione dei file CN, il parametro è AutoCopyCNFolder e si trova nel paragrafo CAM . Impostando questo percorso i file potranno essere memorizzati direttamente nel pc a bordo macchina.
N.B.3 : E' possibile modificare i nomi dei pezzi e dei relativi file CN generati, l'impostazione si trova nei Settaggi in CN Names .
Back to the Top
» CNC
Indietro
```

## `tabelle_cam_accessori_utensili.html` — Tabelle CAM Accessori > Utensili - the tool table's fields

*7,180 B of HTML, sha256 `113fb21f3567c1dc`. Text exactly as extracted:*

```text
In questa finestra vanno inseriti gli utensili, tipicamente le frese e le lame ma per alcune macchine anche le punte , che è necessario specificare perchè non selezionati automaticamente.
Per ciascuno è necessario specificare un nome ➊ , questo sarà poi l'identificativo utilizzato dalla macchina per richiamare quello specifico utensile. Gli altri dati che di seguito possono essere specificati non sono sempre necessari: il senso di rotazione ➋ , che può essere orario o antiorario, il numero di giri di rotazione al minuto ➌ , l'avanzamento di mm al secondo ➍ , il diametro ➎ e la descrizione ➏ , quest'ultimo campo può eventualmente essere usato anche per brevi annotazioni sugli utensili. Cliccando col pulsante destro del mouse sui titoli delle colonne compare una finestra ➐ che permette di selezionare le colonne da visualizzare, nella barra in basso troviamo invece i pulsanti per l'inserimento di un nuovo utensile ➑ e per la cancellazione ➒ dell'utensile selezionato.
Back to the Top
» Top Menu » Tabelle CAM Accessori » Utensili
Indietro
```

## `lavorazioni.html` — Lavorazioni - the menu (Intagli, Lavorazioni a Onda)

*5,430 B of HTML, sha256 `83ca5e731a08db15`. Text exactly as extracted:*

```text
Da questo menu si accede a due tipi di lavorazioni: gli Intagli ➊ e le Lavorazioni a Onda ➋ ,
clicca sui pulsanti a sinistra per spiegazioni dettagliate.
Back to the Top
Indietro
» Lavorazioni
```

