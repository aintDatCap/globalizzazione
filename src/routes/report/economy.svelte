<script>
	import Navbar from '$lib/navbar.svelte';
	import graph from '$lib/assets/economic_growth_graph.png';
</script>

<Navbar />

<article>
	<h2 class="title">Economia</h2>
	<p class="description">
		Parlando di globalizzazione a livello economico possiamo parlare di mercato globale. Citando il
		professor Luciano Gallino possiamo definire la globalizzazione economica come: “Il processo di
		costruzione di un mercato a livello planetario”. Il mercato globale ha avuto un grosso impulso
		dalle NICT (New Information and Communication Technologies) che hanno completamente eliminato le
		distanze fisiche trasformando il mercato globale in un cyber-mercato creando così anche la
		possibilità di trasformare dati, in merci e capitali dando così il via all’era del tutto in
		tempo reale. La globalizzazione a livello economico ha portato diversi benefici alla maggior
		parte degli Stati come ad esempio un arricchimento generale (1) e la possibilità di avere tutti
		i prodotti in ogni periodo dell’anno.

		<!-- Grafico qui -->

		<img src={graph} alt="graph" width="200" height="200"/>
		Questo tipo di “globalizzazione” investe in larga misura anche i cittadini, i lavoratori, le imprese,
		le comunità locali, tutte categorie fortemente implicate negli effetti del processo, tra i quali:
		l’aumento delle disuguaglianze all’interno del sistema di stratificazione sociale; l’aumento della
		disoccupazione e la riduzione dei salari reali; la scomparsa di una reale concorrenza di fronte al
		monopolio delle grandi multinazionali; il degrado economico, e talvolta l’annichilimento fisico di
		intere comunità, costrette dalla dipendenza da forze economiche esterne e a un permanente sottosviluppo.
		Questi aspetti negativi della globalizzazione si possono risolvere andando a limitare i poteri delle
		grandi multinazionali, ad esempio attraverso delle sanzioni alle aziende che decidono di delocalizzare
		oppure dare incentivi alle aziende che decidono di aprire nuove filiali all’interno dei confini del
		proprio Stato. In questo modo si potrebbe limitare il loro potere nei paesi meno sviluppati e proteggere
		anche industrie artigianali locali che non possono competere con le grandi industrie.
	</p>
</article>
<style>
	.description {
		margin-left: 3em;
		text-align: justify;
		margin-right: 3em;
	}

	.title {
		margin-left: 1em;
	}
</style>