
+++

title = "IA Generativa: Tecnologie ed Esempi di Utilizzo"
description = "Formazione su IA generativa"
outputs = ["Reveal"]

+++

{{% section %}}

# IA Generativa: Tecnologie ed Esempi di Utilizzo

[Giovanni Ciatto](mailto:giovanni.ciatto@unibo.it), Dipartimento di Informatica — Scienza e Ingegneria (DISI), Sede di Cesena,
<br> Alma Mater Studiorum—Università di Bologna

{{< image src="./front.webp" max-h="50vh" >}}

<span class="hint">(versione presentazione: {{< today >}})</span>


---

## Link a queste slide

<{{< slides-url >}}>

<!-- ![](./qr-slides.png) -->

[<i class="fa fa-print" aria-hidden="true"></i> versione stampabile](?print-pdf&pdfSeparateFragments=false)

{{% /section %}}

---

## __GenAI__: Intelligenza Artificiale _Generativa_

<!-- > [Sistemi basati su] <br> -->
Algoritmi di _IA_ in grado di __generare automaticamente__ _contenuti_, e.g.:
- _testo_
- immagini
- audio e/o video
- codice [di programmazione]
- ...

(cf. [Policy per un uso etico e responsabile dell’Intelligenza Artificiale Generativa nelle attività di didattica e ricerca](https://www.unibo.it/it/allegati/policy-per-un-uso-etico-e-responsabile-dell2019intelligenza-artificiale-generativa-nelle-attivita-di-didattica-e-ricerca/@@download/file/Policy-Generative-AI.pdf))

---

## GenAI mediante _Modelli Fondazionali_ (FM)

+ Grosse _reti neurali_ che imparano ad _elaborare_, _"capire"_, e _produrre_ __dati non__ [necessariamente] __strutturati__
+ __allenati__ su _grandi_ quantità di dati, e con _grandi_ risorse computazionali, a __fare un po' tutto__
    - con l'idea di poterli poi __specializzare__ per _compiti specifici_

<br>
{{< image src="./foundation-models.png" max-h="60vh" alt="Concept dei modelli fondazionali">}}

---

## Modelli Fondazionali vs. Large Language Models

{{< image src="./fm-vs-llm.webp" width="80%" max-h="70vh" alt="Diagramma di Venn che spiega come gli LLM siano un caso particolare di modelli fondazionali " link="https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404" >}}

---

## GenAI con modello di consumo _as-a-Service_

<br>
{{< image src="./llm-concept.svg" width="100%" max-h="70vh" alt="Modello di consumo 'as a Service' per i modelli fondazionali" >}}

---

{{% section %}}

## Ciclo di apprendimento di GenAI


<br>
{{< image src="./dataflow.svg" width="100%" max-h="70vh" alt="Ciclo di apprendimento di GenAI" >}}

---

## Alcune soluzioni tecnologiche permettono di _scegliere_ (pt. 1)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-1.png" width="100%" morestyle="border: 1px solid black" >}}

---

## Alcune soluzioni tecnologiche permettono di _scegliere_ (pt. 2)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-2.png" width="100%" morestyle="border: 1px solid black" >}}

---

## Alcune soluzioni tecnologiche permettono di _scegliere_ (pt. 3)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-3.png" width="100%" morestyle="border: 1px solid black" >}}


---

## Alcune soluzioni tecnologiche permettono di _scegliere_ (pt. 4)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-4.png" width="100%" morestyle="border: 1px solid black" >}}

{{% /section %}}

---

{{< slide id="interfaces" >}}

# Principali soluzioni __tecnologiche__

## Categorizzate per tipo di __interfaccia__

- _Conversazionali_: e.g. [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/login?returnTo=%2F%3F), [Scite](https://scite.ai)
- _Auto-completamento_: e.g. [GitHub Copilot](https://github.com/features/copilot)
- _Programmatiche_: e.g. [OpenAI Platform](https://openai.com/api/), [Hugging Face](https://huggingface.co/)
- _In-App_: e.g. [Microsoft 365 Copilot](https://www.microsoft.com/it-it/microsoft-365/copilot?market=it)
- _Editing di audio-visivi_: e.g. [Suno](https://suno.com/), [Runway](https://runwayml.com/)
<!-- - _Ispezione di materiale generato_: e.g. [GPTZero](https://gptzero.me/), [ZeroGPT](https://www.zerogpt.com/) -->

---

## Interfaccia __conversazionale__

{{% multicol %}}
{{% col %}}
{{< image src="./logo-chatgpt.svg" height="2em" >}}
{{< image src="./interface-conversational.png" width="100%" link="https://chatgpt.com/share/6798dd04-8a98-8008-a751-bc374318bd9e" >}}
{{% /col %}}
{{% col %}}
<br>

- Interazione _testuale_ che mima una _corrispondenza_ (__chat__)
    + l'utente chiede, l'IA risponde _reattivamente_
- L'interfaccia permette l'inserimento di un __prompt__
    + opzionalmente contenente _allegati_ (e.g. immagini, documenti)
- Le risposte sono __contestuali__
    + i.e., lo _storico_ della conversazione impatta le risposte _future_
- La risposta contiene __testo__ (spesso _formattato_)
    + opzionalmente: _immagini_, URL, codice

{{% fragment %}}

### Talvolta...

- ... prima di rispondere, l'IA fa una __ricerca__ su _Web_
- importante per avere risultati _aggiornati_

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## Interfaccia basata su __auto-completamento__

{{% multicol %}}
{{% col %}}
{{< image src="./logo-copilot.svg" height="2em" >}}
{{< image src="./interface-autocompletion.gif" width="100%" >}}
{{% /col %}}
{{% col %}}
<br>

- L'IA _suggerisce_ un __completamento__ per il testo inserito
    + e.g., codice, testo, URL
- L'utente __accetta__ (anche in parte) o _ignora_ il suggerimento
- Usato anche e soprattutto per __codice__ di _programmazione_

{{% fragment %}}

### Attenzione...
- ... modello di costo ad __abbonamento__ (vedi [qui](https://github.com/features/copilot/plans))
- ... potenziali __leak__ di informazioni _sensibili_
- ... rischio di __lock-in__ non trascurabile

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## Interfaccia __programmatica__

{{% multicol %}}
{{% col class="col-6" %}}
{{< image src="./logo-openai.svg" height="2em" >}}
```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="sk-1234567890abcdef1234567890abcdef")

async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            dict(role="user",
                 content="European countries, one by line")
        ],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end=", ")

asyncio.run(main())
```

Output:
```plaintext
Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Vatican City (Holy See),
```
{{% /col %}}
{{% col %}}

- __Linguaggio di programmazione__ che interagisce con IA
    + e.g., _Python_, JavaScript

- L'interazione rimane di tipo _richiesta-risposta_
    + il __programma__ invia una _richiesta_, l'IA _risponde_

{{% fragment %}}

### Abilitante per 

- Prompt __parametrici__, risposte processate _automaticamente_
    + es. `list of LOCALITIES in AREA, one by line`
        + dove `LOCALITIES` $\in$ {`cities`, `regions`, `states`}
        + e `AREA` $\in$ {`Europe`, `Asia`, `Africa`, `America`, `Oceania`}
        + risultati _ordinati alfabeticamente_

- Scrittura __software__ che usa l'IA come __servizio__
    + utile in _industria_ come in _ricerca_

{{% /fragment %}}

{{% fragment %}}

### Attenzione...
- ... modello di costo __a consumo__ (vedi [qui](https://openai.com/api/pricing/))
    + proporzionale al numero di _token_ processati
    + prezzi variabili _per modello_

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## Interfaccia __in-app__

{{% multicol %}}
{{% col %}}
{{< image src="./logo-copilot-office.svg" height="2em" >}}
{{< image src="./interface-inapp.gif" width="100%" >}}
{{% /col %}}
{{% col %}}
<br>

- GenAI integrata in __applicazioni__ _desktop_ o _web_
    + e.g., _Microsoft Office_ (Word, Excel, Outlook)

- supporto per interfaccia __conversazionale__ _interna_
    + conversazione intrinsecamente _contestualizzata_

- IA __automatizza__ _operazioni complesse_ (interne all'app)
    + e.g., _scrittura_ di bozze
    + e.g., _generazione_ di formule, grafici 

{{% fragment %}}

### Attenzione...
- ... modello di costo ad __abbonamento__ (vedi [qui](https://www.microsoft.com/it-it/microsoft-365/copilot?market=it#plans))
- ... potenziali __leak__ di informazioni _sensibili_
- ... rischio di __lock-in__ non trascurabile

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}} 

---

## Interfaccia per __editing__ di audio-visivi (e.g. _musica_)

{{% multicol %}}
{{% col %}}
{{< image src="./logo-suno.svg" height="2em" >}}
{{< image src="./suno/generate-song-1.png" width="100%" >}}
{{% /col %}}
{{% col %}}
- Interazione __one-shot__ per generare il contenuto
    + _input_: descrizione testuale del contenuto
    + _output_: contenuto

- L'interfaccia permette poi 
    + _riproduzione_ del contenuto
    + __modifica__ del contenuto
        + e.g., _taglio_ di parti, _modifica_ di tonalità

{{% fragment %}}

### Esempio

- ["Canzona di Bacco" (Lorenzo il Magnifico, 1490)](https://it.wikipedia.org/wiki/Il_trionfo_di_Bacco_e_Arianna_(poesia)), rock
    + <https://suno.com/song/cce33ee7-a581-47ae-b9d1-806902e88e47>

{{% /fragment %}}    
{{% /col %}}
{{% /multicol %}}

---

{{< slide id="modes" >}}

# Principali __modalità d'utilizzo__

## Categorizzate per __ruolo di GenAI__

### GenAI come... 

* ... _motore di ricerca_: uso GenAI per __ricercare__ informazioni
* ... _assistente di (ri)scrittura_: uso GenAI per __(ri)scrivere__ documenti
* ... _assistente di lettura_: uso GenAI per __acquisire informazioni__ da documenti
* ... _generatore di contenuti_: uso GenAI per __creare__ contenuti

---

## GenAI come _motore di ricerca_

### Disclaimer

> GenAI __non è__ un _motore di ricerca_ come Google, Bing, DuckDuckGo, etc.

{{% fragment %}}

- FM, di base, __non accedono__ al Web (__né interrogano__ qualche sorgente) prima di rispondere
    * alcune tecnologie specifiche possono farlo, ma non c'è garanzia

- FM, di base, rispondono in base a _dati_ e _conoscenze_ acquisite durante __l'allenamento__
    * informazioni _successive_ all'ultimo ciclo di apprendimento potrebbero non essere considerate

- FM possono essere immaginati come __grandi memorie__
    * in cui (porzioni de) lo _scibile umano_ è stato _"registrato"_
    * interrogabili tramite il _linguaggio naturale_

- Le risposte di GenAI non vanno _mai_ accettate __acriticamente__, in quanto suscettibili di _allucinazioni_:
    * __errori__: informazioni fattualmente false o inventate, riportate con sicumera
    * __fraitendimenti__: informazioni fuori contesto o non pertinenti rispetto all'aspettativa dell'utente
    * __bias__: di campionamento delle informazioni, di selezione del motore di ricerca, intrinseci nel linguaggio, etc.

{{% /fragment %}}

---

## GenAI come _motore di ricerca_

### Razionale

<br>

Possiamo considerare FM come __esperti__ su tematiche che:
* siano temporalmente _consolidate_ $\implies$ diffidare di risposte su temi _recenti_
* siano relativamente _popolari_ $\implies$ diffidare di risposte su temi _di nicchia_

{{% fragment %}}

### <br> Consigli sempre validi

* verificare le __fonti__ menzionate da GenAI
   - esistono davvero? sono aggiornate?

* verificare l'__aderenza__ alle fonti
    - la fonte dice davvero quello che GenAI ha riportato?

{{% /fragment %}}

---

{{% section %}}

{{< slide id="example-search-chatgpt-mas" >}}

## GenAI come _motore di ricerca_

### Esempio: esplorazione sull'argomento ["Sistemi multi-agente"](https://en.wikipedia.org/wiki/Multi-agent_system), con ChatGPT

> Un sistema multi-agente (MAS) è un tipo di sistema composto da __molteplici agenti indipendenti__ (ma _interattivi_), ciascuno capace di _percepire_ il proprio ambiente e di intraprendere _azioni_. 
> Gli agenti possono essere _modelli di IA_, programmi _software_, _robot_ e altre _entità computazionali_. 
> _Molteplici agenti_ possono _cooperare_ o verso un _obiettivo comune_ che va oltre le capacità dei singoli agenti, con una maggiore adattabilità e robustezza.

(cf. <https://www.gartner.com/en/information-technology/glossary/multiagent-systems>)

<br>

### Link alla conversazione completa

<https://chatgpt.com/share/e/679a41e7-e164-8004-8f01-d135dde3892c>

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-1.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- Definizione __corretta__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-2.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- Caratteristiche __corrette__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-3.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- Le applicazioni _menzionate_ sono __corrette__
- _Nessuna_ garanzia di __esaustività__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-4.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- _Nessuna_ garanzia di __esaustività__
- Nessun riferimento per [AlphaStar](https://deepmind.google/discover/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii/)
- Interserzione con _altre nicchie_
    + __blockchain__, __protocolli di consenso__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-5.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- Gli aspetti _menzionati_ hanno __fondamenta solide__
- Lista __incompleta__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-6.png" width="100%" max-h="90vh" >}}
{{% /col %}}
{{% col %}}
- Tutte menzioni __corrette__
- _Nessuna_ garanzia di __esaustività__
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-7.png" width="100%" max-h="90vh" link="https://arxiv.org/abs/1706.02275" >}}
{{% /col %}}
{{% col %}}
- [Link ad Arxiv](https://arxiv.org/abs/1706.02275) __corretto__
- Riferimento _adeguato_ al contesto corrente
- No riferimeto a [paper definitivo](https://dl.acm.org/doi/10.5555/3295222.3295385)
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-8.png" width="100%" max-h="90vh" link="https://arxiv.org/abs/1903.08082" >}}
{{% /col %}}
{{% col %}}
- Riferimento _adeguato_ al contesto corrente
- [Link ad Arxiv](https://arxiv.org/abs/1903.08082) __incoerente__ col riferimento
- Il paper menzionato ha un __altro URL__: 
    + <https://arxiv.org/abs/2011.05373>
- No riferimeto a [paper definitivo](https://dl.acm.org/doi/10.5555/3495724.3497048)
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-9.png" width="100%" max-h="90vh" link="https://arxiv.org/abs/1906.01220" >}}
{{% /col %}}
{{% col %}}
- Riferimento _**in**adeguato_ al contesto corrente
- [Link ad Arxiv](https://arxiv.org/abs/1906.01220) __incoerente__ col riferimento
- Il paper menzionato ha un __altro URL__: 
    + <https://arxiv.org/abs/1809.03531>
- No riferimeto a [paper definitivo](https://doi.org/10.1109/LRA.2019.2903261)
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-10.png" width="100%" max-h="90vh" link="https://arxiv.org/abs/1910.05789" >}}
{{% /col %}}
{{% col %}}
- [Link ad Arxiv](https://arxiv.org/abs/1910.05789) __corretto__
- Riferimento _adeguato_ al contesto corrente
- No riferimeto a [paper definitivo](https://dl.acm.org/doi/10.5555/3454287.3454752)
{{% /col %}}
{{% /multicol %}}

---

{{% multicol %}}
{{% col %}}
{{< image src="./search-engine/chatgpt/mas-11.png" width="100%" max-h="90vh" link="https://arxiv.org/abs/1803.08884" >}}
{{% /col %}}
{{% col %}}
- [Link ad Arxiv](https://arxiv.org/abs/1803.08884) __corretto__
- Riferimento _adeguato_ al contesto corrente
- No riferimeto a [paper definitivo](https://dl.acm.org/doi/10.5555/3327144.3327252)
{{% /col %}}
{{% /multicol %}}


{{% /section %}}

---

![The end](./end.webp)